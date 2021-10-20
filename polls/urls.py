from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
##polls에 urls.py는 추가로 넣은 것