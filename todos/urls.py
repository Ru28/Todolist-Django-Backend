from django.urls import path
from . import views

urlpatterns = [
    path("todos", views.todo_list),
    path("todos/<int:todo_id>",views.todo_detail)
]

# urls:
   # http://127.0.0.1:8000/todos
   # http://127.0.0.1:8000/todos/id