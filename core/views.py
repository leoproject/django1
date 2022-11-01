from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
from django.template import loader

def index(request):
    products = Product.objects.all()
    # print(dir(request.user))
    # print(f"User2:{request.user}")
    # print(type(request.user))

    if str(request.user) == 'AnonymousUser':
        test = "Not log user"
    else:
        test = "User logged"
    context = {
        'curso': 'Web programing with Framework Django.',
        'other': 'Django is great tool.',
        'test': test,
        'products': products,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def product(request, id):
    # prod = Product.objects.get(id=id)
    prod = get_object_or_404(Product, id=id)
    print('PK', id)
    context = {
        'product': prod,
    }
    return render(request, 'product.html', context)

def error404(request,exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html ; charset=utf8',status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html ; charset=utf8', status=404)