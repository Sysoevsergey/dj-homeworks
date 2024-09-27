from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    data = Phone.objects.all()
    sort_pages = request.GET.get('sort')
    if sort_pages == 'min_price':
        data = data.order_by('price')
    elif sort_pages == 'max_price':
        data = data.order_by('-price')
    elif sort_pages == 'name':
        data = data.order_by('name')
    context = {"phones": data
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    data = Phone.objects.get(slug=slug)
    context = {'phone': data
               }
    return render(request, template, context)
