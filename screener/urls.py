from django.urls import path
from screener import views

urlpatterns = [
    path('', views.index,name='home'),
    path('news',views.news,name='news'),
    path('blogs/',views.blogs,name='blogs'),
    path('blogs/<str:slug>',views.view_blog,name='view_blog'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/blog/create',views.new_blog,name='new_blog'),
    path('dashboard/blog/edit/<int:blog_id>',views.edit_blog,name='edit_blog'),
    path('dashboard/blog/<int:blog_id>/delete',views.delete_blog,name='delete_blog'),
]