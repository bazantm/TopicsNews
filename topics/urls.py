from django.urls import path, include
from . import views

urlpatterns = [
    path('topics/', views.topics, name='topics'),
    path('topic/<str:pk_test>', views.topic_detail, name='topic'),
    path('news/', views.news, name='news'),
]
