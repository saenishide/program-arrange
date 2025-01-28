from django.urls import path
from flowchart import views

app_name = 'flowchart'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.get_flowchart, name='index'),
]