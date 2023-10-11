
from django.urls import path
from app_taskPro import views

urlpatterns = [
    # rota, view, nome de referência
    # tarefas.com
    # vai chamar a funcao home importada da view
    path('', views.home, name='home'),
    path('tarefas/', views.tarefas, name='listagem_tarefas')
]
 