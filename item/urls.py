from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemList.as_view()), #서버 IP/item
    path('<int:pk>/', views.ItemDetail.as_view()),
    path('search/<str:q>/', views.ItemSearch.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('register_item/', views.ItemCreate.as_view()),
    path('update_item/<int:pk>/', views.ItemUpdate.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('company/<str:company_name>/', views.company_page),
    path('<int:pk>/list/like/', views.likes_list),
    path('<int:pk>/detail/like/', views.likes_detail),
]