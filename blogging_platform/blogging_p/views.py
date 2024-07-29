from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render,redirect, get_object_or_404
from.forms import ProductForm
# Create your views here.



def product_list(request):
    products = Product.objects.all
    context = {'products': products}
    return render(request, 'product_list.html', context)

def product_detail(request, pk):
    products = Product.objects.get(pk=pk)
    context = {'products': products}
    return render(request, 'product_detail.html', context)

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
        
    # Render the form with any errors if the request method is GET or form is not valid
    return render(request, 'edit.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete.html', {'products': product})