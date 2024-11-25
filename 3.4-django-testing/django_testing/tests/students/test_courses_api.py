import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
	return APIClient()


@pytest.fixture
def courses_factory():
	def factory(*args, **kwargs):
		return baker.make(Course, *args, **kwargs)
	return factory


@pytest.fixture
def students_factory():
	def factory(*args, **kwargs):
		return baker.make(Student, *args, **kwargs)
	return factory


@pytest.mark.django_db
def test_retrieve(client, courses_factory):
	course = courses_factory(_quantity=1)
	response = client.get(f"/api/v1/courses/{course[0].id}/")
	data = response.json()
	assert response.status_code == 200
	assert data["name"] == course[0].name


@pytest.mark.django_db
def test_list(client, courses_factory):
	courses = courses_factory(_quantity=3)
	response = client.get("/api/v1/courses/")
	data = response.json()
	assert response.status_code == 200
	assert len(data) == len(courses)


@pytest.mark.django_db
def test_filter_course_id(client, courses_factory):
	course = courses_factory(_quantity=5)
	response = client.get("/api/v1/courses/", data={"id": course[0].id})
	data = response.json()
	assert response.status_code == 200
	assert data[0]["id"] == course[0].id


@pytest.mark.django_db
def test_filter_course_name(client, courses_factory):
	course = courses_factory(_quantity=5)
	response = client.get("/api/v1/courses/", data={"name": course[0].name})
	data = response.json()
	assert response.status_code == 200
	assert data[0]["name"] == course[0].name


@pytest.mark.django_db
def test_create(client):
	data = {
		"name": "Python с нуля"
	}
	response = client.post("/api/v1/courses/", data=data)
	assert response.status_code == 201
	assert Course.objects.count() == 1
	assert response.data["name"] == data["name"]


@pytest.mark.django_db
def test_patch(client, courses_factory):
	course = courses_factory(_quantity=1)
	data = {
		"name": "Python продвинутый курс"
	}
	response = client.patch(f"/api/v1/courses/{course[0].id}/", data=data)
	assert response.status_code == 200
	assert Course.objects.get(pk=course[0].id).name == data["name"]


@pytest.mark.django_db
def test_delete(client, courses_factory):
	course = courses_factory(_quantity=1)
	response = client.delete(f"/api/v1/courses/{course[0].id}/")
	assert response.status_code == 204
	assert Course.objects.count() == 0


@pytest.mark.django_db
def test_max_students(client, courses_factory, students_factory):
	course = courses_factory(_quantity=1)
	students = students_factory(_quantity=21)
	data = {
		"name": course[0].name,
		"students": [
			student.id for student in students
		]
	}
	response = client.post(f"/api/v1/courses/", data=data)
	assert response.status_code == 201
	assert len(response.data["students"]) == 21


