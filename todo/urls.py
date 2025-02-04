from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
    path('todos/add', views.add_todo, name='add_todo'),
    path('todos/<int:pk>/edit/', views.edit_todo, name='edit_todo'),
    path('todos/<int:pk>/delete/', views.delete_todo, name='delete_todo'),
]
