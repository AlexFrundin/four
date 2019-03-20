from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='index'),
    path('detail/<int:pk>', views.detail, name='detail')
]
