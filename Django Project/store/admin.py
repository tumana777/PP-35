from django.contrib import admin
from .models import Product, Category

# admin.site.register(Category)
# admin.site.register(Product)

admin.site.site_header = 'Store Admin'
admin.site.site_title = 'Admin Panel'
admin.site.index_title = 'Welcome to Store Admin'

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1 



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'is_available', 'category', 'created_at', 'total_price')
    ordering = ('created_at',)
    list_display_links = ['id', 'name']
    search_fields = ('name', 'category__name')
    list_filter = ('is_available', 'category')
    list_editable = ('price', 'is_available')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'category', 'description')
        }),
        ('Price Information', {
            'fields': ('price', 'quantity', 'is_available')
        }),
    )

    @admin.display(description='Total Price')
    def total_price(self, obj):
        return obj.price * obj.quantity
    