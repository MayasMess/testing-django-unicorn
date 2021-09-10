from django.urls import path

from .views import TodoBaseTemplate

urlpatterns = [
    path("", TodoBaseTemplate.as_view(), name="todo-index"),
]
