    #2°B Informatica Projeto COPAE
    #Grupo estudiantes:
    #Angélica Bechara
    #Helinia Alexandra
    #Isaque Simões

def dadosPréexistentes():
    from users.administrador import Administrador
    from users.usuario import Usuario
    from users.cordenador import Coordenador
    from users.membro import Membro
    from atividade import Atividade
    from clube import Clube
    from arquivo import Arquivo
    from mensagens import Mensagem
    from os import system

    bancoDeDados = {}
    clubesSistema = []

    ################### PREENCHIMENTO DO BANCO DE DADOS PARA EXEMPLIFICAR O FUNCIONAMENTO DO CÓDIGO #################
    #Observação: atesto que usamos chatgpt para gerar varias situações, para facilitar o procedimento, afinal são mais de 500 linhas.
    
    usuario1=Usuario()
    usuario1.set_id("8569")
    usuario1.set_nome("Angélica")
    usuario1.set_senha("1234")
    usuario1.set_email("angelicabec@ic.ufpb.br")
    usuario1.set_fone("999999999")
    usuario1.set_hobbies("boa apresentadora")
    usuario1.set_nivelAcesso("área inicial")
    bancoDeDados[usuario1.get_id()] = usuario1

    usuario2 = Usuario()
    usuario2.set_id("8570")
    usuario2.set_nome("João")
    usuario2.set_senha("abcd")
    usuario2.set_email("joao.silva@ic.ufpb.br")
    usuario2.set_fone("988888888")
    usuario2.set_hobbies("gosta de esportes")
    usuario2.set_nivelAcesso("área inicial")
    bancoDeDados[usuario2.get_id()] = usuario2


    usuario3 = Usuario()
    usuario3.set_id("8571")
    usuario3.set_nome("Mariana")
    usuario3.set_senha("5678")
    usuario3.set_email("mariana.santos@ic.ufpb.br")
    usuario3.set_fone("977777777")
    usuario3.set_hobbies("amante de música")
    usuario3.set_nivelAcesso("área inicial")
    bancoDeDados[usuario3.get_id()] = usuario3


    usuario4 = Usuario()
    usuario4.set_id("8572")
    usuario4.set_nome("Carlos")
    usuario4.set_senha("efgh")
    usuario4.set_email("carlos.medeiros@ic.ufpb.br")
    usuario4.set_fone("966666666")
    usuario4.set_hobbies("cinéfilo")
    usuario4.set_nivelAcesso("área inicial")
    bancoDeDados[usuario4.get_id()] = usuario4

    clube1 = Clube()
    clube1.set_nome("COPAE")
    clube1.set_descricao("Clube de Olimpiadas de Programação de Algoritmos e Estrutura de Dados")
    
    
    Coordenador1 = Coordenador()
    Coordenador1.set_id("8573")
    Coordenador1.set_nome("Helinia")
    Coordenador1.set_senha("jklm")
    Coordenador1.set_email("heliniaalexandra@ic.ufpb.br")
    Coordenador1.set_fone("955555555")
    Coordenador1.set_conhecimentoTecnico("programação")
    Coordenador1.set_experiencia("5 anos")
    Coordenador1.set_nivelAcesso("ilimitado no clube")
    Coordenador1.set_clube(clube1)
    bancoDeDados[Coordenador1.get_id()] = Coordenador1

    clube1.set_cordenador(Coordenador1)

    membro1 = Membro()
    membro1.set_id("8575")
    membro1.set_nome("Maria")
    membro1.set_senha("wxyz")
    membro1.set_email("maria.medeiros@ic.ufpb.br")
    membro1.set_fone("944444444")
    membro1.set_hobbies("cinéfilo")
    membro1.set_habilidades("programação")
    membro1.set_nivelAcesso("limitado ao clube")
    bancoDeDados[membro1.get_id()] = membro1

    membro2 = Membro()
    membro2.set_id("8576")
    membro2.set_nome("Luiz")
    membro2.set_senha("abcd1234")
    membro2.set_email("luiz.souza@ic.ufpb.br")
    membro2.set_fone("933333333")
    membro2.set_hobbies("amante de tecnologia")
    membro2.set_habilidades("design gráfico")
    membro2.set_nivelAcesso("limitado ao clube")
    bancoDeDados[membro2.get_id()] = membro2

    membro3 = Membro()
    membro3.set_id("8577")
    membro3.set_nome("Beatriz")
    membro3.set_senha("1234abcd")
    membro3.set_email("beatriz.alves@ic.ufpb.br")
    membro3.set_fone("922222222")
    membro3.set_hobbies("leitora voraz")
    membro3.set_habilidades("edição de vídeo")
    membro3.set_nivelAcesso("limitado ao clube")
    bancoDeDados[membro3.get_id()] = membro3

    membros1=[membro1, membro2, membro3]
    clube1.set_membros(membros1)

    atividade1 = Atividade()
    atividade1.set_titulo("Jogos")
    atividade1.set_descricao("Jogos de Programação de Algoritmos e Estrutura de Dados") 
    atividade1.set_data_vencimento("23/12/2024")
    atividade1.set_tipo_arquivo("PDF")
    clube1.set_atividades(atividade1)

    arquivo1 = Arquivo()
    arquivo1.set_titulo("Algoritmos para Jogo de Tabuleiro")
    arquivo1.set_autores(membro1.get_nome())
    arquivo1.set_id_autor(membro1.get_id())
    arquivo1.set_conteudo("Desenvolvimento de um jogo de tabuleiro utilizando algoritmos em Python para resolução de desafios.")

    arquivo2 = Arquivo()
    arquivo2.set_titulo("Interface Gráfica para Jogo de Algoritmos")
    arquivo2.set_autores(membro2.get_nome())
    arquivo2.set_id_autor(membro2.get_id())
    arquivo2.set_conteudo("Projeto de interface gráfica usando princípios de design gráfico para um jogo de algoritmos.")

    arquivo3 = Arquivo()
    arquivo3.set_titulo("Análise de Algoritmos em Jogos de Programação")
    arquivo3.set_autores(membro3.get_nome())
    arquivo3.set_id_autor(membro3.get_id())
    arquivo3.set_conteudo("Estudo e análise dos algoritmos usados em jogos de programação, focando em estrutura de dados.")

    arquivos1=[arquivo1, arquivo2, arquivo3]
    atividade1.set_respostas(arquivos1)

    atividade2 = Atividade()
    atividade2.set_titulo("Workshop de Python")
    atividade2.set_descricao("Workshop sobre Python para iniciantes, abordando fundamentos da linguagem")
    atividade2.set_data_vencimento("15/11/2024")
    atividade2.set_tipo_arquivo("PPT")
    clube1.set_atividades(atividade2)

    arquivo1_workshop = Arquivo()
    arquivo1_workshop.set_titulo("Introdução a Variáveis e Tipos de Dados em Python")
    arquivo1_workshop.set_autores(membro1.get_nome())
    arquivo1_workshop.set_id_autor(membro1.get_id())
    arquivo1_workshop.set_conteudo("Apresentação sobre conceitos básicos de variáveis, tipos de dados e operadores em Python.")

    arquivo2_workshop = Arquivo()
    arquivo2_workshop.set_titulo("Estruturas Condicionais e Loops em Python")
    arquivo2_workshop.set_autores(membro2.get_nome())
    arquivo2_workshop.set_id_autor(membro2.get_id())
    arquivo2_workshop.set_conteudo("Slides sobre estruturas condicionais e loops, incluindo exemplos práticos para iniciantes.")

    arquivo3_workshop = Arquivo()
    arquivo3_workshop.set_titulo("Funções e Modularização em Python")
    arquivo3_workshop.set_autores(membro3.get_nome())
    arquivo3_workshop.set_id_autor(membro3.get_id())
    arquivo3_workshop.set_conteudo("Apresentação abordando a criação de funções e o conceito de modularização no desenvolvimento em Python.")

    arquivos2=[arquivo1_workshop, arquivo2_workshop, arquivo3_workshop]
    atividade2.set_respostas(arquivos2)


    atividade3 = Atividade()
    atividade3.set_titulo("Hackathon de IA")
    atividade3.set_descricao("Desafio para criação de modelos de IA aplicados a problemas do mundo real")
    atividade3.set_data_vencimento("10/01/2025")
    atividade3.set_tipo_arquivo("DOCX")
    clube1.set_atividades(atividade3)

    arquivo1_hackathon = Arquivo()
    arquivo1_hackathon.set_titulo("Modelo de Regressão para Previsão de Valores")
    arquivo1_hackathon.set_autores(membro1.get_nome())
    arquivo1_hackathon.set_id_autor(membro1.get_id())
    arquivo1_hackathon.set_conteudo("Modelo de IA baseado em regressão linear para previsão de valores numéricos aplicados a cenários do mundo real.")

    arquivo2_hackathon = Arquivo()
    arquivo2_hackathon.set_titulo("Análise de Imagens com Redes Neurais Convolucionais")
    arquivo2_hackathon.set_autores(membro2.get_nome())
    arquivo2_hackathon.set_id_autor(membro2.get_id())
    arquivo2_hackathon.set_conteudo("Modelo de IA usando redes neurais convolucionais para análise e classificação de imagens.")

    arquivo3_hackathon = Arquivo()
    arquivo3_hackathon.set_titulo("Chatbot com Processamento de Linguagem Natural")
    arquivo3_hackathon.set_autores(membro3.get_nome())
    arquivo3_hackathon.set_id_autor(membro3.get_id())
    arquivo3_hackathon.set_conteudo("Desenvolvimento de um chatbot utilizando técnicas de processamento de linguagem natural para responder perguntas.")

    arquivos3=[arquivo1_hackathon, arquivo2_hackathon, arquivo3_hackathon]
    atividade3.set_respostas(arquivos3)

    atividades1=[atividade1, atividade2, atividade3]
    for atividade in atividades1:
        clube1.set_atividades(atividade)

    chatClube1 =  clube1.get_chat()

    # Mensagem inicial do coordenador
    mensagem1 = Mensagem("x","y")
    mensagem1.set_autores(Coordenador1.get_nome())
    mensagem1.set_conteudo("Olá, tudo bem? \nEsse clube foi criado para trabalharmos juntos rumo à Olimpíada de Programação de Algoritmos e Estrutura de Dados. \nAproveitem!")
    chatClube1.send_mensage(mensagem1)

    # Resposta de um dos membros
    mensagem2 = Mensagem("x","y")
    mensagem2.set_autores(membro1.get_nome())
    mensagem2.set_conteudo("Oi, Helinia! Tudo ótimo! Estou animada para começar! Quais são nossos primeiros passos?")
    chatClube1.send_mensage(mensagem2)

    # Mensagem do segundo membro
    mensagem3 = Mensagem("x","y")
    mensagem3.set_autores(membro2.get_nome())
    mensagem3.set_conteudo("Oi pessoal! Eu estava vendo algumas competições passadas e percebi que precisamos focar bastante em estruturas de dados. Que tal começarmos com um projeto sobre isso?")
    chatClube1.send_mensage(mensagem3)

    # Mensagem do terceiro membro
    mensagem4 = Mensagem("x","y")
    mensagem4.set_autores(membro3.get_nome())
    mensagem4.set_conteudo("Oi gente! Gostei da ideia, Luiz. Também acho que precisamos de prática em algoritmos. Talvez a gente possa fazer um estudo de caso juntos?")
    chatClube1.send_mensage(mensagem4)

    # Coordenador respondendo ao grupo
    mensagem5 = Mensagem("x","y")
    mensagem5.set_autores(Coordenador1.get_nome())
    mensagem5.set_conteudo("Adorei a proatividade de vocês! Vamos começar então com uma atividade focada em estruturas de dados e, em seguida, faremos alguns desafios de algoritmos.")
    chatClube1.send_mensage(mensagem5)

    # Membro 1 respondendo
    mensagem6 = Mensagem("x","y")
    mensagem6.set_autores(membro1.get_nome())
    mensagem6.set_conteudo("Ótimo! Vou revisar algumas estruturas mais complexas, como árvores e grafos. E, se precisar de ajuda, conto com vocês!")
    chatClube1.send_mensage(mensagem6)

    # Coordenador incentivando o trabalho em equipe
    mensagem7 = Mensagem("x","y")
    mensagem7.set_autores(Coordenador1.get_nome())
    mensagem7.set_conteudo("Isso mesmo, Maria! O objetivo aqui é nos apoiarmos e trocarmos conhecimentos. Qualquer dúvida, vamos discutindo no chat. Conto com todos!")
    chatClube1.send_mensage(mensagem7)
    
    clubesSistema.append(clube1)


    clube2 = Clube()
    clube2.set_nome("Clube de Literatura")
    clube2.set_descricao("Clube de Literatura e Escrita Criativa para apaixonados por leitura e desenvolvimento literário.")

    Coordenador2 = Coordenador()
    Coordenador2.set_id("2021")
    Coordenador2.set_nome("Júlio")
    Coordenador2.set_senha("poesia")
    Coordenador2.set_email("julio.souza@ic.ufpb.br")
    Coordenador2.set_fone("911111111")
    Coordenador2.set_conhecimentoTecnico("literatura clássica e escrita criativa")
    Coordenador2.set_experiencia("10 anos")
    Coordenador2.set_nivelAcesso("ilimitado no clube")
    Coordenador2.set_clube(clube2)
    bancoDeDados[Coordenador2.get_id()] = Coordenador2

    clube2.set_cordenador(Coordenador2)

    membro4 = Membro()
    membro4.set_id("2023")
    membro4.set_nome("Alice")
    membro4.set_senha("abc123")
    membro4.set_email("alice.literatura@ic.ufpb.br")
    membro4.set_fone("922222222")
    membro4.set_hobbies("leitura de fantasia e mistério")
    membro4.set_habilidades("criação de personagens")
    membro4.set_nivelAcesso("limitado ao clube")
    bancoDeDados[membro4.get_id()] = membro4

    membro5 = Membro()
    membro5.set_id("2024")
    membro5.set_nome("Miguel")
    membro5.set_senha("def456")
    membro5.set_email("miguel.poesia@ic.ufpb.br")
    membro5.set_fone("933333333")
    membro5.set_hobbies("poesia e ensaios")
    membro5.set_habilidades("rimas e metáforas")
    membro5.set_nivelAcesso("limitado ao clube")
    bancoDeDados[membro5.get_id()] = membro5

    membro6 = Membro()
    membro6.set_id("2025")
    membro6.set_nome("Lara")
    membro6.set_senha("ghi789")
    membro6.set_email("lara.ficcao@ic.ufpb.br")
    membro6.set_fone("944444444")
    membro6.set_hobbies("contos de ficção científica")
    membro6.set_habilidades("descrição de cenários e narrativa")
    membro6.set_nivelAcesso("limitado ao clube")
    bancoDeDados[membro6.get_id()] = membro6

    membros2 = [membro4, membro5, membro6]
    clube2.set_membros(membros2)

    atividade1_lit = Atividade()
    atividade1_lit.set_titulo("Oficina de Criação de Personagens")
    atividade1_lit.set_descricao("Desenvolvimento de personagens profundos e multidimensionais.")
    atividade1_lit.set_data_vencimento("23/11/2024")
    atividade1_lit.set_tipo_arquivo("DOCX")

    arquivo1_lit = Arquivo()
    arquivo1_lit.set_titulo("A Jornada do Herói no Gênero Fantasia")
    arquivo1_lit.set_autores(membro4.get_nome())
    arquivo1_lit.set_id_autor(membro4.get_id())
    arquivo1_lit.set_conteudo("Desenvolvimento de um personagem de fantasia com base na Jornada do Herói.")

    arquivo2_lit = Arquivo()
    arquivo2_lit.set_titulo("Personagens como Reflexo da Realidade Social")
    arquivo2_lit.set_autores(membro5.get_nome())
    arquivo2_lit.set_id_autor(membro5.get_id())
    arquivo2_lit.set_conteudo("Análise sobre como personagens literários refletem a sociedade.")

    arquivo3_lit = Arquivo()
    arquivo3_lit.set_titulo("O Papel dos Andróides em Narrativas Futuristas")
    arquivo3_lit.set_autores(membro6.get_nome())
    arquivo3_lit.set_id_autor(membro6.get_id())
    arquivo3_lit.set_conteudo("Exploração dos papéis dos andróides em histórias de ficção científica.")

    atividade1_lit.set_respostas([arquivo1_lit, arquivo2_lit, arquivo3_lit])

    # Segunda atividade: Oficina de Poesia e Versificação
    atividade2_lit = Atividade()
    atividade2_lit.set_titulo("Oficina de Poesia e Versificação")
    atividade2_lit.set_descricao("Exercícios de criação poética com foco em rima e métrica.")
    atividade2_lit.set_data_vencimento("05/12/2024")
    atividade2_lit.set_tipo_arquivo("DOCX")

    arquivo1_poesia = Arquivo()
    arquivo1_poesia.set_titulo("Poema sobre a Natureza")
    arquivo1_poesia.set_autores(membro5.get_nome())
    arquivo1_poesia.set_id_autor(membro5.get_id())
    arquivo1_poesia.set_conteudo("Poema explorando metáforas e a relação do ser humano com a natureza.")

    arquivo2_poesia = Arquivo()
    arquivo2_poesia.set_titulo("Soneto sobre o Tempo")
    arquivo2_poesia.set_autores(membro4.get_nome())
    arquivo2_poesia.set_id_autor(membro4.get_id())
    arquivo2_poesia.set_conteudo("Soneto em 14 versos refletindo sobre a passagem do tempo e a efemeridade da vida.")

    arquivo3_poesia = Arquivo()
    arquivo3_poesia.set_titulo("Haiku sobre as Estações")
    arquivo3_poesia.set_autores(membro6.get_nome())
    arquivo3_poesia.set_id_autor(membro6.get_id())
    arquivo3_poesia.set_conteudo("Haiku explorando a beleza e simplicidade das mudanças sazonais.")

    atividade2_lit.set_respostas([arquivo1_poesia, arquivo2_poesia, arquivo3_poesia])

    # Terceira atividade: Contos e Narrativas Curtas
    atividade3_lit = Atividade()
    atividade3_lit.set_titulo("Contos e Narrativas Curtas")
    atividade3_lit.set_descricao("Desenvolvimento de contos curtos, com foco em estrutura e narrativa.")
    atividade3_lit.set_data_vencimento("20/12/2024")
    atividade3_lit.set_tipo_arquivo("PDF")

    arquivo1_conto = Arquivo()
    arquivo1_conto.set_titulo("A Última Viagem")
    arquivo1_conto.set_autores(membro4.get_nome())
    arquivo1_conto.set_id_autor(membro4.get_id())
    arquivo1_conto.set_conteudo("Conto sobre uma jornada mística que desafia a percepção do tempo.")

    arquivo2_conto = Arquivo()
    arquivo2_conto.set_titulo("O Encontro Inesperado")
    arquivo2_conto.set_autores(membro6.get_nome())
    arquivo2_conto.set_id_autor(membro6.get_id())
    arquivo2_conto.set_conteudo("Narrativa que explora os temas de coincidência e destino em um café movimentado.")

    arquivo3_conto = Arquivo()
    arquivo3_conto.set_titulo("O Eco das Montanhas")
    arquivo3_conto.set_autores(membro5.get_nome())
    arquivo3_conto.set_id_autor(membro5.get_id())
    arquivo3_conto.set_conteudo("História que explora o isolamento e a introspecção em uma paisagem montanhosa.")

    atividade3_lit.set_respostas([arquivo1_conto, arquivo2_conto, arquivo3_conto])

    # Associando as atividades ao clube
    atividades_lit = [atividade1_lit, atividade2_lit, atividade3_lit]
    for atividade in atividades_lit:
        clube2.set_atividades(atividade)

    chatClube2 = clube2.get_chat()

    mensagem1_lit = Mensagem("x","y")
    mensagem1_lit.set_autores(Coordenador2.get_nome())
    mensagem1_lit.set_conteudo("Bem-vindos, pessoal! Esse clube foi criado para explorarmos juntos a magia da escrita. Vamos nos desafiar a escrever e a aprender juntos. Preparados?")
    chatClube2.send_mensage(mensagem1_lit)

    mensagem2_lit = Mensagem("x","y")
    mensagem2_lit.set_autores(membro4.get_nome())
    mensagem2_lit.set_conteudo("Oi, Júlio! Eu adoro criar universos e personagens, mas sempre acho difícil dar profundidade a eles. Você tem dicas?")
    chatClube2.send_mensage(mensagem2_lit)

    mensagem3_lit = Mensagem("x","y")
    mensagem3_lit.set_autores(membro5.get_nome())
    mensagem3_lit.set_conteudo("Oi, pessoal! Estou empolgado! Acho que nossa primeira oficina podia ser sobre a construção de sentimentos nos personagens.")
    chatClube2.send_mensage(mensagem3_lit)

    mensagem4_lit = Mensagem("x","y")
    mensagem4_lit.set_autores(membro6.get_nome())
    mensagem4_lit.set_conteudo("Concordo com o Miguel! Uma oficina de sentimentos e personalidades seria incrível. Podemos começar com um personagem em comum?")
    chatClube2.send_mensage(mensagem4_lit)

    clubesSistema.append(clube2)

    clube3 = Clube()
    clube3.set_nome("Clube de Sustentabilidade")
    clube3.set_descricao("Clube dedicado a explorar práticas sustentáveis e ciência ambiental.")
    

    Coordenador3 = Coordenador()
    Coordenador3.set_id("3031")
    Coordenador3.set_nome("Carolina")
    Coordenador3.set_senha("ecologia123")
    Coordenador3.set_email("carolina.sustentabilidade@ic.ufpb.br")
    Coordenador3.set_fone("955555555")
    Coordenador3.set_conhecimentoTecnico("ecologia e sustentabilidade")
    Coordenador3.set_experiencia("8 anos")
    Coordenador3.set_nivelAcesso("ilimitado no clube")
    Coordenador3.set_clube(clube3)
    bancoDeDados[Coordenador3.get_id()] = Coordenador3

    clube3.set_cordenador(Coordenador3)


    membro7 = Membro()
    membro7.set_id("3033")
    membro7.set_nome("Gabriel")
    membro7.set_senha("plantas2024")
    membro7.set_email("gabriel.ecologia@ic.ufpb.br")
    membro7.set_fone("966666666")
    membro7.set_hobbies("jardinagem e biologia")
    membro7.set_habilidades("cultivo sustentável")
    membro7.set_nivelAcesso("limitado ao clube")
    bancoDeDados[membro7.get_id()] = membro7

    membro8 = Membro()
    membro8.set_id("3034")
    membro8.set_nome("Bianca")
    membro8.set_senha("ativismo456")
    membro8.set_email("bianca.ativismo@ic.ufpb.br")
    membro8.set_fone("977777777")
    membro8.set_hobbies("ativismo ambiental")
    membro8.set_habilidades("comunicação e divulgação científica")
    membro8.set_nivelAcesso("limitado ao clube")
    bancoDeDados[membro8.get_id()] = membro8

    membro9 = Membro()
    membro9.set_id("3035")
    membro9.set_nome("Victor")
    membro9.set_senha("oceanos789")
    membro9.set_email("victor.ciencias@ic.ufpb.br")
    membro9.set_fone("988888888")
    membro9.set_hobbies("ciências dos oceanos")
    membro9.set_habilidades("análise de dados ambientais")
    membro9.set_nivelAcesso("limitado ao clube")
    bancoDeDados[membro9.get_id()] = membro9

    membros3 = [membro7, membro8, membro9]
    clube3.set_membros(membros3)

    atividade1_sust = Atividade()
    atividade1_sust.set_titulo("Projeto de Reciclagem Local")
    atividade1_sust.set_descricao("Desenvolvimento de um sistema de reciclagem comunitário")
    atividade1_sust.set_data_vencimento("01/12/2024")
    atividade1_sust.set_tipo_arquivo("PDF")

    arquivo1_sust = Arquivo()
    arquivo1_sust.set_titulo("Reciclagem e Compostagem Doméstica")
    arquivo1_sust.set_autores(membro7.get_nome())
    arquivo1_sust.set_id_autor(membro7.get_id())
    arquivo1_sust.set_conteudo("Projeto de reciclagem e compostagem para pequenos espaços urbanos.")

    arquivo2_sust = Arquivo()
    arquivo2_sust.set_titulo("Engajamento Comunitário para Coleta Seletiva")
    arquivo2_sust.set_autores(membro8.get_nome())
    arquivo2_sust.set_id_autor(membro8.get_id())
    arquivo2_sust.set_conteudo("Plano de comunicação para envolver a comunidade na coleta seletiva.")

    arquivo3_sust = Arquivo()
    arquivo3_sust.set_titulo("Redução de Descartes Plásticos nas Praias")
    arquivo3_sust.set_autores(membro9.get_nome())
    arquivo3_sust.set_id_autor(membro9.get_id())
    arquivo3_sust.set_conteudo("Métodos para minimizar o descarte de plástico nas áreas costeiras.")

    atividade1_sust.set_respostas([arquivo1_sust, arquivo2_sust, arquivo3_sust])

    # Segunda atividade: Projeto de Energias Renováveis
    atividade2_sust = Atividade()
    atividade2_sust.set_titulo("Projeto de Energias Renováveis")
    atividade2_sust.set_descricao("Estudo e implementação de soluções de energia renovável em pequena escala.")
    atividade2_sust.set_data_vencimento("15/12/2024")
    atividade2_sust.set_tipo_arquivo("PPT")

    arquivo1_energia = Arquivo()
    arquivo1_energia.set_titulo("Painéis Solares em Comunidades")
    arquivo1_energia.set_autores(membro7.get_nome())
    arquivo1_energia.set_id_autor(membro7.get_id())
    arquivo1_energia.set_conteudo("Análise de viabilidade e instalação de painéis solares em áreas urbanas.")

    arquivo2_energia = Arquivo()
    arquivo2_energia.set_titulo("Microturbinas para Energia Eólica")
    arquivo2_energia.set_autores(membro8.get_nome())
    arquivo2_energia.set_id_autor(membro8.get_id())
    arquivo2_energia.set_conteudo("Projeto de instalação de microturbinas em áreas com baixa velocidade de vento.")

    arquivo3_energia = Arquivo()
    arquivo3_energia.set_titulo("Sistemas de Biomassa Doméstica")
    arquivo3_energia.set_autores(membro9.get_nome())
    arquivo3_energia.set_id_autor(membro9.get_id())
    arquivo3_energia.set_conteudo("Uso de resíduos orgânicos para produção de biogás em comunidades rurais.")

    atividade2_sust.set_respostas([arquivo1_energia, arquivo2_energia, arquivo3_energia])

    # Terceira atividade: Redução de Pegada de Carbono
    atividade3_sust = Atividade()
    atividade3_sust.set_titulo("Redução de Pegada de Carbono")
    atividade3_sust.set_descricao("Práticas para reduzir a pegada de carbono nas atividades diárias.")
    atividade3_sust.set_data_vencimento("30/12/2024")
    atividade3_sust.set_tipo_arquivo("PDF")

    arquivo1_carbono = Arquivo()
    arquivo1_carbono.set_titulo("Práticas para Residências Sustentáveis")
    arquivo1_carbono.set_autores(membro8.get_nome())
    arquivo1_carbono.set_id_autor(membro8.get_id())
    arquivo1_carbono.set_conteudo("Sugestões para adaptação de hábitos domésticos visando a redução de emissão de carbono.")

    arquivo2_carbono = Arquivo()
    arquivo2_carbono.set_titulo("Transporte Verde e Emissão Zero")
    arquivo2_carbono.set_autores(membro9.get_nome())
    arquivo2_carbono.set_id_autor(membro9.get_id())
    arquivo2_carbono.set_conteudo("Estudo de modos de transporte com baixo impacto ambiental e emissão de gases poluentes.")

    arquivo3_carbono = Arquivo()
    arquivo3_carbono.set_titulo("Alimentação Saudável e Sustentável")
    arquivo3_carbono.set_autores(membro7.get_nome())
    arquivo3_carbono.set_id_autor(membro7.get_id())
    arquivo3_carbono.set_conteudo("Propostas de mudanças alimentares para reduzir o impacto ambiental e melhorar a saúde.")

    atividade3_sust.set_respostas([arquivo1_carbono, arquivo2_carbono, arquivo3_carbono])

    # Associando as atividades ao clube
    atividades_sust = [atividade1_sust, atividade2_sust, atividade3_sust]
    for atividade in atividades_sust:
        clube3.set_atividades(atividade)

    chatClube3 = clube3.get_chat()

    mensagem1_sust = Mensagem("x","y")
    mensagem1_sust.set_autores(Coordenador3.get_nome())
    mensagem1_sust.set_conteudo("Oi, pessoal! Nosso clube é dedicado a encontrar maneiras de tornar nossas comunidades mais sustentáveis. Estou animada para ver como cada um de vocês pode contribuir com suas ideias!")
    chatClube3.send_mensage(mensagem1_sust)

    mensagem2_sust = Mensagem("x","y")
    mensagem2_sust.set_autores(membro7.get_nome())
    mensagem2_sust.set_conteudo("Oi, Carolina! Eu tenho algumas ideias sobre compostagem urbana. Talvez a gente pudesse tentar um projeto comunitário?")
    chatClube3.send_mensage(mensagem2_sust)

    mensagem3_sust = Mensagem("x","y")
    mensagem3_sust.set_autores(membro8.get_nome())
    mensagem3_sust.set_conteudo("Oi, pessoal! Achei a ideia de um projeto comunitário ótima! Acredito que eu poderia ajudar na parte de comunicação para engajar as pessoas.")
    chatClube3.send_mensage(mensagem3_sust)

    mensagem4_sust = Mensagem("x","y")
    mensagem4_sust.set_autores(membro9.get_nome())
    mensagem4_sust.set_conteudo("Oi, todos! Podemos explorar como a ciência dos oceanos e a preservação ambiental estão conectadas. Posso contribuir com dados sobre impacto costeiro.")
    chatClube3.send_mensage(mensagem4_sust)
    
    clubesSistema.append(clube3)
    
    return bancoDeDados, clubesSistema