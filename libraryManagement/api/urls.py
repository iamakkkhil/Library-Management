from django.urls import path 
from . import views 

urlpatterns = [
    path('getBooks/', views.get_books, name="GetBooks"),
    path('getBooks/<str:id>/', views.get_book, name="GetBook"),
]