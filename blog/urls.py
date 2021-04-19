from django.urls import path
from .views import *

app_name='blog'

urlpatterns = [
	path ('news', NewsListView.as_view(), name='news'),
	path ('news_admin', NewsAdminListView.as_view(), name='news_admin'),
	path ('news_create', NewsCreateView.as_view(), name='news_create'),
	path ('news_detail', NewsDetailView.as_view(), name='news_detail'),
	path ('article', ArticleListView.as_view(), name='article'),
	path ('article_detail', ArticleDetailView.as_view(), name='article_detail'),
]