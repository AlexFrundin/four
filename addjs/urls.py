from django.urls import path
from . import views
urlpatterns = [
    path('', views.add_js, name='add_js'),
    path('ajax', views.ajax_js, name='ajax_js'),
]
