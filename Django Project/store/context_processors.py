from .models import Product

def global_context(request):
    return {
        'products': Product.objects.select_related('category')
    }