#2°B Informatica Projeto COPAE
#Grupo estudiantes:
#Angélica Bechara
#Helinia Alexandra
#Isaque Simões

# Lógica principal
from users.administrador import Administrador
from users.usuario import Usuario
from users.pessoa import Pessoa
from users.cordenador import Coordenador
from users.membro import Membro
from atividade import Atividade
from clube import Clube
from arquivo import Arquivo
from mensagens import Mensagem
from dadosPréexistentes import dadosPréexistentes
from os import system

print("--" * 32)
print("Olá, Seja bem-vindo(a) ao nosso sistema de Organização de clubes!!!")
print("--" * 32)

bancoDeDados, clubesSistema = dadosPréexistentes()

# Lógica de cadastro
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
if user.get_nivelAcesso() == "ilimitado":
    print("Bem-vindo(a) ao menu principal, o que deseja fazer?\n[1] Cadastrar novo clube\n[2] Sair")
    print("projeto ainda não esá finalizado, infelismente!!!")
    exit()
#lógica de acesso de usuario comum
elif user.get_nivelAcesso() == "área inicial":
    print("Bem-vindo(a) ao menu principal!!!")
    print("\n[1] Visualizar clubes\n[2] Aderir a comunidade")
    resposta = input()
    if resposta == "1":
      system("clear")
      user.visualizarClubes(clubesSistema.values())
      print("Vocé deseja :\n[1] Aderir a comunidade \n[2] Sair do sistema")
      resposta = input()	
      if resposta == "1":
        system("clear")
        user_1 = user.aderirComunidade(bancoDeDados)
      elif resposta == "2":
        system("clear")
        exit()
    elif resposta == "2":
      system("clear")
      user_1 = user.aderirComunidade(bancoDeDados)

if user_1.get_nivelAcesso() == "ilimitado no clube":
  novo_clube = user_1.criar_clube()
  clubesSistema[novo_clube.get_id()] = novo_clube
  
  print("Aperte enter para prosseguir!")
  input()
  system("clear")
  while True:
    print("Bem-vindo(a) ao menu principal, o que deseja fazer?")
    print("[1] Excluir clube")
    print("[2] Adicionar membro ao clube")
    print("[3] Remover membro do clube")
    print("[4] Remover membro do clube")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      system("clear")
      clubesSistema = user_1.excluir_clube(clubesSistema)
    elif opcao == "2":
      system("clear")
      user_1.adicionar_membro(bancoDeDados.values())
    elif opcao == "3":
      system("clear")
      user_1.remover_membro()
    elif opcao == "4":
      system("clear")
      user_1.remover_membro()
    
elif user_1.get_nivelAcesso() == "limitado ao clube":
  if not clubesSistema:
      print("Nenhum clube encontrado")
      pass
  else:
      for i, clube in enumerate(clubesSistema.values(), 1):
          print(f"{i}° clube : {clube.get_nome()}\nDescrição: {clube.get_descricao()}")
      print("\nDigite a qual clube você deseja participar:")
      escolha = int(input())
      if 1 <= escolha <= len(clubesSistema.values()):
          clube_escolhido = clubesSistema.values()[escolha - 1]
      clube_escolhido.solicitar_entrada(user_1)
      print("como sistema era muito grande não conseguimos finalizar, considerando que este possui umas 2 000 linhas pedimos que considere o que está em funcionamento.")
      exit()

if user_1.get_nivelAcesso() == "ilimitado no clube":
    print("Bem-vindo(a) ao menu principal, o que deseja fazer?")
    print("[1] Criar atividade")
    print("[2] Excluir atividade")
    print("[3] ver atividades")
    print("[4] Acessar o chat")
    opcao=input()
    if opcao == "1":
      user_1.criar_atividade()
      
    elif opcao == "2":
      user_1.excluir_atividade()
      
    elif opcao == "3":
      atividades = user_1.get_clubeCordenando().get_atividades().values()
      for i, atividade in enumerate(atividades, 1):
        print(f"{i}")
        atividade.visualizar()
      print("Deseja acessar as respostas de alguma atividade?")
      print("[1] Sim\n[2] Não")
      decisao = input()
      if decisao == "1":
        print("Qual atividade deseja acessar?")
        escolha=input()
        atividade = atividades[escolha - 1]
        respostas= atividade.get_respostas()
        for resposta in respostas:
          resposta.visualizar()
      elif decisao == "2":
        pass
      
    elif opcao == "4":
      pass
  

elif user_1.get_nivelAcesso() == "limitado ao clube":
  while True:
    print("Bem-vindo(a) ao menu principal, o que deseja fazer?")
    print("[1] acessar atividades [2] acessar o chat\n")
    opcao = input()
    if opcao == "1":
      atividades = clube_escolhido.get_atividades().values()
      for i, atividade in enumerate(atividades, 1):
        print(f"{i}")
        print(atividade.get_titulo())
        print("Deseja acessar alguma atividade?")
        print("[1] Sim\n[2] Não")
        decisao = input()
      if decisao == "1":
        print("Qual atividade deseja acessar?")
        escolha=input()
        atividade = atividades[escolha - 1]
        atividade.visulizar()
        print("Menu de atividade:")
        print("[[1] enviar atividade \n[2] editar atividade\n")
        escolha=input()
        if escolha == "1":
          atividade.concluir(user_1.get_id)
          break
        elif escolha == "2":
          respostas= atividade.get_respostas()
          for resposta in respostas:
            if resposta.get_id_autor() == user_1.get_id():
              resposta.editar_envio()
            else:
              pass
      elif decisao == "2":
        break
    
    elif opcao == "2": 
      break
      
if user_1.get_nivelAcesso() == "ilimitado no clube":
  clube = user_1.get_clubeCordenando()
  chat = clube.get_chat()
  chat.exibir_mensagens()
  while True:
    print("você deseja \n[1] enviar mensagem \n[2] atualizar o chat")
    resposta=input()
    if resposta == "1":
      mensagem=user_1.enviarMensagem()
      chat.send_mensage(mensagem)
    elif resposta == "2":
      system("clear")
      chat.exibir_mensagens()
      
elif user_1.get_nivelAcesso == "limitado ao clube":
  clube = user_1.get_clubeAsssociado()
  chat = clube.get_chat()
  chat.exibir_mensagens()
  while True:
    print("você deseja \n[1] enviar mensagem \n[2] atualizar o chat")
    resposta=input()
    if resposta == "1":
      mensagem=user_1.enviarMensagem()
      chat.send_mensage(mensagem)
    elif resposta == "2":
      system("clear")
      chat.exibir_mensagens()

"""
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
"""