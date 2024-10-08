from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('post/<int:post_id>/comment/new/', views.comment_add, name='comment_add'),
]
