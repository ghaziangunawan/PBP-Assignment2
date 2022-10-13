# TODO: Implement Routings Herefrom django.urls import path
from todolist.views import show_todolist, set_remove,set_status,register,login_user,logout_user,new_task,show_json,show_todolist_ajax
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', new_task, name='new_task'),
    path("set_remove/<int:id>", set_remove, name="set_remove"),
    path("set_status/<int:id>", set_status, name="set_status"),
    path('json/', show_json, name='show_json'),
    path('ajax/', show_todolist_ajax, name='show_todolist_ajax'),
]

