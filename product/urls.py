from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 
    path('', views.home,name='home'),
    path('add_product', views.add_product,name='add_product'),
    path('remove-product/<int:product_id>/', views.remove_product, name='remove_product'),  # Remove product functionality
    path('product-management/', views.product_management, name='product_management'),  # Product management page
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('contact/<int:product_id>/', views.contact, name='contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'product.views.custom_404'
handler500 = 'product.views.custom_500'