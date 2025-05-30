from django import forms
from .models import CustomerProfile

class CustomerProfileForm(forms.ModelForm):
    # Fields for main address
    address_street = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    address_barangay = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    address_city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    address_province = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    address_region = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    address_country = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    address_zip_code = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))

    # Fields for shipping address
    shipping_street = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    shipping_barangay = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    shipping_city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    shipping_province = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    shipping_region = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    shipping_country = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    shipping_zip_code = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))

    # Fields for billing address
    billing_street = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    billing_barangay = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    billing_city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    billing_province = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    billing_region = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    billing_country = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))
    billing_zip_code = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}))

    class Meta:
        model = CustomerProfile
        fields = ['name', 'customer_type', 'email', 'phone', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}),
            'customer_type': forms.Select(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}),
            'phone': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md p-2'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'ml-2'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Populate initial data for the main address
        if self.instance and self.instance.address:
            for key in ['street', 'barangay', 'city', 'province', 'region', 'country', 'zip_code']:
                self.fields[f'address_{key}'].initial = self.instance.address.get(key, '')

        # Populate initial data for the shipping address
        if self.instance and self.instance.shipping_address:
            for key in ['street', 'barangay', 'city', 'province', 'region', 'country', 'zip_code']:
                self.fields[f'shipping_{key}'].initial = self.instance.shipping_address.get(key, '')

        # Populate initial data for the billing address
        if self.instance and self.instance.billing_address:
            for key in ['street', 'barangay', 'city', 'province', 'region', 'country', 'zip_code']:
                self.fields[f'billing_{key}'].initial = self.instance.billing_address.get(key, '')

    def clean(self):
        cleaned_data = super().clean()

        # Compose the JSON data from separate fields for main address
        cleaned_data['address'] = {
            'street': cleaned_data.get('address_street', ''),
            'barangay': cleaned_data.get('address_barangay', ''),
            'city': cleaned_data.get('address_city', ''),
            'province': cleaned_data.get('address_province', ''),
            'region': cleaned_data.get('address_region', ''),
            'country': cleaned_data.get('address_country', ''),
            'zip_code': cleaned_data.get('address_zip_code', ''),
        }

        # Compose the JSON data for shipping address
        cleaned_data['shipping_address'] = {
            'street': cleaned_data.get('shipping_street', ''),
            'barangay': cleaned_data.get('shipping_barangay', ''),
            'city': cleaned_data.get('shipping_city', ''),
            'province': cleaned_data.get('shipping_province', ''),
            'region': cleaned_data.get('shipping_region', ''),
            'country': cleaned_data.get('shipping_country', ''),
            'zip_code': cleaned_data.get('shipping_zip_code', ''),
        }

        # Compose the JSON data for billing address
        cleaned_data['billing_address'] = {
            'street': cleaned_data.get('billing_street', ''),
            'barangay': cleaned_data.get('billing_barangay', ''),
            'city': cleaned_data.get('billing_city', ''),
            'province': cleaned_data.get('billing_province', ''),
            'region': cleaned_data.get('billing_region', ''),
            'country': cleaned_data.get('billing_country', ''),
            'zip_code': cleaned_data.get('billing_zip_code', ''),
        }

        return cleaned_data

    def save(self, commit=True):
        self.instance.address = self.cleaned_data.get('address', {})
        self.instance.shipping_address = self.cleaned_data.get('shipping_address', {})
        self.instance.billing_address = self.cleaned_data.get('billing_address', {})
        return super().save(commit=commit)
