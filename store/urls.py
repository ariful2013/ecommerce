from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<int:id>-<slug:slug>/',
         views.detail_product, name='detail_product'),
    path('search/<slug:category_slug>/',
         views.category_list, name='category_list'),
]
