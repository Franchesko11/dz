from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('become-author/', views.become_author, name='become_author'),  # Здесь ошибка
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('test-providers/', views.test_providers, name='test_providers'),
]