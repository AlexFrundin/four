from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('site_form', views.get_form, name="get_f"),
    path('form_st', views.get_form_st,name="get_st"),
    path("accept_html", views.accept, name="accept_name"),
    path('m_form', views.get_form_model, name="f_model"),
]
