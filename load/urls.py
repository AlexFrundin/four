from django.urls import path
from . import views

urlpatterns=[
    path('country', views.load_country_csv, name='load_country'),
    path('city', views.load_city, name="load_city"),
    path('newcity', views.load_city_new, name="new_city"),
    path('duplicate', views.duplicate, name='duplicate'),
    path('unique_city', views.unique_city, name='unique_city'),
]
