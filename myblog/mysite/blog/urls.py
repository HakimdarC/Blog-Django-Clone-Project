from django.urls import path
from . import views
from .views import PostUpdateView,PostListView,PostDeleteView,AboutView,PostDetailView,CreatePostView,DraftListView
#app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/<pk>/detail/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', CreatePostView.as_view(), name='post_new'),
    path('post/<pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<pk>/remove/', PostDeleteView.as_view(), name='post_remove'),
    path('draft/', DraftListView.as_view(), name='post_draft_list'),
    path('post/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk>/approve/', views.approve_comment, name='approve_comment'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),



]