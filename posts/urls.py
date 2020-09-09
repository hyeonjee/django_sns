from django.urls import path
from .views import *

app_name = "posts"
urlpatterns = [
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name="delete"),

    #comments
    path('<int:post_id>/create_comment/', create_comment, name="create_comment"),
    path('<int:comment_id>/delete_comment/', delete_comment, name="delete_comment"),

    #likes
    path('<int:post_id>/post_like/', post_like, name="post_like"),
    path('like_list/', like_list, name="like_list"),
]