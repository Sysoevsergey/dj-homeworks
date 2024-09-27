from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.URLField(default='')
    release_date = models.DateField(default='')
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.id}; {self.name}; {self.price}; {self.image}; {self.release_date}; {self.lte_exists}; {self.slug}"
