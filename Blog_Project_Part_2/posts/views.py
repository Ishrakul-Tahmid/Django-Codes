from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save(commit=True)
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
    return render(request, 'create_post.html', {'form': post_form})

@login_required
def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post) # instance=post is used so that uesr not change the post it not create problem
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save(commit=True)
            return redirect('homepage')
        
    return render(request, 'create_post.html', {'form': post_form})

@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')