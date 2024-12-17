#2°B Informatica Projeto COPAE
#Grupo estudiantes:
#Angélica Bechara
#Helynia Alexandra
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
from time import sleep

class AlternativaInvalida(Exception):
    #Exceção para alternativas inválidas.
    def __init__(self, alternativa):
        super().__init__(f"Alternativa '{alternativa}' escolhida é inválida!")
        
bancoDeDados, clubesSistema = dadosPréexistentes()

while True:
  
  print("--" * 32)
  print("Olá, Seja bem-vindo(a) ao nosso sistema de Organização de clubes!!!")
  print("--" * 32)

  # Lógica de cadastro
  processoA = False
  while not processoA:
    try:
      print("Você deseja realizar:\n[1] Cadastro\n[2] Login")
      opcao = input()
      system("clear")

      if opcao == "1":
          while not processoA:
            try:
              print("Você deseja se cadastrar como:\n[1] Administrador\n[2] Usuário")
              opcao2 = input()
              system("clear")
              if opcao2 == "1":
                  user = Administrador()
                  user.set_cadastro(bancoDeDados)
                  system("clear")
                  bancoDeDados[user.get_id()] = user
                  processoA = True
                  break
              elif opcao2 == "2":
                  user = Usuario()
                  user.set_cadastro(bancoDeDados)
                  system("clear") 
                  bancoDeDados[user.get_id()] = user
                  processoA = True
                  break
              else:
                  raise AlternativaInvalida(opcao2)
            except AlternativaInvalida as e:
              print(e)
            else:
              print("cadastrado com sucesso!!!") 
            finally:
              sleep(2)
              system("clear") 
                  
      elif opcao == "2":
          resultado = Pessoa.get_login(bancoDeDados)
          if resultado:
              processoA = True
          else:
              continue
      else:
          raise AlternativaInvalida(opcao)

    except AlternativaInvalida as e:
      print(e)
    else:
      print("Acesso permitido!!!")
    finally:
      sleep(2)
      system("clear")

  processoB1 = False
  #lógica de acesso de administrador
  if user.get_nivelAcesso() == "ilimitado":
    while not processoB1:
      try:
        print("Bem-vindo(a) ao menu principal!!!")
        print("[1] remover clubes\n[2] remover usuarios\n[3] voltar a entrada principal")
        resposta = input()
        if resposta == "1":
          system("clear")
          clubesSistema = user.removerClube(clubesSistema)
        elif resposta == "2":
          system("clear")
          bancoDeDados = user.removerUsuario(bancoDeDados)
        elif resposta == "3":
          system("clear")
          processoB1 = True
          processoA = False
        else:
          raise AlternativaInvalida(resposta)
      except AlternativaInvalida as e:
        print(e)
      else:
        print("Processando...")
      finally:
        sleep(2)
        system("clear")
      
  
  #lógica de acesso de usuario comum a tela principal
  if user.get_nivelAcesso() == "área inicial":
      processoB = False

      print("Bem-vindo(a) ao menu principal!!!")
      while not processoB:
        try:
          print("\n[1] Visualizar clubes\n[2] Aderir a comunidade\n[3] Sair")
          resposta = input()
          if resposta == "1":
            user.visualizarClubes(clubesSistema)
            print("Aperte enter para voltar ao menu...")
            resposta = input()	
            
          elif resposta == "2":
            system("clear")
            user_1 = user.aderirComunidade(bancoDeDados, clubesSistema)
            processoB = True
          elif resposta == "3":
            system("clear")
            exit()
          else:
            raise AlternativaInvalida(resposta)
        except AlternativaInvalida as e:
          print(e)
        else:
          print("Processando...")
        finally:
          sleep(2)
          system("clear")
          
  processo = False
  #lógica de acesso de coordenador ao clube
  if user_1.get_nivelAcesso() == "ilimitado no clube":
    novo_clube = user_1.criar_clube()
    clubesSistema.append(novo_clube)
    print("Aperte enter para prosseguir!")
    input()
    system("clear")
    while not processo:
      try: 
        print("Bem-vindo(a) ao menu principal, o que deseja fazer?")
        print("[1] Configurar clube (adicionar ou remover membros)")
        print("[2] Acessar aba de interação")
        print("[3] voltar a entrada principal")
        print("[4] Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
          processo1 = False
          while not processo1:
            try:
              print("Menu de configuração, o que deseja fazer?")
              print("[1] Excluir clube")
              print("[2] Adicionar membro ao clube")
              print("[3] Remover membro do clube")
              print("[4] Voltar ao menu principal")

              opcao = input()

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
                print ("Voltando ao menu principal...")
                processo1 = True
              else:
                raise AlternativaInvalida(opcao)
            except AlternativaInvalida as e:
              print(e)
            else:
              print("voltando ao menu...")
            finally:
              sleep(2)
              system("clear")
              
        elif opcao == "2":
          processo2 = False
          while not processo2:
            try:
              print("Aba de interação, o que deseja fazer?")
              print("[1] Criar atividade")
              print("[2] Excluir atividade")
              print("[3] ver atividades")
              print("[4] Acessar o chat")
              print("[5] Voltar ao menu principal")
              opcao=input()
              if opcao == "1":
                user_1.criar_atividade()
                
              elif opcao == "2":
                user_1.excluir_atividade()
                
              elif opcao == "3":
                atividades = user_1.get_clubeCordenando().get_atividades()
                if not  atividades:
                  print("Nao existem atividades cadastradas")
                  print("Aperte enter para voltar ao menu...")
                  input()
                  system("clear")
                else:
                  for i, atividade in enumerate(atividades, 1):
                    print(f"{i}° Atividade:")
                    atividade.visualizar()
                  while True:
                    try:
                      print("Deseja acessar as respostas de alguma atividade?")
                      print("[1] Sim\n[2] Não")
                      decisao = input()
                      if decisao == "1":
                        print("Qual atividade deseja acessar?")
                        escolha=input()
                        atividade = atividades[int(escolha) - 1]
                        atividade.visualizar_respostas()
                        print("\nAperte enter para voltar ao menu...")
                        input()
                      elif decisao == "2":
                        pass
                      else:
                        raise AlternativaInvalida(decisao)
                    except AlternativaInvalida as e:
                      print(e)
                    else:
                      break
                    finally:
                      sleep(2)
                      system("clear")  
                  
              elif opcao == "4":
                clube = user_1.get_clubeCordenando()
                chat = clube.get_chat()
                chat.exibir_mensagens()
                conversa = False
                while not conversa:
                  try:
                    print("você deseja:\n[1] enviar mensagem \n[2] atualizar o chat\n[3] voltar ao menu principal")
                    resposta=input()
                    if resposta == "1":
                      mensagem=user_1.enviarMensagem()
                      chat.send_mensage(mensagem)
                    elif resposta == "2":
                      system("clear")
                      chat.exibir_mensagens()
                    elif resposta == "3":
                      conversa = True
                    else:
                      raise AlternativaInvalida(resposta)
                  except AlternativaInvalida as e:
                    print(e)
                  else:
                    print("aperte enter!!!")
                    input ()
                  finally:
                    sleep(2)
                    system("clear")
                
              elif opcao == "5":
                print ("Voltando ao menu principal...")
                processo2 = True
              else:
                raise AlternativaInvalida(opcao)
            except AlternativaInvalida as e:
              print(e)
            else:
              print("voltando ao menu...")
            finally:
              sleep(2)
              system("clear")
        elif opcao == "3":
          processo = True
          processoA = False
        elif opcao == "4":
          exit()
        else:
          raise AlternativaInvalida(opcao)
        
      except AlternativaInvalida as e:
        print(e)
      else: 
        print("processo em execução...")
      finally:
        sleep(2)
        system("clear")

  processo = False
  #logica para acessar o clube como um membro
  if user_1.get_nivelAcesso() == "limitado ao clube":
    user_1.visualizarClubes(clubesSistema)
    while True:
      try:
        print("\nDigite o número do clube que você deseja participar:")
        escolha = int(input())
        if 1 <= escolha <= len(clubesSistema):
            clube_escolhido = clubesSistema[escolha - 1]
            clube_escolhido.solicitar_entrada(user_1)
            print("Aperte enter para prosseguir...")
            input()
        else:
            raise AlternativaInvalida(escolha)
      except AlternativaInvalida as e:
        print(e)
      else:
        break
      finally:
        sleep(2)
        system("clear")
    
    while not processo:
      try:
        print("Bem-vindo(a) ao menu principal, o que deseja fazer?")
        print("[1] acessar atividades \n[2] acessar o chat\n[3] voltar a entrada principal\n[4] Sair")
        opcao = input()
        if opcao == "1":
          processo1 = False
          while not processo1:
            try:
              print("Menu de atividades:")
              print("[1] ver atividades \n[2] enviar/editar envio de atividade\n[3] voltar ao menu principal")
              decisao = input()
              if decisao == "1":	
                atividades = clube_escolhido.get_atividades()
                for i, atividade in enumerate(atividades, 1):
                  print(f"{i}°")
                  atividade.visualizar()
                  
                print("\nAperte enter para voltar ao menu...")
                input()
              elif decisao == "2":
                while True:
                  try:
                    print("Qual atividade deseja enviar?\n")
                    atividades = clube_escolhido.get_atividades()
                    for i, atividade in enumerate(atividades, 1):
                      print(f"\n{i}° Atividade: {atividade.get_titulo()}")
                      situacao=False
                      respostas = atividade.get_respostas()
                      for resposta in respostas:
                        if  resposta.get_id_autor() == user_1.get_id():
                          situacao=True
                          print(f" Resposta: {resposta.get_titulo()}")
                        else:
                          pass
                      if situacao == False:
                        print("Nenhuma resposta enviada")
                      
                    escolha=input()
                    atividade = atividades[int(escolha) - 1]
                  except IndexError:
                    print("Atividade nao encontrada")
                    print("selecione uma atividade existente")
                  else:
                    existenciaDeResposta = False
                    respostas = atividade.get_respostas()
                    for resposta in respostas:
                      if resposta.get_id_autor() == user_1.get_id():
                        while True:
                          try:
                            print("Voce ja realizou o envio desta atividade")
                            print("[1]Deseja editar o envio desta  atividade?")
                            print("[2]voltar ao menu")
                            escolha = input()
                            if escolha == "1":
                              resposta.editar_envio(user_1.get_id())
                              atividade.set_respostas(resposta)
                              clube_escolhido.set_atividades(atividade)
                            elif  escolha == "2":
                              
                              pass
                            else:
                              raise AlternativaInvalida(escolha)  
                          except AlternativaInvalida as e:
                            print(e)
                          else:
                            existenciaDeResposta = True
                            break
                          finally:
                            sleep(2)
                            system("clear")
                      else:
                        pass
                      
                    if existenciaDeResposta == False:
                      atividade.concluir(user_1.get_id)
                      clube_escolhido.set_atividades(atividade)
                      break
                    
              elif decisao == "3":
                processo1 = True
              else: 
                raise AlternativaInvalida(decisao)  
                
            except AlternativaInvalida as e:
              print(e)
            else:
              print("Processando...")
              break
            finally:
              sleep(2)
              system("clear")
            
        elif opcao == "2": 
          clube = user_1.get_clubeAsssociado()
          chat = clube.get_chat()
          chat.exibir_mensagens()
          conversa = False
          while not conversa:
            try:
              print("você deseja:\n[1] enviar mensagem \n[2] atualizar o chat\n[3] voltar ao menu principal")
              resposta=input()
              if resposta == "1":
                mensagem=user_1.enviarMensagem()
                chat.send_mensage(mensagem)
              elif resposta == "2":
                system("clear")
                chat.exibir_mensagens()
              elif resposta == "3":
                conversa = True
              else:
                raise AlternativaInvalida(resposta)
            except AlternativaInvalida as e:
              print(e)
            else:
              print("aperte enter!!!")
              input ()
            finally:
              sleep(2)
              system("clear")
        elif opcao == "3":
          processo = True
          processoA = False
        elif opcao == "4":
          exit()
          
        else:
          raise AlternativaInvalida(opcao)
      except AlternativaInvalida as e:
        print(e)
      else:
        print("processo em execução...")
      finally:
        sleep(2)
        system("clear")