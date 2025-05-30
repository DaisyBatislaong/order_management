from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomerProfile
from .forms import CustomerProfileForm

def customer_list(request):
    customers = CustomerProfile.objects.filter(is_active=True)
    return render(request, "customer_list.html", {"customers": customers})

def customer_detail(request, pk):
    customer = get_object_or_404(CustomerProfile, pk=pk)
    return render(request, 'customer_detail.html', {'customer': customer})


# Creation of customers
def customer_create(request):
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerProfileForm()
    return render(request, 'customer_form.html', {'form': form})

def customer_edit(request, pk):
    customer = get_object_or_404(CustomerProfile, pk=pk)
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerProfileForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form, 'edit_mode': True})

