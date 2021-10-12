from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import Post
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect

def CreatePost(request):
    if request.method == "POST":
        user = request.user
        body = request.POST.get("body", 'default value')
        created_on = request.POST.get("created_on", 'default value')
        updated_on = request.POST.get("updated_on", 'default value')
        post = Post.objects.create(user = user, body = body, created_on = created_on, updated_on = updated_on)
        post.save()
        return redirect('list')
    else:
        return render(request, "clientProfile/profile/about.html", {})

class ListPost(ListView):
    model = Post
    template_name = 'clientProfile/profile/about.html'

class DetailPost(DetailView):
    model = Post
    template_name = 'postsDetail.html'

class EditPost(UpdateView):
    model = Post
    template_name = 'postsEdit.html'
    fields = ['body',]

class DeletePost(DeleteView):
    model = Post
    template_name = 'postsDelete.html'
    success_url = reverse_lazy('list')
