from django.urls import path
from . import views
'''
urlpatterns = [
    path('alunos', views.lista_alunos, name='lista_alunos'),
    path('', views.adiciona_aluno, name='adiciona_aluno'),
]

'''
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('alunos', views.lista_alunos, name='lista_alunos'),
    path('', views.adiciona_aluno, name='adiciona_aluno'),
    path('sucesso/', views.adiciona_aluno_sucesso, name='adiciona_aluno_sucesso'),
]
