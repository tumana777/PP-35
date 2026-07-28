from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse
from store.models import Product
from store.forms import AddProductForm

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


def add_product(request):
    if request.method == 'POST':

        # print(request.POST)

        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save()
            # product = form.save(commit=False)
            #
            # product.quantity = 10
            #
            # product.save()

            return redirect('store:products')
    else:
        form = AddProductForm()

    return render(request, 'add_product.html', {'form': form})


def update_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            return redirect('store:product_detail', product_pk=product_pk)

    form = AddProductForm(instance=product)

    return render(request, 'update_product.html', {'form': form})

def delete_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        product.delete()

    return redirect('store:products')
















