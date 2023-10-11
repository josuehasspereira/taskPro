from django.shortcuts import render, redirect
from .models import Tarefa


# request permite acessar os dados dentro da página
# render: renderiza uma pagina e passa os dados (request) e uma pagina html para mostrar os dados
def home(request):
    return render(request, 'tarefas/home.html')


def tarefas(request):

    if request.method == 'POST':   
        nova_tarefa = Tarefa()
        nova_tarefa.nome = request.POST.get('nome')
        nova_tarefa.tarefa = request.POST.get('tarefa')
        nova_tarefa.save()
        # Redireciona para a página de tarefas após o envio do formulário
        return redirect('listagem_tarefas')

    tarefas = {
        'tarefas': Tarefa.objects.all()
    }


    return render(request, 'tarefas/tarefas.html', tarefas)