from django.urls import path, include
from .views import index, blog_post, BlogIndexView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

urlpatterns = [
    path('', BlogIndexView.as_view(), name="blog-index"),
    path('create/', BlogPostCreateView.as_view(), name="blog-post-create"),
    path('<str:slug>/', BlogPostDetailView.as_view(), name="blog-post-detail"),
    path('<str:slug>/edit/', BlogPostUpdateView.as_view(), name="blog-post-edit"),
path('<str:slug>/delete/', BlogPostDeleteView.as_view(), name="blog-post-delete"),
]