from django.urls import path
from . import views
from .views import DeletePost, DetailPost, ListPost, EditPost, ListPt

urlpatterns = [
    path('addpost/', views.CreatePost, name = "postare"),
    path('home/', ListPost.as_view(), name = "list"),
    path('test/', ListPt.as_view(), name = "list1"),

    path('detail/<int:pk>/', DetailPost.as_view(), name = 'detail'),
    path('detail/edit/<int:pk>/', EditPost.as_view(), name = 'edit'),
    path('detail/<int:pk>/delete/', DeletePost.as_view(), name = 'delete'),
]