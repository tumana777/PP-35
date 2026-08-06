from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse
from store.models import Product
from store.forms import AddProductForm
from django.views.generic import TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

# def index(request):
#     return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

# def about(request):
#     return render(request, 'about.html')

class AboutView(TemplateView):
    template_name = 'about.html'

# def products(request):
#     all_products = Product.objects.all().select_related('category')
#     total = all_products.count()

#     context = {
#         'total': total,
#         'products': all_products
#     }

#     return render(request, 'products.html', context=context)


# class ProductsView(View):
#     @staticmethod
#     def get(request):
#         all_products = Product.objects.all().select_related('category')
#         total = all_products.count()

#         context = {
#             'total': total,
#             'products': all_products
#         }

#         return render(request, 'products.html', context=context)
    
class ProductsListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    queryset = Product.objects.all().select_related('category')
    # paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_queryset().count()
        print(context)
        return context

# def product_detail(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)

#     return render(request, 'product_detail.html', {'product': product})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    # context_object_name = 'product'


# def add_product(request):
#     if request.method == 'POST':

#         # print(request.POST)

#         form = AddProductForm(request.POST)

#         if form.is_valid():
#             form.save()
#             # product = form.save(commit=False)
#             #
#             # product.quantity = 10
#             #
#             # product.save()

#             return redirect('store:products')
#     else:
#         form = AddProductForm()

#     return render(request, 'add_product.html', {'form': form})


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('store:products')
    login_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.instance.quantity = 10
        return super().form_valid(form)


# def update_product(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)

#     if request.method == 'POST':
#         form = AddProductForm(request.POST, instance=product)

#         if form.is_valid():
#             form.save()

#             return redirect('store:product_detail', product_pk=product_pk)

#     form = AddProductForm(instance=product)

#     return render(request, 'update_product.html', {'form': form})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'update_product.html'
    form_class = AddProductForm
    pk_url_kwarg = 'product_pk'

    def get_success_url(self):
        return reverse_lazy('store:product_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.name = f'Updated {form.instance.name}'
        return super().form_valid(form)

# def delete_product(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)

#     if request.method == 'POST':
#         product.delete()

#     return redirect('store:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('store:products')
    pk_url_kwarg = 'product_pk'


class TechProductsView(ListView):
    model = Product
    template_name = 'tech_products.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(category__name='tech').select_related('category')











