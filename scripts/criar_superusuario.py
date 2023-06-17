from django.contrib.auth.models import User
import secrets
import string


def gerar_senha():
    # Gera uma senha aleatória com 8 caracteres
    alfabeto = string.ascii_letters + string.digits
    senha = ''.join(secrets.choice(alfabeto) for i in range(8))
    return senha


def run():
    """
    Executará um script para criar um super usuário e
    informará os dados de acesso
    """

    print("Você está prestes a criar um super usuário.")
    usuario = input("Digite o nome do usuário: ")
    while User.objects.filter(username=usuario).exists():
        print("Usuário já existe. Tente novamente.")
        usuario = input("Digite o nome do usuário: ")
    senha = gerar_senha()
    try:
        User.objects.create_superuser(usuario, '', senha)
        print(
            "Usuário criado com sucesso. \n "
            "Acesse http://localhost:8000/admin/ \n "
            "Utilize o usuário: {} e senha: {}".format(
                usuario, senha))
    except Exception as e:
        print("Erro ao criar usuário: {}".format(e))
    finally:
        print("Fim do script.")
