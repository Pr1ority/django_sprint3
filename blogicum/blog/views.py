from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category


def get_published_posts():
    return Post.objects.filter(is_published=True, pub_date__lte=timezone.now())


def index(request):
    template_name = 'blog/index.html'
    post_list = get_published_posts()[:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(get_published_posts(), pk=id)
    if not post.category.is_published:
        raise Http404("Публикация не найдена")
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    post_list = get_published_posts().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, template_name, context)
