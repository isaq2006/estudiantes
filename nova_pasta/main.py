from classes import *
from os import system
 
#angeçlica bjs
 
print("--" * 32)
print("Olá, Seja bem-vindo(a) ao nosso sistema de Organização de clubes!!!")
print("--" * 32)

bancoDeDados = {}

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
                administrador1 = Administrador()
                administrador1.set_cadastro(bancoDeDados)
                system("clear")
                bancoDeDados[administrador1.get_id()] = administrador1
                processo = True
                break
            elif opcao2 == "2":
                while not processo:
                    print("Você deseja se cadastrar como:\n[1] Coordenador\n[2] Membro\nou apenas visualizar a tela inicial como um usuário comum?\n[3] Usuário")
                    opcao3 = input()
                    system("clear")

                    if opcao3 == "1":
                        coordenador1 = Coordenador()
                        coordenador1.set_cadastro(bancoDeDados)
                        system("clear")
                        bancoDeDados[coordenador1.get_id()] = coordenador1
                        processo = True
                        break
                    elif opcao3 == "2":
                        membro1 = Membro()
                        membro1.set_cadastro(bancoDeDados)
                        system("clear")
                        bancoDeDados[membro1.get_id()] = membro1
                        processo = True
                        break
                    elif opcao3 == "3":
                        usuario1 = Usuario()
                        usuario1.set_cadastro(bancoDeDados)
                        system("clear")
                        bancoDeDados[usuario1.get_id()] = usuario1
                        processo = True
                        break
                    else:
                        print("Opção inválida")
            else:
                print("Opção inválida")

    elif opcao == "2":
        resultado = Pessoa.get_login(bancoDeDados)
        if resultado:
            processo = True
        else:
            continue
    else:
        print("Opção inválida")

    while True:
        print("Deseja repetir esse processo?\n[1] Sim\n[2] Não")
        decisao5 = input()
        if decisao5 == "1":
            system("clear")
            processo = False
            break
        elif decisao5 == "2":
            system("clear")
            processo = True
            break
        else:
            print("Opção inválida! Aperte ENTER")
            input()
            system("clear")

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

system("clear")
for pessoa in bancoDeDados.values():
    print(f"Esse é {pessoa.get_nome()}, e esses são seus dados=")
    pessoa.get_imprimirDados()
    print("\n\n")
