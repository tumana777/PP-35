from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from store.models import Product

# def index(request):
#     return HttpResponse("<h1>Hello, world!</h1>")
#
# def about(request):
#     return HttpResponse("<h1>This is about page</h1>")
#
# def products_json(request):
#     products = Product.objects.values()
#
#     return JsonResponse(list(products), safe=False)

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    all_products = Product.objects.all()
    total = all_products.count()

    context = {
        'total': total,
        'products': all_products
    }

    return render(request, 'products.html', context=context)

def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    return render(request, 'product_detail.html', {'product': product})























