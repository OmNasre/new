from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product, Contact
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    products = Product.objects.all()  # Query all products from the database
    return render(request, "product/index.html", {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_management')
        else:
            return render(request, 'product/login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'product/login.html')

@login_required
def product_management(request):
    products = Product.objects.all()
    return render(request, 'product/product_management.html', {'products': products})

# @login_required
# def remove_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     if request.method == 'POST':
#         product.delete()
#         return redirect('product_management')

#     return render(request, 'remove_product_confirmation.html', {'product': product})

@login_required
def remove_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_management')

def logout_view(request):
    logout(request)
    return redirect('login')

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_details.html', {'product': product})

def contact(request, product_id=None):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        user_name = request.POST.get('user_name')
        mobile_number = request.POST.get('mobile_number')

        if not user_name:
            return redirect('contact', product_id=product_id)

        product = get_object_or_404(Product, id=product_id)
        contact = Contact(product=product, user_name=user_name, mobile_number=mobile_number)
        contact.save()

        return redirect('product_details', product_id=product_id)
    else:
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'product/contact.html', {'product': product})


def custom_404(request, exception):
    return render(request, 'product/404.html', status=404)

def custom_500(request):
    return render(request, 'product/500.html', status=500)