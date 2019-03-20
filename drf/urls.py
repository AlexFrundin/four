from django.urls import path
from . import views
urlpatterns = [
    path('',views.drf_form,name='drf_form'),
    path('all', views.item_all, name='item_all'),
    path('detail/<int:id>', views.item_detail, name='item_detail'),
    path('create',views.item_create, name='item_create'),
    path('delete/<int:id>', views.item_delete, name='item_delete'),
    path('update/<int:id>', views.item_update, name='item_update'),

]
