from django.urls import path
from core import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('articles/', views.ArticleView.as_view(), name='articles'),
    path('articles/<int:pk>', views.SingleArticleView.as_view()),
    path('authors/', views.AuthorView.as_view(), name='articles'),
    path('authors/<int:pk>', views.SingleAuthorView.as_view()),
]