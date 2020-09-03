from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm


def p_list(request):
    my_list = Post.objects.all().order_by('-id')
    context = {'posts': my_list}
    return render(request, 'list.html', context)

def p_create(request):
    # POST 방식으로 호출될 때
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
        # GET 방식으로 호출될 때
    else:
        post_form = PostForm()

    return render(request, 'create.html', {'post_form': post_form})

def p_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('posts:list')

def p_update(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    # POST 방식으로 호출될 떄
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    # GET 방식으로 호출될 때
    else:
        post_form = PostForm(instance=post)

    return render(request, 'create.html', {'post_form': post_form})

def p_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'p_detail.html', {'post':post})

def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        comment = Comment(post=post)
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            path = '/posts/{}/'.format(post_id)
            return redirect(path)

    else:
        comment_form = CommentForm()
        return render(request, 'add_comment_to_post.html', {'comment_form':comment_form})

def c_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    post = Post.objects.get(id=comment.post_id)

    return render(request, 'p_detail.html', {'post':post})

def c_update(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    post = Post.objects.get(id=comment.post_id)

    # POST 방식으로 호출될 떄
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            return render(request, 'p_detail.html', {'post':post})

    # GET 방식으로 호출될 때
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'c_update.html', {'comment_form': comment_form})

def c_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'c_detail.html', {'comment':comment})


