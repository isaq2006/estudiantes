# Lógica principal
from users.administrador import Administrador
from users.usuario import Usuario
from users.pessoa import Pessoa
from users.cordenador import Coordenador
from users.membro import Membro
from atividade import Atividade
from clube import Clube
from arquivo import Arquivo
from os import system

print("--" * 32)
print("Olá, Seja bem-vindo(a) ao nosso sistema de Organização de clubes!!!")
print("--" * 32)

bancoDeDados = {}
clubesSistema = {}

# Lógica de cadastro
user=None
processo = False
while not processo:
    print("Você deseja realizar:\n[1] Cadastro\n[2] Login")
    opcao = input()
    system("clear")

    if opcao == "1":
        while not processo:
            print("Você deseja se cadastrar como:\n[1] Administrador\n[2] Usuário")
            opcao2 = input()
            system("clear")

            if opcao2 == "1":
                user = Administrador()
                user.set_cadastro(bancoDeDados)
                system("clear")
                bancoDeDados[user.get_id()] = user
                processo = True
                break
            elif opcao2 == "2":
                user = Usuario()
                user.set_cadastro(bancoDeDados)
                system("clear") 
                bancoDeDados[user.get_id()] = user
                processo = True
                break
            else:
                print("Opção inválida")
                processo  = False
                
    elif opcao == "2":
        resultado = Pessoa.get_login(bancoDeDados)
        if resultado:
            processo = True
        else:
            continue
    else:
        print("Opção inválida")

#lógica de acesso de administrador
if user.get_nivelAcesso == "ilimitado":
  while True:
    print("Bem-vindo(a) ao menu principal, o que deseja fazer?\n[1] Cadastrar novo clube\n[2] Sair")

#lógica de acesso de usuario comum
elif user.get_nivelAcesso == "área inicial":
  while True:
    print("Bem-vindo(a) ao menu principal!!!")
    print("\n[1] Visualizar clubes\n[2]Aderir a comunidade")
    resposta = input()
    if resposta == "1":
      user.visualizarClubes(clubesSistema.values())
      
    elif resposta == "2":
      user.aderirComunidade(bancoDeDados,clubesSistema.values())
  
    else:
      print("Opção inválida")


acao=False
while acao==False:
  while True: 
    print("você deseja alterar algum dado do seu cadastro?\n[1] Sim\n[2] Não")
    decisao6 = input()
    system("clear")
    if decisao6 == "1":
      while True:
        print("Insira seu id")
        id = input()
        if id in bancoDeDados:
          pessoa = bancoDeDados.get(id)
          if pessoa is not None:
            pessoa.set_atualizarDados(bancoDeDados)
          break
        else:
          print("usuario não encontrado")
          continue
      break
    elif decisao6 == "2":
      break
    else:
      print("opção invalida, aperte enter!")
      input()
      system("clear")
      continue
  while True:
      print(f"você deseja alterar outro dado?\n[1] Sim\n[2] Não")
      decisao7 = input()
      if decisao7 == "1":
        system("clear")
        acao=False
        break
      elif decisao7 == "2":
        system("clear")
        acao=True
        break
      else:
        print("opção invalida, aperte enter!")
        input()
        system("clear")

