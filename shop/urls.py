from django.urls import path, re_path
from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),  # пример URL-адреса без параметров
    path('<category_slug>/', views.product_list, name='product_list_by_category'),  # пример URL-адреса с параметром
    path('<id>/<slug>/', views.product_detail, name='product_detail'),  # URL-адрес для детализации продукта
]