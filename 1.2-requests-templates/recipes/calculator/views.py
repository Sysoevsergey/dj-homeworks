from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def index(request):
    link = []
    for recipe in DATA.keys():
        link.append(f'<a href="/{recipe}/">{recipe}</a><br>')
    return HttpResponse(link)


def get_recipe(request):
    servings = int(request.GET.get('servings', 1))
    recipe_request = request.path[1:].replace('/', '')
    recipe = {}
    if recipe_request in DATA.keys():
        for key, value in DATA[recipe_request].items():
            recipe[key] = f'{servings * value:.2f}'

    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)
