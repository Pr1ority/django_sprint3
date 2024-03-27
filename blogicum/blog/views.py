from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category


def get_published_posts(posts):
    return posts.filter(is_published=True,
                        pub_date__lte=timezone.now(),
                        category__is_published=True)


def index(request):
    template_name = 'blog/index.html'
    all_posts = Post.objects.all()
    post_list = get_published_posts(all_posts)[:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(get_published_posts(Post.objects.all()),
                             pk=post_id)
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    all_posts = Post.objects.filter(category=category)
    post_list = get_published_posts(all_posts)
    context = {'category': category, 'post_list': post_list}
    return render(request, template_name, context)
