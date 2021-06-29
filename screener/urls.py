from django.urls import path
from screener import views

urlpatterns = [
    path('', views.index,name='home'),
    path('news',views.news,name='news'),
    path('blogs',views.blogs,name='blogs'),
    path('test',views.test,name='test'),
    path('test2',views.test2,name='test2'),
    path('test3/<int:blog_id>',views.test3,name='test3'),
]