from django.shortcuts import render
from.models import Usuario


def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #exibir users cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #Retorna os dados para a página de listagem de usuários
    return render(request,'usuarios/usuarios.html',usuarios)
    
    