from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .models import Post
from .forms import PostForm,ReplyForm


# Create your views here.

def index(request):
    posts = Post.objects.order_by('-create_at');
    return render(request, 'index.html', {'posts': posts})


@login_required
def create(request):
    params = request.POST if request.method == 'POST' else None
    form = PostForm(params)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.info(request, 'Post `{}` created successfully!'.format(post.title))
        form = PostForm()

    return render(request, 'create.html', {'form': form})


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = ReplyForm()
    return render(request, 'post.html', {'post':post,'reply_form':form})


@login_required
@require_POST
def reply(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.author = request.user
        reply.post = post
        print(reply.save())
        messages.info(request, 'Post `{}` replied successfully!'.format(post.title))
    else:
        print('not valid')
        messages.warning(request, 'Post `{}` replied failed')

    return redirect('post', post.id)
