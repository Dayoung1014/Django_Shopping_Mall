from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),    # 서버IP/
    path('company_page/', views.company_page)   # 서버IP/about_me
]