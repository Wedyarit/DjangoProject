from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def about(request):
    return render(request, 'mainapp/about.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def products(request):
    return render(request, 'mainapp/products.html')


def single_product(request):
    return render(request, 'mainapp/single-product.html')
