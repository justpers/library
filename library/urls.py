from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),  # 책 목록
    path('books/<int:book_id>/history/', views.book_history, name='book_history'),  # 대출 이력
]