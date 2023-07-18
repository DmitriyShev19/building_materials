from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from forumify.forms import CommentForm
from forumify.models import Category, Topic, Post, Comment


def category_list(request):
    categories = Category.objects.all()
    context = {
               'categories': categories
    }
    return render(request, 'forumify/category_list.html', context=context)


class TopicListView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        topics = Topic.objects.filter(category=category)
        context = {
            'category': category,
            'topics': topics
        }
        return render(request, 'forumify/topic_list.html', context)


class PostListView(View):
    def get(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)
        posts = Post.objects.filter(topic_id=topic.pk).all()
        context = {
            'topic': topic,
            'posts': posts
        }
        print(posts)
        return render(request, 'forumify/post_list.html', context=context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    topic = get_object_or_404(Topic, id=post.topic.pk)
    comments = Comment.objects.filter(post=post.pk).all()
    context = {
        'topic': topic,
        'post': post,
        'comments': comments
    }
    return render(request, 'forumify/post.html', context=context)


class AddCommentView(View):
    def post(self, request, post_id):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = get_object_or_404(Post, id=post_id)
            comment.save()
            return redirect('post_detail', post_id=post_id)

