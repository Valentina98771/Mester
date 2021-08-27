from django.urls import path
from . import views
from .views import PostsDelete, PostsEdit, PostsView, PostsDetail

app_name = 'posts'

urlpatterns = [
    path('addpost/', views.PostsAddView, name = "postare"),
    path('', PostsView.as_view(), name = "list"),
    path('detail/<int:pk>/', PostsDetail.as_view(), name = 'detail'),
    path('detail/edit/<int:pk>/', PostsEdit.as_view(), name = 'edit'),
    path('detail/<int:pk>/delete/', PostsDelete.as_view(), name = 'delete'),

]