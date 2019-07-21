from django.urls import path
from . import views 
from .feeds import LatestPostsFeed

app_name = 'article'
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    # path('test/', views.test, name='articletest'),
    # path('article_list/', views.article_list, name='article_list'),
    path('article_detail/', views.article_detail, name='article_detail'),
]