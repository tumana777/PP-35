from django import forms
from store.models import Product

# class AddProductForm(forms.Form):
#     name = forms.CharField()
#     price = forms.DecimalField()
#     quantity = forms.IntegerField()
#     description = forms.CharField(required=False)
#     category = forms.CharField()

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'price', 'quantity', 'description', 'category']
        exclude = ['is_available']