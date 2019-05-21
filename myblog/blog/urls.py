from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = \
    [
        path('', views.home, name="home"),
        path('posts', views.posts, name='posts')
        # path('category', views.category, name='category'),
        # path('category/<int:category_id>', views.category_id, name='category_id'),
        # path('posts/<int:posts_id>/members', views.posts_id, name='posts_id')
    ]
