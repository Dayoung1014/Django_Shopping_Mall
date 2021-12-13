from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemList.as_view()), #서버 IP/item
    path('<int:pk>/', views.ItemDetail.as_view()),
]