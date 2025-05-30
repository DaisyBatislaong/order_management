from django import forms
from .models import Product

# forms for creating product and updating
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'price', 'stock_quantity', 'unit', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input w-full border border-gray-300 rounded-md p-2'}),
            'sku': forms.TextInput(attrs={'class': 'form-input w-full border border-gray-300 rounded-md p-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-input w-full border border-gray-300 rounded-md p-2'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-input w-full border border-gray-300 rounded-md p-2'}),
            'unit': forms.Select(attrs={'class': 'form-select w-full border border-gray-300 rounded-md p-2'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'ml-2'}),
        }