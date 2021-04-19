from django.shortcuts import render
from django.views.generic import View
from blog.forms import PostForm


class NewsListView(View):
    def get(self, request):
        return render(request, 'blog/news/news.html', {})


class NewsAdminListView(View):
    def get(self, request):
        return render(request, 'blog/news/admin_list.html', {})


class NewsDetailView(View):
    def get(self, request):
        return render(request, 'blog/news/detail.html', {})


class NewsCreateView(View):
    def get(self, request):
        form = PostForm
        return render(request, 'blog/news/create.html', {'form': form})


class ArticleListView(View):
    def get(self, request):
        return render(request, 'blog/articles/articles.html', {})


class ArticleDetailView(View):
    def get(self, request):
        return render(request, 'blog/articles/detail.html', {})
