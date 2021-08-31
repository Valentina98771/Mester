from django.urls import path
from . import views
from .views import DeletePosts, DetailPosts, ListPosts, EditPosts

urlpatterns = [
    path('addpost/', views.CreatePosts, name = "postare"),
    path('home/', ListPosts.as_view(), name = "list"),
    path('detail/<int:pk>/', DetailPosts.as_view(), name = 'detail'),
    path('detail/edit/<int:pk>/', EditPosts.as_view(), name = 'edit'),
    path('detail/<int:pk>/delete/', DeletePosts.as_view(), name = 'delete'),

]