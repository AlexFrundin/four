from django.urls import path
from . import views
urlpatterns = [
    path('', views.book_gt, name='book_gt'),
    path('detail/', views.book_detail, name='book_detail')
]
