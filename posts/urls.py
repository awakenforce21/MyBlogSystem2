
from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('list/', views.p_list, name = 'list'),
    path('create/', views.p_create, name = 'create'),
    path('<int:post_id>/update', views.p_update, name = 'update'),
    path('<int:post_id>/delete', views.p_delete, name = 'delete'),
    path('<int:post_id>/', views.p_detail, name = 'p_detail'),
    path('<int:post_id>/comment/', views.add_comment_to_post, name = 'add_comment_to_post'),
    path('<int:comment_id>/c_update', views.c_update, name = 'update_comment'),
    path('<int:comment_id>/c_delete', views.c_delete, name = 'delete_comment'),
    path('<int:comment_id>/c_detail', views.c_detail, name = 'c_detail')

]