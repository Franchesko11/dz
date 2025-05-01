from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from .models import Post
from django.http import HttpResponse
from allauth.socialaccount.models import SocialApp


# Главная страница
def home(request):
    return render(request, 'home.html')


# Список постов
class PostListView(ListView):
    model = Post
    template_name = 'news/post_list.html'
    context_object_name = 'posts'


# Создание поста
class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'post_type']
    template_name = 'news/post_form.html'
    success_url = reverse_lazy('news:post_list')  # Добавлено пространство имён
    permission_required = 'news.add_post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Редактирование поста
class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'post_type']
    template_name = 'news/post_form.html'
    success_url = reverse_lazy('news:post_list')  # Добавлено пространство имён
    permission_required = 'news.change_post'


# Стать автором
@login_required
def become_author(request):
    authors_group, _ = Group.objects.get_or_create(name='authors')
    request.user.groups.add(authors_group)
    return redirect('/')


# Редактирование профиля
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'news/profile.html'
    success_url = reverse_lazy('news:profile')

    def get_object(self):
        return self.request.user


# Тест провайдеров для allauth
def test_providers(request):
    providers = SocialApp.objects.all()
    return HttpResponse(f"Доступные провайдеры: {[provider.provider for provider in providers]}")