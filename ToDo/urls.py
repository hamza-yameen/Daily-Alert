from django.urls import path
from .views import home, addtodo, delete

app_name = 'ToDo'

urlpatterns = [
    path('', home, name='home'),
    path('addtodo/', addtodo, name='addtodo'),
    path('del/<int:iditem>/', delete, name='delitem'),
]