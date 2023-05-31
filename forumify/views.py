from django.shortcuts import render, get_object_or_404

from forumify.models import Category, Topic


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'forumify/category_list.html', {'categories': categories})


def topic_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = category.topic_set.all()
    return render(request, 'forumify/topic_list.html', {'category': category, 'topics': topics})


def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.post_set.all()
    return render(request, 'forumify/topic_detail.html', {'topic': topic, 'posts': posts})
