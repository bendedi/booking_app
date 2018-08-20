from django.urls import re_path
from . import views

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	re_path(r'send/', views.send, name='send'),
	re_path(r'^model/', views.model, name='model'),
	re_path(r'^gettoken/', views.gettoken, name='gettoken'),
	re_path(r'^mail/', views.mail, name='mail')
]
