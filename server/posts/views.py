from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import Post
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect

def CreatePosts(request):
    user = request.user
    body = request.POST.get("body", 'default value')
    created_on = request.POST.get("created_on", 'default value')
    updated_on = request.POST.get("updated_on", 'default value')
    post = Post.objects.create(user = user, body = body, created_on = created_on, updated_on = updated_on)
    post.save()
    return redirect('list')

class ListPosts(ListView):
    model = Post
    template_name = 'profile/profile.html'

class DetailPosts(DetailView):
    model = Post
    template_name = 'postsDetail.html'

class EditPosts(UpdateView):
    model = Post
    template_name = 'postsEdit.html'
    fields = ['body',]

class DeletePosts(DeleteView):
    model = Post
    template_name = 'postsDelete.html'
    success_url = reverse_lazy('list')
