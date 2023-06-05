from django.shortcuts import render, get_object_or_404
from django.views import View

from forumify.models import Category, Topic


def category_list(request):
    categories = Category.objects.all()
    context = {
               'categories': categories
    }
    return render(request, 'forumify/category_list.html', context=context)


class TopicListView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        topics = Topic.objects.filter(category=category)
        context = {
            'category': category,
            'topics': topics
        }
        return render(request, 'forumify/topic_list.html', context)

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.post_set.all()
    context = {
        'topic': topic,
        'posts': posts
    }
    return render(request, 'forumify/topic_detail.html', context=context)
