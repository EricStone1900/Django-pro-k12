from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from django.db.models import Count
from taggit.models import Tag
from .forms import CommentForm

def article_detail(request):
  return render(request,'arttest/article_detail.html')

# def test(request, tag_slug=None):
#     object_list = Post.published.all()
#     latest_posts = Post.published.order_by('-publish')[:4]
#     tag = None

#     if tag_slug:
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         object_list = object_list.filter(tags__in=[tag])

#     paginator = Paginator(object_list, 3) # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)

#     return render(request,
#                   'arttest/arttest.html',
#                   {'page': page,
#                    'posts': posts,
#                    'tag': tag,
#                    'latest_posts': latest_posts})

# def article_list(request):
#   article_list = Post.published.all()
#   paginator = Paginator(article_list, 2)
#   page = request.GET.get('page')
#   try:
#     articles = paginator.page(page)
#   except PageNotAnInteger:
#     articles = paginator.page(1)
#   except EmptyPage:
#     articles = paginator.page(paginator.num_pages)
#   return render(request,'arttest/aritcle_list.html',{'article_list': articles})


# Create your views here.
def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    latest_posts = Post.published.order_by('-publish')[:4]
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'article/post/list.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag,
                   'latest_posts': latest_posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]

    return render(request,
                  'article/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts': similar_posts})
