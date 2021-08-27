from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Post
from django.views.generic import ListView, UpdateView, DeleteView
from django.shortcuts import render, redirect


def PostsAddView(request):
    if request.method=='POST':
        user = request.user
        body = request.POST.get("body", 'default value')
        created_on = request.POST.get("created_on", 'default value')
        updated_on = request.POST.get("updated_on", 'default value')
        post = Post.objects.create(user = user, body = body, created_on = created_on, updated_on = updated_on)
        post.save()
        return redirect('posts:list')
    else:
        return render(request, 'postsList.html', {})

class PostsView(ListView):
    model = Post
    template_name = 'postsList.html'

class PostsDetail(DetailView):
    model = Post
    template_name = 'postsDetail.html'

class PostsEdit(UpdateView):
    model = Post
    template_name = 'postsEdit.html'
    fields = ['body',]

class PostsDelete(DeleteView):
    model = Post
    template_name = 'postsDelete.html'
    success_url = reverse_lazy('posts:list')
