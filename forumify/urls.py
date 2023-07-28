from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('category/<int:category_id>',
         TopicListView.as_view(),
         name='topic_list'),
    path('topic/<int:topic_id>/', PostListView.as_view(), name='topic_detail'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/addcomment/<int:post_id>', AddCommentView.as_view(), name='add_comment'),
    path('feedback/', feedback, name='feedback'),
    path('feedback/success/', feedback_success, name='feedback_success'),
]