from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {
        'products': products
    })


def detail_product(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {
        'product': product
    })


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {
        'category': category,
        'products': products
    })
