from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def adiciona_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adiciona_aluno_sucesso')
    else:
        form = AlunoForm()
    return render(request, 'adiciona_aluno.html', {'form': form})


def adiciona_aluno_sucesso(request):
    return render(request, 'sucesso.html')
