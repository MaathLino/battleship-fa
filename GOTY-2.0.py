import random

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#00: Mostra o logo da PlascanSoft

def ShowLogo():
   print("                                                                                ")
   print("                                                         . .                    ")
   print("                                                  8DDNNND=  .                   ")
   print("                                            .  ZNNNMN8M.                        ")
   print("                                           ..7DNNNMN8                           ")
   print("                        .                   DMNNNNN                             ")
   print("                       .+O .               ONNNND+                              ")
   print("                        ..NDD      7DD8  .~NNNDD .                              ")
   print("                           =NNN8DNNN?     NMNNN                                 ")
   print("                          . .DDNNND.     +NNNO.                                 ")
   print("                  ~8 .       +NNNNDO..   ZNN8                                   ")
   print("                  . 8NO.     NM8NNNNN8  .8NN          .                         ")
   print("                     +ND8 ...DZ. 8DNNDD. 8D,. .7NNNNNDNN: ..                    ")
   print("                     . DDN:.IN.  :NNNNDD=DD  ?NNNNNNNNNDNND .                   ")
   print("                        DNDZ$: $NDDDDNMNNN= DMNNDO:   ... . ..                  ")
   print("                        .7NDN?NN: ...NNNND~DND8                                 ")
   print("                          7NNN=       DNDNNND                                   ")
   print("                           8N?.       ,DNNMD.                                   ")
   print("    7..                   . D          ~DNN.                                    ")
   print("      $M:                 . 8          .NM$                                     ")
   print("        ZND?                Z           ~NI.                                    ")
   print("      . ..7NNN?.            7            NI                                     ")
   print("          ..?MNNNZ  ..+OI   O            D=                                     ")
   print("           .  8NMNND,    ,DNN$. .        8:                                     ")
   print("             . .8NNDNDN.    :NNNNN$.  ...8:      .   .                          ")
   print("                  DNNNMND$      DNNNNND: D.  .7NDNNNNDDZ=,    .                 ")
   print("                   ,NNNNNNNO   .  ~DNNNNNNO...   .,I8NDNNNNNNM8Z,.              ")
   print("                    .NDNNNNND8    .  DDNNNNNN8,.    .  IDNNNNNNNNNDD8O,         ")
   print("                      ,NDNNNNNND       ZNNNDNNNND,       ..=NNNDNNNNNNNNN.      ")
   print("                        $NNNNNNNN8  .    :DNNNNNNNNN..         +DNNNNNN:.       ")
   print("                         .NNNNNNNNN$     . .DNNNNNNNNDZ        .  =NND          ")
   print("                         . DNNNNNNNNM: .  .  ,DNNNNNNNNND.         .            ")
   print("                           .?NNNNNNNNND       .,NNNNNNNNDDDZ .                  ")
   print("                             =NNNNNNNNNNO.      .~DMNNNNNNNNNZ .                ")
   print("                              .NNNNNNNNNND         8MNNNNNNNND                  ")
   print("                               .NNNNNNNNNNM?       ..NNNNNN,.                   ")
   print("                                 DDNNNNNNNNN8       . ON                        ")
   print("                                  NNNNNNNNNNNN.                                 ")
   print("                                   8DNNNNNNNNNN                                 ")
   print("                                   ,NNNNNNND:..                                 ")
   print()
   print("                  FORFÉ AQUÁTICO 2.0 - Game of the Year Edition")
   print("                         Um produto PlascanSoft © 2015")
   print()
   print()
   print()
   return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#01: Função para auxiliar no controle de interface. Retorna o nome do jogador que inicia o jogo.

def PegaNome():
   print("Qual é o teu nome, pessoa? ", end="")

   while True:
      Nome=input()
      if len(Nome)>10:
         print("Tá pensando que é membro da côrte portuguesa?!")
         print("Encurta esse nome aí, faz favor: ", end="")
      elif len(Nome)==0:
         print("Tua mãe jogou fora a criança e criou a placenta?")
         print("Me diz o teu NOME, indivíduo: ", end="")
      else:
         print()
         break
   return Nome

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#02: Função para auxiliar no controle de interface. Identifica o gênero do jogador e...
#    retorna "True" se for homem, "False" se for mulher.

def PegaGenero(Nome):
   aux=Nome
   while True:
      TesteGenero=input("Isso por acaso é nome de homem? (S/N) ")
      TesteGenero=TesteGenero.lower()
      if ((TesteGenero!="s") and (TesteGenero!="n")):
         print("Não morde a chumbada, ", aux,", responde direitinho pra gente prosseguir.", sep="")
         print("Como eu estava dizendo... ", end="")
      else:
         print()
         if (TesteGenero=="s"):
            print("Firmeza, ", aux,". Seja bem-vindo ao Forfé Aquático.", sep="")
            break
         else:
            print("Suave, ", aux,". Seja bem-vinda ao Forfé Aquático (e desculpa ter perguntado).", sep="")
            break
   Homem=True
   if (TesteGenero=="n"):
      Homem=False
   return Homem

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#03: Escreve o menu principal com todas as opções.

def MostraMenu():
   print()
   print("-=-=-=-=-=-=-= Forfé Aquático =-=-=-=-=-=-=-")
   print()
   print("       1. Configurar o Tabuleiro")
   print("       2. Iniciar Partida")
   print("       3. Modo Patão Trapaceiro")
   print("       4. Sobre Essa Belezura de Jogo")
   print("       5. Mudar de Nome")
   print("       6. Sair")
   print()
   print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
   print()
   return;

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#04: Função para auxiliar o controle de menu. Retorna a escolha de alguma opção no menu principal.

def VerificaEscolhaMenu(Escolha, Homem):

   while True:
      if (Homem==True):
         print("Diz aí a tua escolha, parceiro: ", end="")
      else:
         print("A senhorita faça a gentileza de escolher uma opção: ", end="") 
      Escolha=input()            
      if ((len(Escolha)!=1) or (Escolha.isnumeric()==False)):
         print("Opção inválida! Tente novamente.")
      else:
         Escolha=int(Escolha)
         if ((Escolha)<1 or int(Escolha)>6):
            print("Opção inválida! Tente novamente.")
         elif ((Escolha)>=1 and (Escolha<=6)):
            return Escolha
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#05: Função para auxiliar o controle de interface. Retorna o nome do novo jogador.

def MudaNome(Nome, Genero):
   NomeAnterior=Nome
   Homem=Genero

   print("Temos um novo jogador: ", end="")

   while True:
      Nome=input()
      if len(Nome)>10:
         print("Tá pensando que é membro da côrte portuguesa? Encurta esse nome aí, faz favor. ", end="")
      elif len(Nome)==0:
         print("Tua mãe jogou fora a criança e criou a placenta? Me diz o teu NOME, indivíduo. ", end="")
      else:
         break

   if (Nome==NomeAnterior):
      if (Homem==True):
         print("Bem-vindo, ", Nome,"! Espero que jogue melhor do que o teu xará.", sep="")
      else:
         print("Bem-vinda, ", Nome,"! Espero que jogue melhor do que a tua xará.", sep="")
   else:
      print("Prazer, ", Nome,"! Espero que você jogue melhor do que ", NomeAnterior,".", sep="")
   return Nome

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#06: Função para auxiliar o controle de interface. Retorna "True" se o jogador for homem, e "False" se não for.

def MudaGenero(Nome, Genero):
   aux=Nome
   Homem=Genero

   while True:
      print("Rapidão:", aux,"é nome de homem? (S/N) ", end="")
      TesteGenero=input()
      TesteGenero=TesteGenero.lower()
      if ((TesteGenero!="s") and (TesteGenero!="n")):
         print("Colabora ai, ", aux,", vai, senão a gente fica aqui o dia todo.", sep="")
         print("Mais uma vez... ", end="")
      else:
         if (TesteGenero=="s"):
            print("Tá certo, ", aux,". Bora com isso, e boa sorte.", sep="")
            break
         else:
            print("Entendi. Seja bem-vinda, ", aux,", e boa sorte.", sep="")
            break

   Homem=True
   if (TesteGenero=="n"):
      Homem=False

   return Homem

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#07: Exibe informações sobre o jogo.
   
def SobreOJogo():
   print()
   print("'Forfé Aquático' é uma versão tupiniquim do clássico Battleship, criado nos")
   print("idos da Primeira Guerra Mundial para ser jogado com papel e caneta.  O jogo")
   print("foi desenvolvido para a disciplina de 'Introdução à Computação', ministrada")
   print("pelo professor  Adinovam Pimenta para o curso de  Biotecnologia, no segundo")
   print("semestre de 2015.")
   print()
   print("Regras:")
   print("Este jogo foi  criado originalmente para dois  jogadores, mas neste caso um")
   print("oponente será o computador. O jogador pode  configurar seu tabuleiro de ma-")
   print("neira automática ou manual. Se escolher 'manual', deve lembrar que as peças")
   print("não podem ficar adjacentes no tabuleiro (o jogo não permitirá isso).")
   print()
   print("O jogador e o computador então tomam turnos para procurar adivinhar a posi-")
   print("ção dos veículos do adversário, e quando um deles tiver destruído todos os ")
   print("veiculos do oponente, o jogo acaba.")
   print()
   print("Bom jogo!")
      
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#08: Exibe mensagem quando o programa é finalizado.
   
def Tchau(Nome):
   aux=Nome
   print("Deus lhe pague, ", aux,". Desculpa qualquer coisa, tá?", sep="")
   print("Volte sempre!")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#09: Reinicializa o tabuleiro do jogador com valor zero em todos os campos
   
def ResetTotalTabJog():
    global TabJog
    TabJog = [[[0 for k in range(0,3)] for j in range (0,15)] for i in range(0,15)]
        
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#10: Reinicializa o tabuleiro do computador com valor zero em todos os campos
    
def ResetTotalTabComp():
    global TabComp
    TabComp = [[[0 for k in range(0,3)] for j in range (0,15)] for i in range(0,15)]
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#11: Reinicia Parcialmente o tabuleiro do jogador, mantendo apenas as posições dos veículos
#    Obs: Esta função não foi utilizada, provavelmente porque não deu tempo de implementar
#    a funcionalidade da qual ela faria parte.    
def ResetParcialTabJog():
   global TabJog

   for lin in range(0,15):
      for col in range(0,15):
         if (TabJog[i][j][0]>1):   # se a posição (i,j) for veículo...
            TabJog[i][j][0]=2      # ...essa posição recebe o flag de "veículo intacto".

         TabJog[i][j][1]=0         # Todas as posições recebem o flag de "ainda não atacado".

   # Observe que TabJog[i][j][0] não sofre alteração para posições vazias ou adjacentes
   # Observe que TabJog[i][j][2] não sofre nenhuma alteração, pois refere-se aos tipos de veículos

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#12: Escreve os dois tabuleiros na tela, o do jogador e o do computador, lado a lado.
#    As informações do tabuleiro do computador estão todas visíveis.
def EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp):

    if len(Nome)==10:
       esp=8
       esp2=19
    elif len(Nome)==9 or len(Nome)==8:
       esp=9
       esp2=20
    elif len(Nome)==7 or len(Nome)==6:
       esp=10
       esp2=21
    elif len(Nome)==5 or len(Nome)==4:
       esp=11
       esp2=22
    elif len(Nome)==3 or len(Nome)==2:
       esp=12
       esp2=23
    elif len(Nome)==1:
       esp=13
       esp2=24
        
    print()
    print(esp*" ", end="")
    if (Homem==True):
       print("Grid do %s"%Nome, end="")
    else:
       print("Grid da %s"%Nome, end="")
    print(esp2*" ", end="")
    print("Grid do Computador")
    print()
    print("   A B C D E F G H I J K L M N O        A B C D E F G H I J K L M N O")
    for i in range(0,15):
        # Este if só serve para justificar a coluna dos números,
        # uma vez que alguns números so tem 1 dígito e outros tem 2
        if (i<9):
            print("", i+1, end=" ")
        else:
            print(i+1, end=" ")
        
        for j in range (0,15):
            if ((TabJog[i][j][0]<2) and (TabJog[i][j][1]==0)):   # vazio e ainda não atacado
                print("- ", end="")
            elif ((TabJog[i][j][0]<2) and (TabJog[i][j][1]==1)): # vazio e já atacado
                print("O ", end="")
            elif (TabJog[i][j][0]==2):  # veículo intacto
                print("# ", end="")
            elif(TabJog[i][j][0]==3):   # veículo danificado
                print("X ", end="")
            elif(TabJog[i][j][0]==4):   # veículo destruído
                print("A ", end="")     
            else:                       # ERRO! Valor inválido em TabJog[i][j][0]
                print("E ", end="")     

        # justificando a coluna dos números para o tabuleiro do computador
        print("    ", end="")
        if (i<9):
            print("", i+1, end=" ")
        else:
            print(i+1, end=" ")

        for j in range (0,15):
            if ((TabComp[i][j][0]<2) and (TabComp[i][j][1]==0)):   # vazio e ainda não atacado
                print("- ", end="")
            elif ((TabComp[i][j][0]<2) and (TabComp[i][j][1]==1)): # vazio e já atacado
                print("O ", end="")
            elif (TabComp[i][j][0]==2):  # veículo intacto
                print("# ", end="")
            elif(TabComp[i][j][0]==3):   # veículo danificado
                print("X ", end="")
            elif(TabComp[i][j][0]==4):   # veículo destruído
                print("A ", end="")     
            else:                        # ERRO! Valor inválido em TabComp[i][j][0]
                print("E ", end="")

        print()
    print()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#13: Escreve os dois tabuleiros na tela, o do jogador e o do computador, lado a lado.
#    As informações do tabuleiro do computador estão ocultas, até serem atacadas.
def EscreverTabuleiros(Nome, Homem, TabJog, TabComp):

    if len(Nome)==10:
       esp=8
       esp2=19
    elif len(Nome)==9 or len(Nome)==8:
       esp=9
       esp2=20
    elif len(Nome)==7 or len(Nome)==6:
       esp=10
       esp2=21
    elif len(Nome)==5 or len(Nome)==4:
       esp=11
       esp2=22
    elif len(Nome)==3 or len(Nome)==2:
       esp=12
       esp2=23
    elif len(Nome)==1:
       esp=13
       esp2=24
        
    print()
    print(esp*" ", end="")
    if (Homem==True):
       print("Grid do %s"%Nome, end="")
    else:
       print("Grid da %s"%Nome, end="")
    print(esp2*" ", end="")
    print("Grid do Computador")
    print()
    print("   A B C D E F G H I J K L M N O        A B C D E F G H I J K L M N O")
    for i in range(0,15):
        # Este if só serve para justificar a coluna dos números,
        # uma vez que alguns números so tem 1 dígito e outros tem 2
        if (i<9):
            print("", i+1, end=" ")
        else:
            print(i+1, end=" ")
        
        for j in range (0,15):
            if ((TabJog[i][j][0]<2) and (TabJog[i][j][1]==0)):   # vazio e ainda não atacado
                print("- ", end="")
            elif ((TabJog[i][j][0]<2) and (TabJog[i][j][1]==1)): # vazio e já atacado
                print("O ", end="")
            elif (TabJog[i][j][0]==2):  # veículo intacto
                print("# ", end="")
            elif(TabJog[i][j][0]==3):   # veículo danificado
                print("X ", end="")
            elif(TabJog[i][j][0]==4):   # veículo destruído
                print("A ", end="")     
            else:                       # ERRO! Valor inválido em TabJog[i][j][0]
                print("E ", end="")     

        # justificando a coluna dos números para o tabuleiro do computador
        print("    ", end="")
        if (i<9):
            print("", i+1, end=" ")
        else:
            print(i+1, end=" ")

        for j in range (0,15):
            if (TabComp[i][j][1]==0):    # ainda não atacado
               print("- ", end="")
            elif (TabComp[i][j][0]<2):   # vazio
                print("O ", end="")
            elif(TabComp[i][j][0]==3):   # veículo danificado
                print("X ", end="")
            elif(TabComp[i][j][0]==4):   # veículo destruído
                print("A ", end="")     
            else:                        # ERRO! Valor inválido em TabComp[i][j][0]
                print("E ", end="")

        print()
    print()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#14: Escreve apenas o tabuleiro do jogador na tela.
    
def EscreverTabJog(Nome, Homem, TabJog):

    if len(Nome)==10:
       esp=8
       esp2=19
    elif len(Nome)==9 or len(Nome)==8:
       esp=9
       esp2=20
    elif len(Nome)==7 or len(Nome)==6:
       esp=10
       esp2=21
    elif len(Nome)==5 or len(Nome)==4:
       esp=11
       esp2=22
    elif len(Nome)==3 or len(Nome)==2:
       esp=12
       esp2=23
    elif len(Nome)==1:
       esp=13
       esp2=24
        
    print()
    print(esp*" ", end="")
    if (Homem==True):
       print("Grid do %s"%Nome)
    else:
       print("Grid da %s"%Nome)
    print()
    print("   A B C D E F G H I J K L M N O")
    for i in range(0,15):
        # Este if só serve para justificar a coluna dos números,
        # uma vez que alguns números so tem 1 dígito e outros tem 2
        if (i<9):
            print("", i+1, end=" ")
        else:
            print(i+1, end=" ")
        
        for j in range (0,15):
            if ((TabJog[i][j][0]<2) and (TabJog[i][j][1]==0)):   # vazio e ainda não atacado
                print("- ", end="")
            elif ((TabJog[i][j][0]<2) and (TabJog[i][j][1]==1)): # vazio e já atacado
                print("O ", end="")
            elif (TabJog[i][j][0]==2):  # veículo intacto
                print("# ", end="")
            elif(TabJog[i][j][0]==3):   # veículo danificado
                print("X ", end="")
            elif(TabJog[i][j][0]==4):   # veículo destruído
                print("A ", end="")     
            else:                       # ERRO! Valor inválido em TabJog[i][j][0]
                print("E ", end="")

        print()
    print()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#15: Escreve apenas o tabuleiro do jogador na tela, incluindo os espaços adjacentes.
#    Obs: Esta função foi utilizada apenas para realizar testes durante o desenvolvimento.
    
def EscreverTabJog2(TabJog):

    print()
    print("          Grid do Jogador")
    print()
    print("   A B C D E F G H I J K L M N O")
    for i in range(0,15):
        # Este if só serve para justificar a coluna dos números,
        # uma vez que alguns números so tem 1 dígito e outros tem 2
        if (i<9):
            print("", i+1, end=" ")
        else:
            print(i+1, end=" ")
        
        for j in range (0,15):
            if ((TabJog[i][j][0]==0) and (TabJog[i][j][1]==0)):    # vazio e ainda não atacado
                print("- ", end="")
            elif ((TabJog[i][j][0]==1) and (TabJog[i][j][1]==0)):  # adjacente e ainda não atacado
                print("+ ", end="")
            elif ((TabJog[i][j][0]<2) and (TabJog[i][j][1]==1)):   # vazio/adjacente e já atacado
                print("O ", end="")
            elif (TabJog[i][j][0]==2):  # veículo intacto
                print("# ", end="")
            elif(TabJog[i][j][0]==3):   # veículo danificado
                print("X ", end="")
            elif(TabJog[i][j][0]==4):   # veículo destruído
                print("A ", end="")     
            else:                       # ERRO! Valor inválido em TabJog[i][j][0]
                print("E ", end="")

        print()
    print()
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#16: Escreve apenas o tabuleiro do jogador na tela, incluindo os espaços adjacentes
#    e as flags que designam tipo de veículo, ou seja, TabJog[i][j][2]
#    Obs: Esta função foi utilizada apenas para realizar testes durante o desenvolvimento.    
def EscreverTabJog3(TabJog):

    print()
    print("          Grid do Jogador")
    print()
    print("   A B C D E F G H I J K L M N O")
    for i in range(0,15):
        # Este if só serve para justificar a coluna dos números,
        # uma vez que alguns números so tem 1 dígito e outros tem 2
        if (i<9):
            print("", i+1, end=" ")
        else:
            print(i+1, end=" ")
        
        for j in range (0,15):
            if ((TabJog[i][j][0]==0) and (TabJog[i][j][1]==0)):    # vazio e ainda não atacado
                print("- ", end="")
            elif ((TabJog[i][j][0]==1) and (TabJog[i][j][1]==0)):  # adjacente e ainda não atacado
                print("+ ", end="")
            elif ((TabJog[i][j][0]<2) and (TabJog[i][j][1]==1)):   # vazio/adjacente e já atacado
                print("O ", end="")
            elif (TabJog[i][j][2]==1):  # submarino
                print("1 ", end="")
            elif(TabJog[i][j][2]==2):   # cruzador
                print("2 ", end="")
            elif(TabJog[i][j][2]==3):   # hidroavião
                print("3 ", end="")
            elif(TabJog[i][j][2]==4):   # encouraçado
                print("4 ", end="")
            elif(TabJog[i][j][2]==5):   # porta-aviões
                print("5 ", end="")     
            else:                       # ERRO! Valor inválido em TabJog[i][j][0]
                print("E ", end="")

        print()
    print()
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#17: Verifica se a posição no tabuleiro é válida para posicionar um porta-aviões.
#    Retorna "True" se a posição é válida, e "False" se não for.
    
def PosicaoPortaAvioesValida(Tabuleiro, i, j, orientacao):
    # (i,j) é a primeira posição de uma peça que ocupa cinco posições
    # orientação = 0 ---> horizonal (as posições são contadas da esquerda pra direita)
    # orientação = 1 ---> vertical  (as posições são contadas de cima pra baixo)

    # assume-se de inicio que a posição (i,j) na matriz é válida
    PosicaoValida=True

    if ((i<0) or (j<0)):
        PosicaoValida=False
        return(PosicaoValida)

    if ((i>14) or (j>14)):
        PosicaoValida=False
        return(PosicaoValida)

    # testa se a peça vai "sair" do tabuleiro
    # orientacao horizontal
    if (orientacao==0): 
        if (j>10):
            PosicaoValida=False
            return(PosicaoValida)
    # orientacao vertical
    else:               
        if (i>10):
            PosicaoValida=False
            return(PosicaoValida)

    # testa se a peça tem sobreposição ou adjacência
    # orientacao horizontal
    if (orientacao==0):
        for j in range(j, j+5):
            if (Tabuleiro[i][j][0]>0): # ver descrição do campo [i][j][0]
                PosicaoValida=False
                return(PosicaoValida)
    #orientacao vertical
    else:
        for i in range(i, i+5):
            if (Tabuleiro[i][j][0]>0): # ver descrição do campo [i][j][0]
                PosicaoValida=False
                return(PosicaoValida)
    
    # se a posição (i,j) passar em todos os testes, a função returna "True"
    return(PosicaoValida)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#18: Verifica se a posição no tabuleiro é válida para posicionar um encouraçado.
#    Retorna "True" se a posição é válida, e "False" se não for.
def PosicaoEncouracadoValida(Tabuleiro, i, j, orientacao):
    # (i,j) é a primeira posição de uma peça que ocupa quatro posições
    # orientação = 0 ---> horizonal (as posições são contadas da esquerda pra direita)
    # orientação = 1 ---> vertical  (as posições são contadas de cima pra baixo)

    # assume-se de inicio que a posição (i,j) na matriz é válida
    PosicaoValida=True

    if ((i<0) or (j<0)):
        PosicaoValida=False
        return(PosicaoValida)

    if ((i>14) or (j>14)):
        PosicaoValida=False
        return(PosicaoValida)

    # testa se a peça vai "sair" do tabuleiro
    # orientacao horizontal
    if (orientacao==0): 
        if (j>11):
            PosicaoValida=False
            return(PosicaoValida)
    # orientacao vertical
    else:               
        if (i>11):
            PosicaoValida=False
            return(PosicaoValida)

    # testa se a peça tem sobreposição ou adjacência
    # orientacao horizontal
    if (orientacao==0):
        for j in range(j, j+4):
            if (Tabuleiro[i][j][0]>0): # ver descrição do campo [i][j][0]
                PosicaoValida=False
                return(PosicaoValida)
    #orientacao vertical
    else:
        for i in range(i, i+4):
            if (Tabuleiro[i][j][0]>0): # ver descrição do campo [i][j][0]
                PosicaoValida=False
                return(PosicaoValida)

    # se a posição (i,j) passar em todos os testes, a função returna "True"
    return(PosicaoValida)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#19: Verifica se a posição no tabuleiro é válida para posicionar um Cruzador.
#    Retorna "True" se a posição é válida, e "False" se não for.
def PosicaoCruzadorValida(Tabuleiro, i, j, orientacao):
    # (i,j) é a primeira posição de uma peça que ocupa duas posições
    # orientação = 0 ---> horizonal (as posições são contadas da esquerda pra direita)
    # orientação = 1 ---> vertical  (as posições são contadas de cima pra baixo)

    # assume-se de inicio que a posição (i,j) na matriz é válida
    PosicaoValida=True

    if ((i<0) or (j<0)):
        PosicaoValida=False
        return(PosicaoValida)

    if ((i>14) or (j>14)):
        PosicaoValida=False
        return(PosicaoValida)

    # testa se a peça vai "sair" do tabuleiro
    # orientacao horizontal
    if (orientacao==0): 
        if (j>13):
            PosicaoValida=False
            return(PosicaoValida)
    # orientacao vertical
    else:               
        if (i>13):
            PosicaoValida=False
            return(PosicaoValida)

    # testa se a peça tem sobreposição ou adjacência
    # orientacao horizontal
    if (orientacao==0):
        for j in range(j, j+2):
            if (Tabuleiro[i][j][0]>0): # ver descrição do campo [i][j][0]
                PosicaoValida=False
                return(PosicaoValida)
    #orientacao vertical
    else:
        for i in range(i, i+2):
            if (Tabuleiro[i][j][0]>0): # ver descrição do campo [i][j][0]
                PosicaoValida=False
                return(PosicaoValida)

    # se a posição (i,j) passar em todos os testes, a função returna "True"
    return(PosicaoValida)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#20: Verifica se a posição no tabuleiro é válida para posicionar um hidroavião.
#    Retorna "True" se a posição é válida, e "False" se não for.
def PosicaoHidroaviaoValida(Tabuleiro, i, j, orientacao):
    # (i,j) é a posição do nariz do hidroavião
    # orientação = 0 ---> nariz para cima
    # orientação = 1 ---> nariz para a direita
    # orientação = 2 ---> nariz para baixo
    # orientação = 3 ---> nariz para a esquerda

    # assume-se de inicio que a posição (i,j) na matriz é válida
    PosicaoValida=True

    if ((i<0) or (j<0)):
        PosicaoValida=False
        return(PosicaoValida)

    if ((i>14) or (j>14)):
        PosicaoValida=False
        return(PosicaoValida)

    # testa se a peça vai "sair" do tabuleiro
    # nariz para cima
    if (orientacao==0):
        if ((j==0) or (j==14) or (i==14)):
            PosicaoValida=False
            return(PosicaoValida)
    # nariz para direita
    elif (orientacao==1):
        if ((j==0) or (i==0) or (i==14)):
            PosicaoValida=False
            return(PosicaoValida)
    # nariz para baixo
    elif (orientacao==2):
        if ((j==0) or (j==14) or (i==0)):
            PosicaoValida=False
            return(PosicaoValida)
    # nariz para esquerda
    else:
        if ((j==14) or (i==0) or (i==14)):
            PosicaoValida=False
            return(PosicaoValida)
    
    # testa se a peça tem sobreposição ou adjacência:
    # nariz para cima
    if (orientacao==0):
        if ((Tabuleiro[i][j][0]>0) or (Tabuleiro[i+1][j-1][0]>0) or (Tabuleiro[i+1][j+1][0]>0)):
            PosicaoValida=False
            return(PosicaoValida)           
    # nariz para direita
    elif (orientacao==1):
        if ((Tabuleiro[i][j][0]>0) or (Tabuleiro[i-1][j-1][0]>0) or (Tabuleiro[i+1][j-1][0]>0)):
            PosicaoValida=False
            return(PosicaoValida)        
    # nariz para baixo
    elif (orientacao==2):
        if ((Tabuleiro[i][j][0]>0) or (Tabuleiro[i-1][j-1][0]>0) or (Tabuleiro[i-1][j+1][0]>0)):
            PosicaoValida=False
            return(PosicaoValida)        
    # nariz para esquerda
    else:
        if ((Tabuleiro[i][j][0]>0) or (Tabuleiro[i-1][j+1][0]>0) or (Tabuleiro[i+1][j+1][0]>0)):
            PosicaoValida=False
            return(PosicaoValida)
        
    # se a posição (i,j) passar em todos os testes, a função returna "True"
    return(PosicaoValida)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#21: Verifica se a posição no tabuleiro é válida para posicionar um Submarino.
#    Retorna "True" se a posição é válida, e "False" se não for.
def PosicaoSubmarinoValida(Tabuleiro, i, j):
    # (i,j) é a posição do submarino, que ocupa apenas um espaço
    
    if ((i<0) or (j<0)):
        PosicaoValida=False
        return(PosicaoValida)

    if ((i>14) or (j>14)):
        PosicaoValida=False
        return(PosicaoValida)

    PosicaoValida=True
    if (Tabuleiro[i][j][0]>0):
        PosicaoValida=False

    return(PosicaoValida)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#22: Insere um porta-aviões no tabuleiro. O autor dessa função reconhece que tomou o
# caminho mais estúpido e trabalhoso para implementar a mesma, mas no frigir dos
# ovos o que conta é que ela funciona. Pare de me julgar. - Inforzato
def InserirPortaAvioes(Tabuleiro, i, j, orientacao):
    # (i,j) é a primeira posição de uma peça que ocupa cinco posições
    # orientação = 0 ---> horizonal (as posições são contadas da esquerda pra direita)
    # orientação = 1 ---> vertical  (as posições são contadas de cima pra baixo)

    if (orientacao==0):
    # veículo está na HORIZONTAL
        
        # Primeiramente, examina-se e modifica-se a vizinhança das extremidades
        if ((i==0) and (j==0)):     # encostado na quina superior esquerda
            # extremidade esquerda
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i+1][j+4][0]=1
            Tabuleiro[i][j+5][0]=1
            Tabuleiro[i+1][j+5][0]=1
        elif ((i==0) and (j==10)):  # encostado na quina superior direita
            # extremidade esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i+1][j+4][0]=1
        elif ((i==14) and (j==0)):  # encostado na quina inferior esquerda
            # extremidade esquerda
            Tabuleiro[i-1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+4][0]=1
            Tabuleiro[i-1][j+5][0]=1
            Tabuleiro[i][j+5][0]=1
        elif ((i==14) and (j==10)): # encostado na quina inferior direita
            # extremidade esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+4][0]=1
        elif (i==0):   # encostado na borda superior, mas não numa quina
            # extremidade esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i][j+5][0]=1
            Tabuleiro[i+1][j+4][0]=1
            Tabuleiro[i+1][j+5][0]=1            
        elif (i==14):  # encostado na borda inferior, mas não numa quina
            # extremidade esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            # extremidade direita
            Tabuleiro[i][j+5][0]=1
            Tabuleiro[i-1][j+4][0]=1
            Tabuleiro[i-1][j+5][0]=1            
        elif (j==0):   # encostado na borda esquerda, mas não numa quina
            # extremidade esquerda
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+4][0]=1
            Tabuleiro[i+1][j+4][0]=1
            Tabuleiro[i-1][j+5][0]=1
            Tabuleiro[i][j+5][0]=1
            Tabuleiro[i+1][j+5][0]=1
        elif (j==10):  # encostado na borda direita, mas não numa quina
            # extremidade esquerda
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+4][0]=1
            Tabuleiro[i+1][j+4][0]=1            
        else:          # não encosta em nenhuma borda    
            # extremidade esquerda
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+4][0]=1
            Tabuleiro[i+1][j+4][0]=1
            Tabuleiro[i-1][j+5][0]=1
            Tabuleiro[i][j+5][0]=1
            Tabuleiro[i+1][j+5][0]=1

        # modifica-se a vizinhança da parte "interna" do porta-aviões, isto é,
        # das posições localizadas entre as extremidades.
        for col in range(j+1, j+4):
            if (i!=0):  # não está encostando na borda superior
                Tabuleiro[i-1][col][0]=1
            if (i!=14): # não está encostando na borda inferior
                Tabuleiro[i+1][col][0]=1

    else:
    # veículo está na VERTICAL
        
        # Primeiramente, examina-se e modifica-se a vizinhança das extremidades
        if ((i==0) and (j==0)):     # encostado na quina superior esquerda
            # extremidade superior
            Tabuleiro[i][j+1][0]=1
            # extremidade inferior
            Tabuleiro[i+4][j+1][0]=1
            Tabuleiro[i+5][j][0]=1
            Tabuleiro[i+5][j+1][0]=1            
        elif ((i==0) and (j==14)):  # encostado na quina superior direita
            # extremidade superior
            Tabuleiro[i][j-1][0]=1
            # extremidade inferior
            Tabuleiro[i+4][j-1][0]=1
            Tabuleiro[i+5][j-1][0]=1
            Tabuleiro[i+5][j][0]=1            
        elif ((i==10) and (j==0)):  # encostado na quina inferior esquerda
            # extremidade superior
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j+1][0]=1            
            # extremidade inferior
            Tabuleiro[i+4][j+1][0]=1            
        elif ((i==10) and (j==14)): # encostado na quina inferior direita
            # extremidade superior
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i][j-1][0]=1            
            # extremidade inferior
            Tabuleiro[i+4][j-1][0]=1            
        elif (i==0):   # encostado na borda superior, mas não numa quina
            # extremidade superior
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            # extremidade inferior
            Tabuleiro[i+4][j-1][0]=1
            Tabuleiro[i+4][j+1][0]=1
            Tabuleiro[i+5][j-1][0]=1
            Tabuleiro[i+5][j][0]=1
            Tabuleiro[i+5][j+1][0]=1                        
        elif (i==10):  # encostado na borda inferior, mas não numa quina
            # extremidade superior
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1            
            # extremidade inferior
            Tabuleiro[i+4][j-1][0]=1
            Tabuleiro[i+4][j+1][0]=1                        
        elif (j==0):   # encostado na borda esquerda, mas não numa quina
            # extremidade superior
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j+1][0]=1            
            # extremidade inferior
            Tabuleiro[i+4][j+1][0]=1
            Tabuleiro[i+5][j][0]=1
            Tabuleiro[i+5][j+1][0]=1            
        elif (j==14):  # encostado na borda direita, mas não numa quina
            # extremidade superior
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i][j-1][0]=1            
            # extremidade inferior
            Tabuleiro[i+4][j-1][0]=1
            Tabuleiro[i+5][j-1][0]=1
            Tabuleiro[i+5][j][0]=1                        
        else:          # não encosta em nenhuma borda    
            # extremidade superior
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1            
            # extremidade inferior
            Tabuleiro[i+4][j-1][0]=1
            Tabuleiro[i+4][j+1][0]=1
            Tabuleiro[i+5][j-1][0]=1
            Tabuleiro[i+5][j][0]=1
            Tabuleiro[i+5][j+1][0]=1            

        # modifica-se a vizinhança da parte "interna" do porta-aviões, isto é,
        # das posições localizadas entre as extremidades.
        for lin in range(i+1, i+4):
            if (j!=0):  # não está encostando na borda esquerda
                Tabuleiro[lin][j-1][0]=1
            if (j!=14): # não está encostando na borda direita
                Tabuleiro[lin][j+1][0]=1       
   
    # Atribui-se as posições do porta-aviões propriamente dito:
    # orientacao horizontal
    if (orientacao==0):
        for col in range(j, j+5):
            Tabuleiro[i][col][0]=2   # veículo intacto
            Tabuleiro[i][col][2]=5   # porta-aviões
    # orientacao vertical
    else:
        for lin in range(i, i+5):
            Tabuleiro[lin][j][0]=2   # veículo intacto
            Tabuleiro[lin][j][2]=5   # porta-aviões        

    return(Tabuleiro)
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#23: Insere um encouraçado no tabuleiro. O autor desta função reconhece que tomou
# caminho mais estúpido e trabalhoso para implementar a mesma, mas no frigir dos
# ovos o que conta é que ela funciona. Pare de me julgar. - Inforzato
def InserirEncouracado(Tabuleiro, i, j, orientacao):
    # (i,j) é a primeira posição de uma peça que ocupa quatro posições
    # orientação = 0 ---> horizonal (as posições são contadas da esquerda pra direita)
    # orientação = 1 ---> vertical  (as posições são contadas de cima pra baixo)

    if (orientacao==0):
    # veículo está na HORIZONTAL
        
        # Primeiramente, examina-se e modifica-se a vizinhança das extremidades
        if ((i==0) and (j==0)):     # encostado na quina superior esquerda
            # extremidade esquerda
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i+1][j+3][0]=1
            Tabuleiro[i][j+4][0]=1
            Tabuleiro[i+1][j+4][0]=1
        elif ((i==0) and (j==11)):  # encostado na quina superior direita
            # extremidade esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i+1][j+3][0]=1
        elif ((i==14) and (j==0)):  # encostado na quina inferior esquerda
            # extremidade esquerda
            Tabuleiro[i-1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+3][0]=1
            Tabuleiro[i-1][j+4][0]=1
            Tabuleiro[i][j+4][0]=1
        elif ((i==14) and (j==11)): # encostado na quina inferior direita
            # extremidade esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+3][0]=1
        elif (i==0):   # encostado na borda superior, mas não numa quina
            # extremidade esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i][j+4][0]=1
            Tabuleiro[i+1][j+3][0]=1
            Tabuleiro[i+1][j+4][0]=1            
        elif (i==14):  # encostado na borda inferior, mas não numa quina
            # extremidade esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            # extremidade direita
            Tabuleiro[i][j+4][0]=1
            Tabuleiro[i-1][j+3][0]=1
            Tabuleiro[i-1][j+4][0]=1            
        elif (j==0):   # encostado na borda esquerda, mas não numa quina
            # extremidade esquerda
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+3][0]=1
            Tabuleiro[i+1][j+3][0]=1
            Tabuleiro[i-1][j+4][0]=1
            Tabuleiro[i][j+4][0]=1
            Tabuleiro[i+1][j+4][0]=1
        elif (j==11):  # encostado na borda direita, mas não numa quina
            # extremidade esquerda
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+3][0]=1
            Tabuleiro[i+1][j+3][0]=1            
        else:          # não encosta em nenhuma borda    
            # extremidade esquerda
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            # extremidade direita
            Tabuleiro[i-1][j+3][0]=1
            Tabuleiro[i+1][j+3][0]=1
            Tabuleiro[i-1][j+4][0]=1
            Tabuleiro[i][j+4][0]=1
            Tabuleiro[i+1][j+4][0]=1

        # modifica-se a vizinhança da parte "interna" do Encouraçado, isto é,
        # das posições localizadas entre as extremidades.
        for col in range(j+1, j+3):
            if (i!=0):  # não está encostando na borda superior
                Tabuleiro[i-1][col][0]=1
            if (i!=14): # não está encostando na borda inferior
                Tabuleiro[i+1][col][0]=1

    else:
    # veículo está na VERTICAL
        
        # Primeiramente, examina-se e modifica-se a vizinhança das extremidades
        if ((i==0) and (j==0)):     # encostado na quina superior esquerda
            # extremidade superior
            Tabuleiro[i][j+1][0]=1
            # extremidade inferior
            Tabuleiro[i+3][j+1][0]=1
            Tabuleiro[i+4][j][0]=1
            Tabuleiro[i+4][j+1][0]=1            
        elif ((i==0) and (j==14)):  # encostado na quina superior direita
            # extremidade superior
            Tabuleiro[i][j-1][0]=1
            # extremidade inferior
            Tabuleiro[i+3][j-1][0]=1
            Tabuleiro[i+4][j-1][0]=1
            Tabuleiro[i+4][j][0]=1            
        elif ((i==11) and (j==0)):  # encostado na quina inferior esquerda
            # extremidade superior
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j+1][0]=1            
            # extremidade inferior
            Tabuleiro[i+3][j+1][0]=1            
        elif ((i==11) and (j==14)): # encostado na quina inferior direita
            # extremidade superior
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i][j-1][0]=1            
            # extremidade inferior
            Tabuleiro[i+3][j-1][0]=1            
        elif (i==0):   # encostado na borda superior, mas não numa quina
            # extremidade superior
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            # extremidade inferior
            Tabuleiro[i+3][j-1][0]=1
            Tabuleiro[i+3][j+1][0]=1
            Tabuleiro[i+4][j-1][0]=1
            Tabuleiro[i+4][j][0]=1
            Tabuleiro[i+4][j+1][0]=1                        
        elif (i==11):  # encostado na borda inferior, mas não numa quina
            # extremidade superior
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1            
            # extremidade inferior
            Tabuleiro[i+3][j-1][0]=1
            Tabuleiro[i+3][j+1][0]=1                        
        elif (j==0):   # encostado na borda esquerda, mas não numa quina
            # extremidade superior
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j+1][0]=1            
            # extremidade inferior
            Tabuleiro[i+3][j+1][0]=1
            Tabuleiro[i+4][j][0]=1
            Tabuleiro[i+4][j+1][0]=1            
        elif (j==14):  # encostado na borda direita, mas não numa quina
            # extremidade superior
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i][j-1][0]=1            
            # extremidade inferior
            Tabuleiro[i+3][j-1][0]=1
            Tabuleiro[i+4][j-1][0]=1
            Tabuleiro[i+4][j][0]=1                        
        else:          # não encosta em nenhuma borda    
            # extremidade superior
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1            
            # extremidade inferior
            Tabuleiro[i+3][j-1][0]=1
            Tabuleiro[i+3][j+1][0]=1
            Tabuleiro[i+4][j-1][0]=1
            Tabuleiro[i+4][j][0]=1
            Tabuleiro[i+4][j+1][0]=1            

        # modifica-se a vizinhança da parte "interna" do Encouraçado, isto é,
        # das posições localizadas entre as extremidades.
        for lin in range(i+1, i+3):
            if (j!=0):  # não está encostando na borda esquerda
                Tabuleiro[lin][j-1][0]=1
            if (j!=14): # não está encostando na borda direita
                Tabuleiro[lin][j+1][0]=1       
   
    # Atribui-se as posições do Encouraçado propriamente dito:
    # orientacao horizontal
    if (orientacao==0):
        for col in range(j, j+4):
            Tabuleiro[i][col][0]=2   # veículo intacto
            Tabuleiro[i][col][2]=4   # Encouraçado
    # orientacao vertical
    else:
        for lin in range(i, i+4):
            Tabuleiro[lin][j][0]=2   # veículo intacto
            Tabuleiro[lin][j][2]=4   # Encouraçado     

    return(Tabuleiro)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#24: Insere um cruzador no tabuleiro. O autor desta função reconhece que tomou o
# caminho mais estúpido e trabalhoso para implementar a mesma, mas no frigir dos
# ovos o que conta é que ela funciona. Pare de me julgar. - Inforzato
def InserirCruzador(Tabuleiro, i, j, orientacao):
    # (i,j) é a primeira posição de uma peça que ocupa duas posições
    # orientação = 0 ---> horizonal (as posições são contadas da esquerda pra direita)
    # orientação = 1 ---> vertical  (as posições são contadas de cima pra baixo)

    # veiculo esta na HORIZONTAL
    if (orientacao==0):
        
        # marca-se as posições adjacentes ao veículo
        if ((i==0) and (j==0)):     # encostado na quina superior esquerda
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+1][j+1][0]=1
            Tabuleiro[i+1][j+2][0]=1
            Tabuleiro[i][j+2][0]=1            
        elif ((i==0) and (j==13)):  # encostado na quina superior direita
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+1][j+1][0]=1            
        elif ((i==14) and (j==0)):  # encostado na quina inferior esquerda
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i-1][j+2][0]=1
            Tabuleiro[i][j+2][0]=1            
        elif ((i==14) and (j==13)): # encostado na quina inferior direita
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1            
        elif (i==0):   # encostado na borda superior, mas não numa quina
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+1][j+1][0]=1
            Tabuleiro[i+1][j+2][0]=1
            Tabuleiro[i][j+2][0]=1            
        elif (i==14):  # encostado na borda inferior, mas não numa quina
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i-1][j+2][0]=1
            Tabuleiro[i][j+2][0]=1                    
        elif (j==0):   # encostado na borda esquerda, mas não numa quina
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i+1][j+1][0]=1
            Tabuleiro[i-1][j+2][0]=1
            Tabuleiro[i][j+2][0]=1
            Tabuleiro[i+1][j+2][0]=1          
        elif (j==13):  # encostado na borda direita, mas não numa quina
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i+1][j+1][0]=1            
        else:          # não encosta em nenhuma borda
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i+1][j+1][0]=1
            Tabuleiro[i-1][j+2][0]=1
            Tabuleiro[i][j+2][0]=1
            Tabuleiro[i+1][j+2][0]=1
            
    # veículo está na VERTICAL
    else:

        # marca-se as posições adjacentes ao veículo
        if ((i==0) and (j==0)):     # encostado na quina superior esquerda
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+1][j+1][0]=1
            Tabuleiro[i+2][j+1][0]=1
            Tabuleiro[i+2][j][0]=1            
        elif ((i==0) and (j==14)):  # encostado na quina superior direita
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+2][j-1][0]=1
            Tabuleiro[i+2][j][0]=1                        
        elif ((i==13) and (j==0)):  # encostado na quina inferior esquerda
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+1][j+1][0]=1            
        elif ((i==13) and (j==14)): # encostado na quina inferior direita
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1            
        elif (i==0):   # encostado na borda superior, mas não numa quina
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+1][j+1][0]=1
            Tabuleiro[i+2][j-1][0]=1
            Tabuleiro[i+2][j][0]=1
            Tabuleiro[i+2][j+1][0]=1            
        elif (i==13):  # encostado na borda inferior, mas não numa quina
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+1][j+1][0]=1                    
        elif (j==0):   # encostado na borda esquerda, mas não numa quina
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+1][j+1][0]=1
            Tabuleiro[i+2][j][0]=1
            Tabuleiro[i+2][j+1][0]=1
        elif (j==14):  # encostado na borda direita, mas não numa quina
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+2][j-1][0]=1
            Tabuleiro[i+2][j][0]=1            
        else:          # não está encostado em nenhuma borda
            Tabuleiro[i-1][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+1][j-1][0]=1
            Tabuleiro[i+1][j+1][0]=1
            Tabuleiro[i+2][j-1][0]=1
            Tabuleiro[i+2][j][0]=1
            Tabuleiro[i+2][j+1][0]=1

    # Atribuimos as posições do Cruzador propriamente dito:
    # orientacao horizontal
    if (orientacao==0):
        Tabuleiro[i][j][0]=2         # veículo intacto
        Tabuleiro[i][j+1][0]=2
        Tabuleiro[i][j][2]=2         # Cruzador
        Tabuleiro[i][j+1][2]=2
    # orientação vertical
    else:
        Tabuleiro[i][j][0]=2         # veículo intacto
        Tabuleiro[i+1][j][0]=2
        Tabuleiro[i][j][2]=2         # Cruzador
        Tabuleiro[i+1][j][2]=2     

    return(Tabuleiro)
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#25: Insere um hidroavião no tabuleiro. O autor desta função reconhece que tomou o
# caminho mais estúpido e trabalhoso para implementar a mesma, mas no frigir dos
# ovos o que conta é que ela funciona. Pare de me julgar. - Inforzato
def InserirHidroaviao(Tabuleiro, i, j, orientacao):
    # (i,j) é a posição do nariz do hidroavião
    # orientação = 0 ---> nariz para cima
    # orientação = 1 ---> nariz para a direita
    # orientação = 2 ---> nariz para baixo
    # orientação = 3 ---> nariz para a esquerda

    # atribuição das posições adjacentes ao veículo:
    # nariz do hidroaviao para CIMA:
    if (orientacao==0):
        if ((i==0) and (j==1)):     # encostado na quina superior esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i][j+2][0]=1
            Tabuleiro[i+1][j+2][0]=1        
            for col in range(j-1,j+3):
                Tabuleiro[i+2][col][0]=1                    
        elif ((i==0) and (j==13)):  # encostado na quina superior direita
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i][j-2][0]=1
            Tabuleiro[i+1][j-2][0]=1
            Tabuleiro[i+1][j][0]=1            
            for col in range(j-2,j+2):
                Tabuleiro[i+2][col][0]=1                
        elif ((i==13) and (j==1)):  # encostado na quina inferior esquerda
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+1][j+2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i][j+2][0]=1
            for col in range(j-1,j+2):
                Tabuleiro[i-1][col][0]=1 
        elif ((i==13) and (j==13)): # encostado na quina inferior direita
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+1][j-2][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j-2][0]=1
            for col in range(j-1,j+2):
                Tabuleiro[i-1][col][0]=1            
        elif (i==0):    # encostado na borda superior, mas não numa quina
            for col in range(j-2,j+3):
                if (col!=j):
                    Tabuleiro[i][col][0]=1
            for col in range(j-2,j+3,2):
                Tabuleiro[i+1][col][0]=1
            for col in range(j-2,j+3):
                Tabuleiro[i+2][col][0]=1            
        elif (i==13):   # encostado na borda inferior, mas não numa quina
            for col in range(j-1,j+2):
                Tabuleiro[i-1][col][0]=1
            for col in range(j-2,j+3):
                if (col!=j):
                    Tabuleiro[i][col][0]=1
            for col in range(j-2,j+3,2):
                Tabuleiro[i+1][col][0]=1            
        elif (j==1):    # encostado na borda esquerda, mas não numa quina
            for col in range(j-1,j+2):
                Tabuleiro[i-1][col][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i][j+2][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+1][j+2][0]=1
            for col in range(j-1,j+3):
                Tabuleiro[i+2][col][0]=1            
        elif (j==13):   # encostado na borda direita, mas não numa quina
            for col in range(j-1,j+2):
                Tabuleiro[i-1][col][0]=1
            Tabuleiro[i][j-2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+1][j-2][0]=1
            Tabuleiro[i+1][j][0]=1
            for col in range(j-2,j+2):
                Tabuleiro[i+2][col][0]=1            
        else:           # não encosta em nenhuma borda
            for col in range(j-1,j+2):
                Tabuleiro[i-1][col][0]=1
            for col in range(j-2,j+3):
                if (col!=j):
                    Tabuleiro[i][col][0]=1
            for col in range(j-2,j+3,2):
                Tabuleiro[i+1][col][0]=1
            for col in range(j-2,j+3):
                Tabuleiro[i+2][col][0]=1

    # nariz do hidroaviao para a DIREITA:
    elif (orientacao==1):
        if ((i==1) and (j==1)):     # encostado na quina superior esquerda
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+2][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+2][j][0]=1
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j+1][0]=1            
        elif ((i==1) and (j==14)):  # encostado na quina superior direita
            for lin in range(i-1,i+3):
                Tabuleiro[lin][j-2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+2][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+2][j][0]=1
        elif ((i==13) and (j==1)):  # encostado na quina inferior esquerda
            Tabuleiro[i-2][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i-2][j][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j+1][0]=1                
        elif ((i==13) and (j==14)): # encostado na quina inferior direita
            for lin in range(i-2,i+2):
                Tabuleiro[lin][j-2][0]=1
            Tabuleiro[i-2][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i-2][j][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1            
        elif (i==1):    # encostado na borda superior, mas não numa quina
            for lin in range(i-1,i+3):
                Tabuleiro[lin][j-2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i+2][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+2][j][0]=1
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j+1][0]=1            
        elif (i==13):   # encostado na borda inferior, mas não numa quina
            for lin in range(i-2,i+2):
                Tabuleiro[lin][j-2][0]=1
            Tabuleiro[i-2][j-1][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i-2][j][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j+1][0]=1            
        elif (j==1):    # encostado na borda esquerda, mas não numa quina
            for lin in range(i-2,i+3,2):
                Tabuleiro[lin][j-1][0]=1
            for lin in range(i-2,i+3):
                if (lin!=i):
                    Tabuleiro[lin][j][0]=1
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j+1][0]=1            
        elif (j==14):   # encostado na borda direita, mas não numa quina
            for lin in range(i-2,i+3):
                Tabuleiro[lin][j-2][0]=1
            for lin in range(i-2,i+3,2):
                Tabuleiro[lin][j-1][0]=1
            for lin in range(i-2,i+3):
                if (lin!=i):
                    Tabuleiro[lin][j][0]=1
        else:           # não encosta em nenhuma borda
            for lin in range(i-2,i+3):
                Tabuleiro[lin][j-2][0]=1
            for lin in range(i-2,i+3,2):
                Tabuleiro[lin][j-1][0]=1
            for lin in range(i-2,i+3):
                if (lin!=i):
                    Tabuleiro[lin][j][0]=1
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j+1][0]=1                    

    # nariz do hidroaviao para BAIXO:
    elif (orientacao==2):
        if ((i==1) and (j==1)):     # encostado na quina superior esquerda
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i][j+2][0]=1
            for col in range(j-1,j+2):
                Tabuleiro[i+1][col][0]=1            
        elif ((i==1) and (j==13)):  # encostado na quina superior direita
            Tabuleiro[i-1][j-2][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i][j-2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            for col in range(j-1,j+2):
                Tabuleiro[i+1][col][0]=1                
        elif ((i==14) and (j==1)):  # encostado na quina inferior esquerda
            for col in range(j-1,j+3):
                Tabuleiro[i-2][col][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i][j+2][0]=1                
        elif ((i==14) and (j==13)): # encostado na quina inferior direita
            for col in range(j-2,j+2):
                Tabuleiro[i-2][col][0]=1
            Tabuleiro[i-1][j-2][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i][j-2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1            
        elif (i==1):    # encostado na borda superior, mas não numa quina
            for col in range(j-2,j+3,2):
                Tabuleiro[i-1][col][0]=1
            for col in range(j-2,j+3):
                if (col!=j):
                    Tabuleiro[i][col][0]=1
            for col in range(j-1,j+2):
                Tabuleiro[i+1][col][0]=1            
        elif (i==14):   # encostado na borda inferior, mas não numa quina
            for col in range(j-2,j+3):
                Tabuleiro[i-2][col][0]=1
            for col in range(j-2,j+3,2):
                Tabuleiro[i-1][col][0]=1
            for col in range(j-2,j+3):
                if (col!=j):
                    Tabuleiro[i][col][0]=1            
        elif (j==1):    # encostado na borda esquerda, mas não numa quina
            for col in range(j-1,j+3):
                Tabuleiro[i-2][col][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i-1][j+2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i][j+2][0]=1
            for col in range(j-1,j+2):
                Tabuleiro[i+1][col][0]=1            
        elif (j==13):   # encostado na borda direita, mas não numa quina
            for col in range(j-2,j+2):
                Tabuleiro[i-2][col][0]=1
            Tabuleiro[i-1][j-2][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i][j-2][0]=1
            Tabuleiro[i][j-1][0]=1
            Tabuleiro[i][j+1][0]=1
            for col in range(j-1,j+2):
                Tabuleiro[i+1][col][0]=1
        else:           # não encosta em nenhuma borda
            for col in range(j-2,j+3):
                Tabuleiro[i-2][col][0]=1
            for col in range(j-2,j+3,2):
                Tabuleiro[i-1][col][0]=1
            for col in range(j-2,j+3):
                if (col!=j):
                    Tabuleiro[i][col][0]=1
            for col in range(j-1,j+2):
                Tabuleiro[i+1][col][0]=1

    # nariz do hidroaviao para a ESQUERDA:
    else:
        if ((i==1) and (j==0)):     # encostado na quina superior esquerda
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+2][j][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+2][j+1][0]=1
            for lin in range(i-1,i+3):
                Tabuleiro[lin][j+2][0]=1            
        elif ((i==1) and (j==13)):  # encostado na quina superior direita
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+2][j][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+2][j+1][0]=1                
        elif ((i==13) and (j==0)):  # encostado na quina inferior esquerda
            Tabuleiro[i-2][j][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i-2][j+1][0]=1
            Tabuleiro[i][j+1][0]=1
            for lin in range(i-2,i+2):
                Tabuleiro[lin][j+2][0]=1                
        elif ((i==13) and (j==13)): # encostado na quina inferior direita
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j-1][0]=1
            Tabuleiro[i-2][j][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i-2][j+1][0]=1
            Tabuleiro[i][j+1][0]=1            
        elif (i==1):    # encostado na borda superior, mas não numa quina
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j-1][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i+2][j][0]=1
            Tabuleiro[i][j+1][0]=1
            Tabuleiro[i+2][j+1][0]=1
            for lin in range(i-1,i+3):
                Tabuleiro[lin][j+2][0]=1            
        elif (i==13):   # encostado na borda inferior, mas não numa quina
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j-1][0]=1
            Tabuleiro[i-2][j][0]=1
            Tabuleiro[i-1][j][0]=1
            Tabuleiro[i+1][j][0]=1
            Tabuleiro[i-2][j+1][0]=1
            Tabuleiro[i][j+1][0]=1
            for lin in range(i-2,i+2):
                Tabuleiro[lin][j+2][0]=1            
        elif (j==0):    # encostado na borda esquerda, mas não numa quina
            for lin in range(i-2,i+3):
                if (lin!=i):
                    Tabuleiro[lin][j][0]=1
            for lin in range(i-2,i+3,2):
                Tabuleiro[lin][j+1][0]=1
            for lin in range(i-2,i+3):
                Tabuleiro[lin][j+2][0]=1            
        elif (j==13):   # encostado na borda direita, mas não numa quina
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j-1][0]=1
            for lin in range(i-2,i+3):
                if (lin!=i):
                    Tabuleiro[lin][j][0]=1
            for lin in range(i-2,i+3,2):
                Tabuleiro[lin][j+1][0]=1
        else:           # não encosta em nenhuma borda
            for lin in range(i-1,i+2):
                Tabuleiro[lin][j-1][0]=1
            for lin in range(i-2,i+3):
                if (lin!=i):
                    Tabuleiro[lin][j][0]=1
            for lin in range(i-2,i+3,2):
                Tabuleiro[lin][j+1][0]=1
            for lin in range(i-2,i+3):
                Tabuleiro[lin][j+2][0]=1
    
    # Atribuição das posições do hidroavião propriamente dito:
    # nariz do hidroaviao para CIMA:
    if (orientacao==0):
        Tabuleiro[i][j][0]=2      # [i][j][0]=2 ---> Veículo intacto
        Tabuleiro[i+1][j-1][0]=2
        Tabuleiro[i+1][j+1][0]=2
        Tabuleiro[i][j][2]=3      # [i][j][2]=3 ---> Hidroavião
        Tabuleiro[i+1][j-1][2]=3
        Tabuleiro[i+1][j+1][2]=3
    # nariz do hidroaviao para a DIREITA:
    elif (orientacao==1):
        Tabuleiro[i][j][0]=2
        Tabuleiro[i-1][j-1][0]=2
        Tabuleiro[i+1][j-1][0]=2
        Tabuleiro[i][j][2]=3
        Tabuleiro[i-1][j-1][2]=3
        Tabuleiro[i+1][j-1][2]=3
    # nariz do hidroaviao para BAIXO:
    elif (orientacao==2):
        Tabuleiro[i][j][0]=2
        Tabuleiro[i-1][j-1][0]=2
        Tabuleiro[i-1][j+1][0]=2
        Tabuleiro[i][j][2]=3
        Tabuleiro[i-1][j-1][2]=3
        Tabuleiro[i-1][j+1][2]=3
    # nariz do hidroaviao para a ESQUERDA:
    else:
        Tabuleiro[i][j][0]=2
        Tabuleiro[i-1][j+1][0]=2
        Tabuleiro[i+1][j+1][0]=2
        Tabuleiro[i][j][2]=3
        Tabuleiro[i-1][j+1][2]=3
        Tabuleiro[i+1][j+1][2]=3
    
    return(Tabuleiro)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#26: Insere um submarino no tabuleiro. O autor desta função reconhece que tomou o
# caminho mais estúpido e trabalhoso para implementar a mesma, mas no frigir dos
# ovos o que conta é que ela funciona. Pare de me julgar. - Inforzato
def InserirSubmarino(Tabuleiro, i, j):

    # primeiro marcamos as posições adjacentes ao veículo
    if ((i==0) and (j==0)):     # encostado na quina superior esquerda
        Tabuleiro[i][j+1][0]=1
        Tabuleiro[i+1][j][0]=1
        Tabuleiro[i+1][j+1][0]=1    
    elif ((i==0) and (j==14)):  # encostado na quina superior direita
        Tabuleiro[i][j-1][0]=1
        Tabuleiro[i+1][j-1][0]=1
        Tabuleiro[i+1][j][0]=1    
    elif ((i==14) and (j==0)):  # encostado na quina inferior esquerda
        Tabuleiro[i-1][j][0]=1
        Tabuleiro[i-1][j+1][0]=1
        Tabuleiro[i][j+1][0]=1    
    elif ((i==14) and (j==14)): # encostado na quina inferior direita
        Tabuleiro[i-1][j-1][0]=1
        Tabuleiro[i-1][j][0]=1
        Tabuleiro[i][j-1][0]=1    
    elif (i==0):   # encostado na borda superior, mas não numa quina
        Tabuleiro[i][j-1][0]=1
        Tabuleiro[i][j+1][0]=1
        Tabuleiro[i+1][j-1][0]=1
        Tabuleiro[i+1][j][0]=1
        Tabuleiro[i+1][j+1][0]=1
    elif (i==14):  # encostado na borda inferior, mas não numa quina
        Tabuleiro[i-1][j-1][0]=1
        Tabuleiro[i-1][j][0]=1
        Tabuleiro[i-1][j+1][0]=1
        Tabuleiro[i][j-1][0]=1
        Tabuleiro[i][j+1][0]=1    
    elif (j==0):   # encostado na borda esquerda, mas não numa quina
        Tabuleiro[i-1][j][0]=1
        Tabuleiro[i+1][j][0]=1
        Tabuleiro[i-1][j+1][0]=1
        Tabuleiro[i][j+1][0]=1
        Tabuleiro[i+1][j+1][0]=1    
    elif (j==14):  # encostado na borda direita, mas não numa quina
        Tabuleiro[i-1][j][0]=1
        Tabuleiro[i+1][j][0]=1
        Tabuleiro[i-1][j-1][0]=1
        Tabuleiro[i][j-1][0]=1
        Tabuleiro[i+1][j-1][0]=1    
    else:          # não encosta em nenhuma borda
        Tabuleiro[i-1][j-1][0]=1
        Tabuleiro[i-1][j][0]=1
        Tabuleiro[i-1][j+1][0]=1
        Tabuleiro[i][j-1][0]=1
        Tabuleiro[i][j+1][0]=1
        Tabuleiro[i+1][j-1][0]=1
        Tabuleiro[i+1][j][0]=1
        Tabuleiro[i+1][j+1][0]=1  

    # Atribuimos a posição ao Submarino propriamente dito:
    Tabuleiro[i][j][0]=2    # veículo intacto
    Tabuleiro[i][j][2]=1    # submarino

    return(Tabuleiro)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#27: Preenche automaticamente o tabuleiro do jogador. Para você que é preguiçoso(a). De nada.
def AutoPreencherTabJog():

    global TabJog

    # Apaga o tabuleiro, para o caso dele ter sido preenchido anteriormente
    ResetTotalTabJog()

    n_PortaAvioesRestantes=1 # para teste ---> 6
    n_EncouracadosRestantes=2 # para teste ---> 4
    n_CruzadoresRestantes=3
    n_HidroavioesRestantes=3
    n_SumbarinosRestantes=4

    n_PecasRestantes=13 # para teste ---> 20

    aux_i=0
    aux_j=0
    aux_pos=0

    while (n_PecasRestantes!=0):
        aux_i=random.randint(0,14)
        aux_j=random.randint(0,14)
        if (n_PortaAvioesRestantes!=0):
            aux_pos=random.randint(0,1)
            if PosicaoPortaAvioesValida(TabJog,aux_i,aux_j,aux_pos):
                InserirPortaAvioes(TabJog,aux_i,aux_j,aux_pos)
                n_PortaAvioesRestantes-=1
                n_PecasRestantes-=1
        elif (n_HidroavioesRestantes!=0):
            aux_pos=random.randint(0,3)
            if PosicaoHidroaviaoValida(TabJog,aux_i,aux_j,aux_pos):
                InserirHidroaviao(TabJog,aux_i,aux_j,aux_pos)
                n_HidroavioesRestantes-=1
                n_PecasRestantes-=1
        elif (n_EncouracadosRestantes!=0):
            aux_pos=random.randint(0,1)
            if PosicaoEncouracadoValida(TabJog,aux_i,aux_j,aux_pos):
                InserirEncouracado(TabJog,aux_i,aux_j,aux_pos)
                n_EncouracadosRestantes-=1
                n_PecasRestantes-=1
        elif (n_CruzadoresRestantes!=0):
            aux_pos=random.randint(0,1)
            if PosicaoCruzadorValida(TabJog,aux_i,aux_j,aux_pos):
                InserirCruzador(TabJog,aux_i,aux_j,aux_pos)
                n_CruzadoresRestantes-=1
                n_PecasRestantes-=1
        elif (n_SumbarinosRestantes!=0):
            if PosicaoSubmarinoValida(TabJog,aux_i,aux_j):
                InserirSubmarino(TabJog,aux_i,aux_j)
                n_SumbarinosRestantes-=1
                n_PecasRestantes-=1
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#28: Preenche automaticamente o tabuleiro do computador. Porque ele é uma besta e não consegue sozinho.
def AutoPreencherTabComp():

    global TabComp

    # Apaga o tabuleiro, para o caso dele ter sido preenchido anteriormente
    ResetTotalTabComp()

    n_PortaAvioesRestantes=1
    n_EncouracadosRestantes=2
    n_CruzadoresRestantes=3
    n_HidroavioesRestantes=3
    n_SumbarinosRestantes=4

    n_PecasRestantes=13

    aux_i=0
    aux_j=0
    aux_pos=0

    while (n_PecasRestantes!=0):
        aux_i=random.randint(0,14)
        aux_j=random.randint(0,14)
        if (n_PortaAvioesRestantes!=0):
            aux_pos=random.randint(0,1)
            if PosicaoPortaAvioesValida(TabComp,aux_i,aux_j,aux_pos):
                InserirPortaAvioes(TabComp,aux_i,aux_j,aux_pos)
                n_PortaAvioesRestantes-=1
                n_PecasRestantes-=1
        elif (n_HidroavioesRestantes!=0):
            aux_pos=random.randint(0,3)
            if PosicaoHidroaviaoValida(TabComp,aux_i,aux_j,aux_pos):
                InserirHidroaviao(TabComp,aux_i,aux_j,aux_pos)
                n_HidroavioesRestantes-=1
                n_PecasRestantes-=1
        elif (n_EncouracadosRestantes!=0):
            aux_pos=random.randint(0,1)
            if PosicaoEncouracadoValida(TabComp,aux_i,aux_j,aux_pos):
                InserirEncouracado(TabComp,aux_i,aux_j,aux_pos)
                n_EncouracadosRestantes-=1
                n_PecasRestantes-=1
        elif (n_CruzadoresRestantes!=0):
            aux_pos=random.randint(0,1)
            if PosicaoCruzadorValida(TabComp,aux_i,aux_j,aux_pos):
                InserirCruzador(TabComp,aux_i,aux_j,aux_pos)
                n_CruzadoresRestantes-=1
                n_PecasRestantes-=1
        elif (n_SumbarinosRestantes!=0):
            if PosicaoSubmarinoValida(TabComp,aux_i,aux_j):
                InserirSubmarino(TabComp,aux_i,aux_j)
                n_SumbarinosRestantes-=1
                n_PecasRestantes-=1
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#29: Função que conta o número de partes de veículo adjacentes a uma posição (i,j)
# Essa função foi desenvolvida unicamente para resolver o problema de converter X em A,
# quando um veículo é afundado. 
def NAdj(Tabuleiro,i,j):

   cont=0

   if (i!=0): # checa as posições superiores
      if (Tabuleiro[i-1][j][0]>1):        # posição Norte
         cont+=1
      if (j!=0):
         if (Tabuleiro[i-1][j-1][0]>1):   # posição Noroeste
            cont+=1
      if (j!=14):
         if (Tabuleiro[i-1][j+1][0]>1):   # posição Nordeste
            cont+=1
   if (i!=14): #checa as posições inferiores
      if (Tabuleiro[i+1][j][0]>1):        # posição Sul
         cont+=1
      if (j!=0):
         if (Tabuleiro[i+1][j-1][0]>1):   # posição Sudoeste
            cont+=1
      if (j!=14):
         if (Tabuleiro[i+1][j+1][0]>1):   # posição Sudeste
            cont+=1
   # checa as posições laterais
   if (j!=0):                             # posição Oeste
      if (Tabuleiro[i][j-1][0]>1):
         cont+=1
   if (j!=14):                            # posição Leste
      if (Tabuleiro[i][j+1][0]>1):
         cont+=1

   return(cont)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#30: Ataca uma posição do porta-aviões e avalia se ele foi destruído, modificando o
#    tabuleiro de acordo caso isso seja verificado.
def AtingirPortaAvioes(Tabuleiro,i,j):

   Tabuleiro[i][j][1]=1  # posição (i,j) recebe o flag de "já atacada"
   Tabuleiro[i][j][0]=3  # posição (i,j) recebe o flag de "veículo danificado"

   # assume-se que o veiculo está na posição vertical
   Vertical=True

   # testa-se se o veiculo está realmente na posição vertical, mudando caso necessário
   if (NAdj(Tabuleiro,i,j)==1): # proa ou popa
      if (i==0):     # encostado na borda superior
         if (Tabuleiro[i+1][j][0]==1):
            Vertical=False
      elif (i==14):  # encostado na borda inferior
         if (Tabuleiro[i-1][j][0]==1):
            Vertical=False
      else:          # não encostado em nenhuma borda
         if ((Tabuleiro[i-1][j][0]==1) and (Tabuleiro[i+1][j][0]==1)):
            Vertical=False
   else:                        # parte interna do corpo do porta-aviões (2 adjacências)
      if ((i==0) or (i==14)):   # encostado na borda superior ou inferior
         Vertical=False
      else:
         if (Tabuleiro[i-1][j][0]==1):
            Vertical=False

   # variáveis auxiliares para identificar as extremidades do porta-aviões:
   # a proa é o começo e a popa é o fim. (esquerda pra direita, cima pra baixo)
   proa_i=-1
   proa_j=-1
   popa_i=-1
   popa_j=-1

   # OBS: Quase uma semana depois de implementar essa função, eu me dou conta de que
   # só precisávamos da posição da proa e da orientação, e as variáveis popa_i e popa_j
   # são desnecessárias. Se der tempo, vou optimizar a função, mas isso não está no topo
   # da lista de prioridades, já que a função funciona do jeito que está. (Alexandre)

   # veículo na vertical
   if (Vertical==True):
      if (NAdj(Tabuleiro,i,j)==1):       # (i,j) é proa ou popa.
         if (i==0):                      # (i,j) é proa, encostada na borda superior do tabuleiro.
            proa_i=i
            popa_i=i+4            
         elif (Tabuleiro[i-1][j][0]==1): # (i,j) é proa, pois a posição (i-1,j) é vazia.
            proa_i=i            
            popa_i=i+4            
         else:                           # (i,j) é popa, pois a posição (i-1,j) não é vazia.
            proa_i=i-4            
            popa_i=i            
      elif (NAdj(Tabuleiro,i-1,j)==1):   # (i,j) está adjacente à proa.
         proa_i=i-1         
         popa_i=i+3         
      elif (NAdj(Tabuleiro,i+1,j)==1):   # (i,j) está adjacente à popa.
         proa_i=i-3         
         popa_i=i+1         
      else:                              # (i,j) é o meio do porta-aviões.
         proa_i=i-2         
         popa_i=i+2         

   # veículo na horizontal
   else:
      if (NAdj(Tabuleiro,i,j)==1):       # (i,j) é proa ou popa.
         if (j==0):                      # (i,j) é proa, encostada na borda esquerda do tabuleiro.            
            proa_j=j            
            popa_j=j+4
         elif (Tabuleiro[i][j-1][0]==1): # (i,j) é proa, pois a posição (i,j-1) é vazia.            
            proa_j=j            
            popa_j=j+4
         else:                           # (i,j) é popa, pois a posição (i,j-1) não é vazia.            
            proa_j=j-4            
            popa_j=j
      elif (NAdj(Tabuleiro,i,j-1)==1):   # (i,j) está adjacente à proa.         
         proa_j=j-1         
         popa_j=j+3
      elif (NAdj(Tabuleiro,i,j+1)==1):   # (i,j) está adjacente à popa.         
         proa_j=j-3         
         popa_j=j+1
      else:                              # (i,j) é o meio do porta-aviões.         
         proa_j=j-2         
         popa_j=j+2

   # Agora sabemos exatamente as posições das extremidades do porta-aviões, e a sua orientação.
   # Basta verificarmos se todas as posições estão danificadas e, neste caso, o porta-aviões
   # será destruído (todas as suas posições receberão flag de "veículo destruído").

   # Começamos assumindo que todas as partes do veículo estão danificadas
   VeiculoDestruido=True

   # Testamos essa hipótese, alterando a variável "VeiculoDestruido" caso necessário:
   # Veículo na vertical
   if (Vertical==True):
      for lin in range(proa_i,popa_i+1):
         if (Tabuleiro[lin][j][0]==2): # posição intacta
            VeiculoDestruido=False
   # Veículo na horizontal
   else:
      for col in range(proa_j,popa_j+1):
         if (Tabuleiro[i][col][0]==2): # posição intacta
            VeiculoDestruido=False

   # Se nenhuma das posições estiver intacta, o veículo está destruído.
   if (VeiculoDestruido==True):
      # veículo na vertical
      if (Vertical==True):
         for lin in range(proa_i,popa_i+1):
            Tabuleiro[lin][j][0]=4 # [i][j][0]=4 ---> flag de veículo destruído
      # veículo na horizontal
      else:
         for col in range(proa_j,popa_j+1):
            Tabuleiro[i][col][0]=4 # [i][j][0]=4 ---> flag veículo destruído  
         
   return(Tabuleiro)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#    
#31: Ataca uma posição do encouraçado e avalia se ele foi destruído, modificando o
#    tabuleiro de acordo caso isso seja verificado.
def AtingirEncouracado(Tabuleiro,i,j):

   Tabuleiro[i][j][1]=1  # posição (i,j) recebe o flag de "já atacada"
   Tabuleiro[i][j][0]=3  # posição (i,j) recebe o flag de "veículo danificado"

   # assume-se que o veiculo está na posição vertical
   Vertical=True

   # testa-se se o veiculo está realmente na posição vertical, mudando o valor da variável caso necessário
   if (NAdj(Tabuleiro,i,j)==1): # proa ou popa
      if (i==0):     # encostado na borda superior
         if (Tabuleiro[i+1][j][0]==1):
            Vertical=False
      elif (i==14):  # encostado na borda inferior
         if (Tabuleiro[i-1][j][0]==1):
            Vertical=False
      else:          # não encostado em nenhuma borda
         if ((Tabuleiro[i-1][j][0]==1) and (Tabuleiro[i+1][j][0]==1)):
            Vertical=False
   else:                        # parte interna do corpo do encouraçado (2 adjacências)
      if ((i==0) or (i==14)):   # encostado na borda superior ou inferior
         Vertical=False
      else:
         if (Tabuleiro[i-1][j][0]==1):
            Vertical=False

   # variáveis auxiliares para identificar as extremidades do encouraçado:
   # a proa é o começo e a popa é o fim. (da esquerda pra direita, de cima pra baixo)
   proa_i=-1
   proa_j=-1
   popa_i=-1
   popa_j=-1

   # veículo na vertical
   if (Vertical==True):
      if (NAdj(Tabuleiro,i,j)==1):       # (i,j) é proa ou popa.
         if (i==0):                      # (i,j) é proa, encostada na borda superior do tabuleiro.
            proa_i=i
            popa_i=i+3            
         elif (Tabuleiro[i-1][j][0]==1): # (i,j) é proa, pois a posição (i-1,j) é vazia.
            proa_i=i            
            popa_i=i+3            
         else:                           # (i,j) é popa, pois a posição (i-1,j) não é vazia.
            proa_i=i-3            
            popa_i=i            
      elif (NAdj(Tabuleiro,i-1,j)==1):   # (i,j) está adjacente à proa.
         proa_i=i-1         
         popa_i=i+2         
      else:                              # (i,j) está adjacente à popa.
         proa_i=i-2         
         popa_i=i+1          

   # veículo na horizontal
   else:
      if (NAdj(Tabuleiro,i,j)==1):       # (i,j) é proa ou popa.
         if (j==0):                      # (i,j) é proa, encostada na borda esquerda do tabuleiro.            
            proa_j=j            
            popa_j=j+3
         elif (Tabuleiro[i][j-1][0]==1): # (i,j) é proa, pois a posição (i,j-1) é vazia.            
            proa_j=j            
            popa_j=j+3
         else:                           # (i,j) é popa, pois a posição (i,j-1) não é vazia.            
            proa_j=j-3            
            popa_j=j
      elif (NAdj(Tabuleiro,i,j-1)==1):   # (i,j) está adjacente à proa.         
         proa_j=j-1         
         popa_j=j+2
      else:                              # (i,j) está adjacente à popa.         
         proa_j=j-2         
         popa_j=j+1

   # Agora sabemos exatamente as posições das extremidades do encouraçado, e a sua orientação.
   # Basta verificarmos se todas as posições estão danificadas e, neste caso, o encouraçado
   # será destruído (todas as suas posições receberão flag de "veículo destruído").

   # Começamos assumindo que todas as partes do veículo estão danificadas
   VeiculoDestruido=True

   # Testamos essa hipótese, alterando a variável "VeiculoDestruido" caso necessário:
   # Veículo na vertical
   if (Vertical==True):
      for lin in range(proa_i,popa_i+1):
         if (Tabuleiro[lin][j][0]==2): # posição intacta
            VeiculoDestruido=False
   # Veículo na horizontal
   else:
      for col in range(proa_j,popa_j+1):
         if (Tabuleiro[i][col][0]==2): # posição intacta
            VeiculoDestruido=False

   # Se nenhuma das posições estiver intacta, o veículo está destruído.
   if (VeiculoDestruido==True):
      # veículo na vertical
      if (Vertical==True):
         for lin in range(proa_i,popa_i+1):
            Tabuleiro[lin][j][0]=4 # [i][j][0]=4 ---> flag de veículo destruído
      # veículo na horizontal
      else:
         for col in range(proa_j,popa_j+1):
            Tabuleiro[i][col][0]=4 # [i][j][0]=4 ---> flag veículo destruído  
         
   return(Tabuleiro)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#    
#32: Ataca uma posição do hidroavião e avalia se ele foi destruído, modificando o
#    tabuleiro de acordo caso isso seja verificado.

def AtingirHidroaviao(Tabuleiro,i,j):

   Tabuleiro[i][j][1]=1  # posição (i,j) recebe o flag de "já atacada"
   Tabuleiro[i][j][0]=3  # posição (i,j) recebe o flag de "veículo danificado"

   # variaveis auxiliares para determinar a posicao e orientacao do hidroaviao:
   i_nariz=-1
   j_nariz=-1
   orientacao=-1

   # (i,j) é NARIZ do hidroavião
   if (NAdj(Tabuleiro,i,j)==2):  
      i_nariz=i
      j_nariz=j
      if (i_nariz==0):      # nariz encostado na borda superior
         orientacao=0
      elif (j_nariz==14):   # nariz encostado na borda direita
         orientacao=1
      elif (i_nariz==14):   # nariz encostado na borda inferior
         orientacao=2
      elif (j_nariz==0):    # nariz encostado na borda esquerda
         orientacao=3
      elif ((Tabuleiro[i_nariz+1][j_nariz-1][0]>=2) and (Tabuleiro[i_nariz+1][j_nariz+1][0]>=2)):
         orientacao=0
      elif ((Tabuleiro[i_nariz-1][j_nariz-1][0]>=2) and (Tabuleiro[i_nariz+1][j_nariz-1][0]>=2)):
         orientacao=1
      elif ((Tabuleiro[i_nariz-1][j_nariz-1][0]>=2) and (Tabuleiro[i_nariz-1][j_nariz+1][0]>=2)):
         orientacao=2
      else:
         orientacao=3

   # (i,j) é ASA do hidroavião
   else:                           
      # primeiro obtemos as coordenadas do nariz do avião:
      if ((i==0) and (j==0)):     # (i,j) é a quina esquerda superior
         i_nariz=i+1
         j_nariz=j+1
      elif ((i==0) and (j==14)):  # (i,j) é a quina direita superior
         i_nariz=i+1
         j_nariz=j-1
      elif ((i==14) and (j==14)): # (i,j) é a quina direita inferior 
         i_nariz=i-1
         j_nariz=j-1
      elif ((i==14) and (j==0)):  # (i,j) é a quina esquerda inferior
         i_nariz=i-1
         j_nariz=j+1
      elif (i==0):                # (i,j) é adjacente à borda superior, mas não é quina
         i_nariz=i+1
         if (Tabuleiro[i+1][j-1][2]==3):
            j_nariz=j-1         
         else:
            j_nariz=j+1
      elif (j==14):               # (i,j) é adjacente à borda direita, mas não é quina
         j_nariz=j-1
         if (Tabuleiro[i-1][j-1][2]==3):
            i_nariz=i-1
         else:
            i_nariz=i+1
      elif (i==14):               # (i,j) é adjacente à borda inferior, mas não é quina
         i_nariz=i-1
         if (Tabuleiro[i-1][j-1][2]==3):
            j_nariz=j-1
         else:
            j_nariz=j+1
      elif (j==0):                # (i,j) é adjacente à borda esquerda, mas não é quina
         j_nariz=j+1
         if (Tabuleiro[i-1][j+1][2]==3):
            i_nariz=i-1
         else:
            i_nariz=i+1
      else:                       # (i,j) não é adjacente a nenhuma borda
         if (Tabuleiro[i-1][j-1][2]==3):
            i_nariz=i-1
            j_nariz=j-1
         elif (Tabuleiro[i-1][j+1][2]==3):
            i_nariz=i-1
            j_nariz=j+1
         elif (Tabuleiro[i+1][j+1][2]==3):
            i_nariz=i+1
            j_nariz=j+1
         else:
            i_nariz=i+1
            j_nariz=j-1

      # agora obtemos a orientação do avião:
      if (i_nariz==0):      # nariz encostado na borda superior
         orientacao=0
      elif (j_nariz==14):   # nariz encostado na borda direita
         orientacao=1
      elif (i_nariz==14):   # nariz encostado na borda inferior
         orientacao=2
      elif (j_nariz==0):    # nariz encostado na borda esquerda
         orientacao=3
      elif ((Tabuleiro[i_nariz+1][j_nariz-1][0]>=2) and (Tabuleiro[i_nariz+1][j_nariz+1][0]>=2)):
         orientacao=0
      elif ((Tabuleiro[i_nariz-1][j_nariz-1][0]>=2) and (Tabuleiro[i_nariz+1][j_nariz-1][0]>=2)):
         orientacao=1
      elif ((Tabuleiro[i_nariz-1][j_nariz-1][0]>=2) and (Tabuleiro[i_nariz-1][j_nariz+1][0]>=2)):
         orientacao=2
      else:
         orientacao=3

   # Agora sabemos a posição do nariz do hidroavião e a sua orientação.
   # Basta verificarmos se todas as posições estão danificadas e, neste caso, o hidroavião
   # será destruído (todas as suas posições receberão flag de "veículo destruído").

   # Começamos assumindo que todas as partes do veículo estão danificadas
   VeiculoDestruido=True

   # nariz para cima
   if (orientacao==0):
      if ((Tabuleiro[i_nariz][j_nariz][0]==2) or (Tabuleiro[i_nariz+1][j_nariz-1][0]==2) or (Tabuleiro[i_nariz+1][j_nariz+1][0]==2)):
         VeiculoDestruido=False
   # nariz para a direita
   elif (orientacao==1):
      if ((Tabuleiro[i_nariz][j_nariz][0]==2) or (Tabuleiro[i_nariz-1][j_nariz-1][0]==2) or (Tabuleiro[i_nariz+1][j_nariz-1][0]==2)):
         VeiculoDestruido=False
   # nariz para baixo
   elif (orientacao==2):
      if ((Tabuleiro[i_nariz][j_nariz][0]==2) or (Tabuleiro[i_nariz-1][j_nariz-1][0]==2) or (Tabuleiro[i_nariz-1][j_nariz+1][0]==2)):
         VeiculoDestruido=False
   # nariz para a esquerda
   else:
      if ((Tabuleiro[i_nariz][j_nariz][0]==2) or (Tabuleiro[i_nariz-1][j_nariz+1][0]==2) or (Tabuleiro[i_nariz+1][j_nariz+1][0]==2)):
         VeiculoDestruido=False
            
   # Se nenhuma das posições estiver intacta, o veículo está destruído.
   if (VeiculoDestruido==True):
      # nariz para cima
      if (orientacao==0):
         Tabuleiro[i_nariz][j_nariz][0]=4       # [i][j][0]=4 ---> flag de "veículo destruído"
         Tabuleiro[i_nariz+1][j_nariz-1][0]=4
         Tabuleiro[i_nariz+1][j_nariz+1][0]=4
      # nariz para a direita
      elif (orientacao==1):
         Tabuleiro[i_nariz][j_nariz][0]=4
         Tabuleiro[i_nariz-1][j_nariz-1][0]=4
         Tabuleiro[i_nariz+1][j_nariz-1][0]=4
      # nariz para baixo
      elif (orientacao==2):
         Tabuleiro[i_nariz][j_nariz][0]=4
         Tabuleiro[i_nariz-1][j_nariz-1][0]=4
         Tabuleiro[i_nariz-1][j_nariz+1][0]=4
      # nariz para a esquerda
      else:
         Tabuleiro[i_nariz][j_nariz][0]=4
         Tabuleiro[i_nariz-1][j_nariz+1][0]=4
         Tabuleiro[i_nariz+1][j_nariz+1][0]=4

   return Tabuleiro

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#  
#33: Ataca uma posição do cruzador e avalia se ele foi destruído, modificando o
#    tabuleiro de acordo, caso isso seja verificado.

def AtingirCruzador(Tabuleiro,i,j):
   
   Tabuleiro[i][j][1]=1  # posição (i,j) recebe o flag de "já atacada"
   Tabuleiro[i][j][0]=3  # posição (i,j) recebe o flag de "veículo danificado"

   # assume-se que o veiculo está na posição vertical
   Vertical=True

   # testa-se se o veiculo está realmente na posição vertical, mudando o valor da variável caso necessário
   if (j==0):                       # se (i,j) está encostada na lateral esquerda
      if (Tabuleiro[i][j+1][2]==2): # se a posição (i,j+1) corresponde a um cruzador
         Vertical=False
   elif (j==14):                    # se (i,j) está encostada na lateral direita
      if (Tabuleiro[i][j-1][2]==2): # se a posição (i,j-1) corresponde a um cruzador
         Vertical=False
   else:                            # se (i,j) não está encostada em nenhuma lateral
      if ((Tabuleiro[i][j-1][2]==2) or (Tabuleiro[i][j+1][2]==2)):
         Vertical=False
      
   # variáveis auxiliares para identificar a posição inicial do cruzador (proa),
   # contando da esquerda pra direita, de cima pra baixo.
   proa_i=-1
   proa_j=-1

   # veículo na vertical
   if (Vertical==True):
      if (i==0):                      # (i,j) encostado na borda superior do tabuleiro
         proa_i=i
         proa_j=j
      elif (i==14):                   # (i,j) encostado na borda inferior do tabuleiro
         proa_i=i-1
         proa_j=j
      elif (Tabuleiro[i+1][j][2]==2): # se (i+1,j) for parte do cruzador
         proa_i=i
         proa_j=j
      else:
         proa_i=i-1
         proa_j=j

   # veículo na horizontal
   else:
      if (j==0):                      # (i,j) encostado na borda esquerda do tabuleiro
         proa_i=i
         proa_j=j
      elif (j==14):                   # (i,j) encostado na borda direita do tabuleiro
         proa_i=i
         proa_j=j-1
      elif (Tabuleiro[i][j+1][2]==2): # se (i,j+1) for parte do cruzador
         proa_i=i
         proa_j=j
      else:
         proa_i=i
         proa_j=j-1

   # Agora sabemos exatamente a posição inicial do cruzador e a sua orientação.
   # Basta verificarmos se todas as suas posições estão danificadas e, neste caso, o cruzador
   # será destruído (todas as suas posições receberão flag de "veículo destruído").

   # Começamos assumindo que todas as partes do veículo estão danificadas
   VeiculoDestruido=True

   # Testamos essa hipótese, alterando a variável "VeiculoDestruido" caso necessário:
   # Veículo na vertical
   if (Vertical==True):
      if ((Tabuleiro[proa_i][proa_j][0]==2) or (Tabuleiro[proa_i+1][proa_j][0]==2)):
         VeiculoDestruido=False
   # Veículo na horizontal
   else:
      if ((Tabuleiro[proa_i][proa_j][0]==2) or (Tabuleiro[proa_i][proa_j+1][0]==2)):
         VeiculoDestruido=False

   # Se nenhuma das posições estiver intacta, o veículo está destruído:
   if (VeiculoDestruido==True):
      # veículo na vertical
      if (Vertical==True):
         Tabuleiro[proa_i][proa_j][0]=4    # [i][j][0]=4 ---> flag veículo destruído
         Tabuleiro[proa_i+1][proa_j][0]=4
      # veículo na horizontal
      else:
         Tabuleiro[proa_i][proa_j][0]=4    # [i][j][0]=4 ---> flag veículo destruído
         Tabuleiro[proa_i][proa_j+1][0]=4
         
   return Tabuleiro

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#34: Ataca um submarino e modifica o status da sua posição para "destruído"
def AtingirSubmarino(Tabuleiro,i,j):
   
   Tabuleiro[i][j][1]=1  # posição (i,j) recebe o flag de "já atacada"
   Tabuleiro[i][j][0]=4  # posição (i,j) recebe o flag de "veículo destruído"

   return Tabuleiro

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#35: Ataca uma posicao que nao é ocupada por nenhum veículo.
def AtingirPosicaoVazia(Tabuleiro,i,j):

   Tabuleiro[i][j][1]=1  # posição (i,j) recebe o flag de "já atacada"   

   return Tabuleiro

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#36: Recebe coordenada informada pelo jogador, trata para pegar linha (i) e retorna
#    Se a coordenada informada for inválida, a função retorna -1 (coordenada inválida)
def PegaLinha(Coor):

   if len(Coor)==2:
      Linha=Coor[1]
      if Linha.isnumeric()==False:
         Linha=Coor[0]
         if Linha.isnumeric()==False:
            Linha=int(-1)
   elif len(Coor)==3 and Coor[0]!='0' and Coor[1]!='0':
      Linha=Coor[1:3]
      if Linha.isnumeric()==False:
         Linha=Coor[0:2]
         if Linha.isnumeric()==False:
            Linha=int(-1)
   else:
      Linha=int(-1)

   return int(Linha)-1

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#37: Recebe coordenada informada pelo jogador, trata para pegar coluna (j) e retorna o int correspondente
#    Se a coordenada informada for inválida, a função retorna @ (coordenada inválida)
def PegaColuna(Coor):
   if len(Coor)==2 and Coor[0]!='0':
      Coluna=Coor[0]
      if Coluna.isalpha()==False:
         Coluna=Coor[1]
         if Coluna.isalpha()==False:
            Coluna='@'
   elif len(Coor)==3:
      Coluna=Coor[0]
      if Coluna.isalpha()==False:
         Coluna=Coor[2]
         if Coluna.isalpha()==False:
               Coluna='@'
   else:
      Coluna='@'

   return ord(Coluna)-97

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#38: Recebe uma coordenada informada pelo jogador, envia a outras funções para tratamento, cria um vetor Coord e verifica
#    se os valores nele presentes correspondem a uma posição da matriz que representa o Tabuleiro.
#    NOTA: O vetor Coord representa uma coordenada. Ou seja, Coord[0]=i (linha), Coord[1]=j (coluna) e Coord[2]=o (orientação)
#    O vetor Coord criado a partir dessa função poderá ser utilizado tanto no Posicionamento quanto no Ataque
def PegaCoord(Coord):

   while True:
      Coor=input()
      Coor=Coor.lower()
      Coord.insert(0,PegaLinha(Coor))
      Coord.insert(1,PegaColuna(Coor))

      if (Coord[0]>=0 and Coord[0]<15) and (Coord[1]>=0 and Coord[1]<15):
         break

      print("Coordenada inválida! Digite novamente: ",end='')

   return Coord

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#   
#39: Obtém, trata e retorna a orientação para posicionamento de um Porta-aviões, Encouraçado ou Cruzador
def OrientacaoInsercao_PEC(TipoPeca):
   print("Escolha a orientação do %s. (V)ertical ou (H)orizontal? "%TipoPeca,end='')

   while True:
      Orientacao=input()
      Orientacao=Orientacao.lower()

      if Orientacao=='h':
         Orientacao=0
      elif Orientacao=='v':
         Orientacao=1
      else: #Orientação informada inválida
         Orientacao=4

      if Orientacao!=4:
         break

      print("Orientação inválida! Digite novamente: ", end='')

   return Orientacao

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#40: Obtém, trata e retorna a orientação para posicionamento de um Hidroavião
def OrientacaoInsercao_H():
   print("Escolha a orientação: (D)ireita, (E)squerda, para (C)ima ou para (B)aixo: ",end='')

   while True:
      Orientacao=input()
      Orientacao=Orientacao.lower()

      if Orientacao=='c':
         Orientacao=0
      elif Orientacao=='d':
         Orientacao=1
      elif Orientacao=='b':
         Orientacao=2
      elif Orientacao=='e':
         Orientacao=3
      else: #Orientação informada inválida
         Orientacao=4

      if Orientacao!=4:
         break

      print("Orientação inválida! Digite novamente: ", end='')

   return Orientacao

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#41: Constrói e retorna um vetor Coord que será usado no posicionamento de um Porta-aviões, Encouraçado ou Cruzador
def CoordInsercao_PEC(Coord,n_Peca,TipoPeca):
   if TipoPeca!='Porta-aviões':
      print("Informe onde deseja posicionar o seu %dº %s: "%(n_Peca,TipoPeca), end='')
   else:
      print("Informe onde deseja posicionar o seu %s: "%TipoPeca, end='')

   PegaCoord(Coord)
   Coord.insert(2,OrientacaoInsercao_PEC(TipoPeca))

   return Coord

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#42: Constrói e retorna um vetor Coord que será usado no posicionamento de um Hidroavião
def CoordInsercao_H(Coord,n_Peca):
   print("Informe onde deseja posicionar o seu %dº Hidroavião: "%n_Peca, end='')

   while True:
      Coord=PegaCoord(Coord)

      if (Coord[0]==0 and Coord[1]==0) or (Coord[0]==0 and Coord[1]==14) or (Coord[0]==14 and Coord[1]==14) or (Coord[0]==14 and Coord[1]==0):               
         print("É impossível posicionar um Hidroavião nessa posição! Informe outra: ", end='')
      else:
         break

   Coord.insert(2,OrientacaoInsercao_H())

   return Coord

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#43: Constrói e retorna um vetor Coord que será usado no posicionamento de um Submarino
def CoordInsercao_S(Coord,n_Peca):
   print("Informe onde deseja posicionar o seu %dº Submarino: "%n_Peca, end='')

   Coord=PegaCoord(Coord)

   return Coord

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#44: Preenche manualmente o Tabuleiro do Jogador.
def ManualPreencherTabJog():

   global TabJog

   # Apaga o tabuleiro, para o caso dele ter sido preenchido anteriormente
   ResetTotalTabJog()
   
   n_PortaAvioesRestantes=1
   n_EncouracadosRestantes=2
   n_CruzadoresRestantes=3
   n_HidroavioesRestantes=3
   n_SumbarinosRestantes=4

   n_PecasRestantes=13

   EscreverTabJog(Nome,Homem,TabJog)

   while (n_PecasRestantes!=0):

      Coord=[] #vetor auxiliar para coleta das coordenadas

      n_Peca=1
      while (n_PortaAvioesRestantes!=0):
         Coord=CoordInsercao_PEC(Coord,n_Peca,'Porta-aviões')
         if PosicaoPortaAvioesValida(TabJog,Coord[0],Coord[1],Coord[2]):
            InserirPortaAvioes(TabJog,Coord[0],Coord[1],Coord[2])
            n_PortaAvioesRestantes-=1
            n_PecasRestantes-=1
            EscreverTabJog(Nome,Homem,TabJog)
         else:
            print("Não é possível inserir um Porta-aviões nessa posição! ")
            print("Dica: Os veículos não podem ficar encostados ou sair do tabuleiro.")
            print()

      n_Peca=1
      while (n_HidroavioesRestantes!=0):
         Coord=CoordInsercao_H(Coord,n_Peca)
         if PosicaoHidroaviaoValida(TabJog,Coord[0],Coord[1],Coord[2]):
            InserirHidroaviao(TabJog,Coord[0],Coord[1],Coord[2])
            n_HidroavioesRestantes-=1
            n_PecasRestantes-=1
            n_Peca+=1
            EscreverTabJog(Nome,Homem,TabJog)
         else:
            print("Não é possível inserir um Hidroavião nessa posição! ")
            print("Dica: Os veículos não podem ficar encostados ou sair do tabuleiro.")
            print()
            
      n_Peca=1
      while (n_EncouracadosRestantes!=0):
         Coord=CoordInsercao_PEC(Coord,n_Peca,'Encouraçado')
         if PosicaoEncouracadoValida(TabJog,Coord[0],Coord[1],Coord[2]):
            InserirEncouracado(TabJog,Coord[0],Coord[1],Coord[2])
            n_EncouracadosRestantes-=1
            n_PecasRestantes-=1
            n_Peca+=1
            EscreverTabJog(Nome,Homem,TabJog)
         else:
            print("Não é possível inserir um Encouraçado nessa posição! ")
            print("Dica: Os veículos não podem ficar encostados ou sair do tabuleiro.")
            print()
            
      n_Peca=1
      while (n_CruzadoresRestantes!=0):
         Coord=CoordInsercao_PEC(Coord,n_Peca,'Cruzador')
         if PosicaoCruzadorValida(TabJog,Coord[0],Coord[1],Coord[2]):
            InserirCruzador(TabJog,Coord[0],Coord[1],Coord[2])
            n_CruzadoresRestantes-=1
            n_PecasRestantes-=1
            n_Peca+=1
            EscreverTabJog(Nome,Homem,TabJog)
         else:
            print("Não é possível inserir um Cruzador nessa posição! ")
            print("Dica: Os veículos não podem ficar encostados ou sair do tabuleiro.")
            print()

      n_Peca=1
      while (n_SumbarinosRestantes!=0):
         Coord=CoordInsercao_S(Coord,n_Peca)
         if PosicaoSubmarinoValida(TabJog,Coord[0],Coord[1]):
            InserirSubmarino(TabJog,Coord[0],Coord[1])
            n_SumbarinosRestantes-=1
            n_PecasRestantes-=1
            n_Peca+=1
            EscreverTabJog(Nome,Homem,TabJog)
         else:
            print("Não é possível inserir um Submarino nessa posição. ")
            print("Dica: Os veículos não podem ficar encostados ou sair do tabuleiro.")
            print()

   return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#45: Sub-menu para configuração do tabuleiro, antes do jogo.
def ConfigurarTabuleiro(Nome, Homem):
   global TabJog

   #laço principal
   while True:

      Escolha=0
      
      while True:

         print()
         print("1. Configurar tabuleiro manualmente.")
         print("2. Configuração automática de tabuleiro.")
         if Homem==True:
            print("3. Tô cansado. Deixa pra lá.")
         else:
            print("3. Tô cansada. Deixa pra lá.")
         print()
         print("Escolha: ", end="")

         Escolha=input()
   
         if ((len(Escolha)!=1) or (Escolha.isnumeric()==False)):
            print("Opção inválida! Tente novamente.")
         else:
            Escolha=int(Escolha)
            if (Escolha==1):
               ManualPreencherTabJog()
               print("Sensacional, ",Nome,"! Configuração manual concluída.", sep="")
               print("Aperte ENTER para continuar.", end="")
               input()
               return

            elif (Escolha==2):
               AutoPreencherTabJog()
               EscreverTabJog(Nome,Homem,TabJog)
               if Homem==True:
                  print("Pronto, meu lorde, configurei o tabuleiro pra você. Quer um suco também?")
               else:
                  print("Pronto, minha princesa, configurei o tabuleiro pra você. Preguicinha, né?")
               print("Aperte ENTER para continuar, pelo menos.", end="")
               input()
               return
            
            elif (Escolha==3):
               print("Vai dormir, então, sua lontra.")
               return

            else:
               if Homem==True:
                  print("Não, meu Precioso. Presta atenção nas opções...")
               else:
                  print("Não, minha Preciosa. Presta atenção nas opções...")
            
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#46: Verifica se um tabuleiro está vazio. Só para o caso de algum espertinho tentar
# começar a jogar sem antes configurar o tabuleiro. Sim, nós pensamos em tudo, pare de
# tentar quebrar o jogo. - Inforzato
def TabuleiroVazio(Tabuleiro):

   Vazio=True
   
   for lin in range(0,15):
      for col in range(0,15):
         if (Tabuleiro[lin][col][0]!=0):
            Vazio=False
            return Vazio

   return Vazio

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#47: Essa função imprime o tabuleiro auxiliar do computador durante a fase de combate.
#    Ela é destinada apenas para a realização de testes.
    
def EscreverTabJog4(TabCompAux):

    print()
    print("    Grid Auxiliar do Computador")
    print()
    print("   A B C D E F G H I J K L M N O")
    for i in range(0,15):
        # Este if só serve para justificar a coluna dos números,
        # uma vez que alguns números so tem 1 dígito e outros tem 2
        if (i<9):
            print("", i+1, end=" ")
        else:
            print(i+1, end=" ")
        
        for j in range (0,15):
            if (TabCompAux[i][j]==0):    # vazio e ainda não atacado
                print("- ", end="")
            elif (TabCompAux[i][j]==1):  # adjacente e ainda não atacado
                print("+ ", end="")
            elif (TabCompAux[i][j]==3):  # veículo danificado
                print("X ", end="")     
            elif (TabCompAux[i][j]==4):  # veículo destruído
                print("A ", end="")     
            else:                       # ERRO! Valor inválido em TabJog[i][j][0]
                print("E ", end="")

        print()
    print()
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#48: Detecta possíveis direções de ataque, fazendo parte de uma série de
#    procedimentos que visam ajudar o computador a fazer jogadas inteligentes.
def DetectarDirecoesPossiveis(TabJog,TabCompAux):

    global Smart1
   
    # Direções nas quais é possivel atacar
    # [N,NE,E,SE,S,SW,W,NW]
    # 0 --> impossível
    # 1 --> possível
    DirecoesPossiveis=[0,0,0,0,0,0,0,0]

    i=Smart1[0]
    j=Smart1[1]

    # (i,j) é quina superior esquerda
    if ((i==0) and (j==0)):
        if (TabJog[i][j+1][1]==0 and TabCompAux[i][j+1]==0):
            DirecoesPossiveis[2]=1
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveis[3]=1
        if (TabJog[i+1][j][1]==0 and TabCompAux[i+1][j]==0):
            DirecoesPossiveis[4]=1

    # (i,j) é quina superior direita
    elif ((i==0) and (j==14)):
        if (TabJog[i+1][j][1]==0 and TabCompAux[i+1][j]==0):
            DirecoesPossiveis[4]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveis[5]=1
        if (TabJog[i][j-1][1]==0 and TabCompAux[i][j-1]==0):
            DirecoesPossiveis[6]=1

    # (i,j) é quina inferior direita
    elif ((i==14) and (j==14)):
        if (TabJog[i-1][j][1]==0 and TabCompAux[i-1][j]==0):
            DirecoesPossiveis[0]=1
        if (TabJog[i][j-1][1]==0 and TabCompAux[i][j-1]==0):
            DirecoesPossiveis[6]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveis[7]=1

    # (i,j) é quina inferior esquerda
    elif ((i==14) and (j==0)):
        if (TabJog[i-1][j][1]==0 and TabCompAux[i-1][j]==0):
            DirecoesPossiveis[0]=1
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveis[1]=1
        if (TabJog[i][j+1][1]==0 and TabCompAux[i][j+1]==0):
            DirecoesPossiveis[2]=1

    # (i,j) está encostada na borda superior, mas não é quina
    elif (i==0):
        if (TabJog[i][j+1][1]==0 and TabCompAux[i][j+1]==0):
            DirecoesPossiveis[2]=1
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveis[3]=1
        if (TabJog[i+1][j][1]==0 and TabCompAux[i+1][j]==0):
            DirecoesPossiveis[4]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveis[5]=1
        if (TabJog[i][j-1][1]==0 and TabCompAux[i][j-1]==0):
            DirecoesPossiveis[6]=1

    # (i,j) está encostada na borda inferior, mas não é quina
    elif (i==14):
        if (TabJog[i-1][j][1]==0 and TabCompAux[i-1][j]==0):
            DirecoesPossiveis[0]=1
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveis[1]=1
        if (TabJog[i][j+1][1]==0 and TabCompAux[i][j+1]==0):
            DirecoesPossiveis[2]=1
        if (TabJog[i][j-1][1]==0 and TabCompAux[i][j-1]==0):
            DirecoesPossiveis[6]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveis[7]=1

    # (i,j) está encostada na borda direita, mas não é quina
    elif (j==14):
        if (TabJog[i-1][j][1]==0 and TabCompAux[i-1][j]==0):
            DirecoesPossiveis[0]=1
        if (TabJog[i+1][j][1]==0 and TabCompAux[i+1][j]==0):
            DirecoesPossiveis[4]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveis[5]=1
        if (TabJog[i][j-1][1]==0 and TabCompAux[i][j-1]==0):
            DirecoesPossiveis[6]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveis[7]=1

    # (i,j) está encostada na borda esquerda, mas não é quina
    elif (j==0):
        if (TabJog[i-1][j][1]==0 and TabCompAux[i-1][j]==0):
            DirecoesPossiveis[0]=1
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveis[1]=1
        if (TabJog[i][j+1][1]==0 and TabCompAux[i][j+1]==0):
            DirecoesPossiveis[2]=1
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveis[3]=1
        if (TabJog[i+1][j][1]==0 and TabCompAux[i+1][j]==0):
            DirecoesPossiveis[4]=1

    # (i,j) não encosta em nenhuma borda
    else:
        if (TabJog[i-1][j][1]==0 and TabCompAux[i-1][j]==0):
            DirecoesPossiveis[0]=1
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveis[1]=1
        if (TabJog[i][j+1][1]==0 and TabCompAux[i][j+1]==0):
            DirecoesPossiveis[2]=1
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveis[3]=1
        if (TabJog[i+1][j][1]==0 and TabCompAux[i+1][j]==0):
            DirecoesPossiveis[4]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveis[5]=1
        if (TabJog[i][j-1][1]==0 and TabCompAux[i][j-1]==0):
            DirecoesPossiveis[6]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveis[7]=1

    return DirecoesPossiveis

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#49: Fornece as coordenadas para a realização de um ataque com base nas coordenadas
#    de um ataque anterior bem-sucedido. 
def SmartAttack1(TabJog,TabCompAux):

    global Smart1

    # Vetor que vai ser retornado com a próxima posição a ser atacada
    AuxPos=[-1,-1]

    # auxiliares de referencia
    i=Smart1[0]
    j=Smart1[1]

    DirecoesPossiveis=[0,0,0,0,0,0,0,0]
    # Direções nas quais é possivel atacar
    # [N,NE,E,SE,S,SW,W,NW]
    # 0 --> impossível
    # 1 --> possível
    
    DirecoesPossiveis=DetectarDirecoesPossiveis(TabJog,TabCompAux)
    # Agora, não apenas temos as direções que PODEM ser atacadas, como podemos
    # contá-las e randomizar uma posição de ataque:

    # Número de posições que podem ser atacadas a partir de Smart1(i,j)
    NPosPossiveis=0
    
    for x in range(0,8):
        if DirecoesPossiveis[x]==1:
            NPosPossiveis+=1

    # Posição no vetor DirecoesPossiveis que representa a próxima jogada
    PosicaoEscolhida=(-1)

    # auxiliar para armazenar numero aleatorio
    aux_random=0
        
    # Das posições possíveis, escolhe-se uma aleatoriamente.
    # Notando que:   1<= NPosPossiveis <=8
    aux_random=random.randint(1,NPosPossiveis)
    for x in range(0,8):
        if (DirecoesPossiveis[x]!=0):
            aux_random-=1
            if (aux_random==0):
                PosicaoEscolhida=x

    # Atribui-se as posicoes escolhidas ao vetor de saída da função
    if (PosicaoEscolhida==0):
        AuxPos[0]=i-1
        AuxPos[1]=j
    elif (PosicaoEscolhida==1):
        AuxPos[0]=i-1
        AuxPos[1]=j+1
    elif (PosicaoEscolhida==2):
        AuxPos[0]=i
        AuxPos[1]=j+1
    elif (PosicaoEscolhida==3):
        AuxPos[0]=i+1
        AuxPos[1]=j+1
    elif (PosicaoEscolhida==4):
        AuxPos[0]=i+1
        AuxPos[1]=j
    elif (PosicaoEscolhida==5):
        AuxPos[0]=i+1
        AuxPos[1]=j-1
    elif (PosicaoEscolhida==6):
        AuxPos[0]=i
        AuxPos[1]=j-1
    elif (PosicaoEscolhida==7):
        AuxPos[0]=i-1
        AuxPos[1]=j-1
    else:
        print("ERRO NO CALCULO de PosicaoEscolhida!!!")

    return(AuxPos)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#    
#50: Manda as coordenadas de Smart1 para Smart2 e vice-versa.
def SwitchSmart():

    global Smart1
    global Smart2

    aux=[-1,-1]

    aux[0]=Smart1[0]
    aux[1]=Smart1[1]
    
    Smart1[0]=Smart2[0]
    Smart1[1]=Smart2[1]

    Smart2[0]=aux[0]
    Smart2[1]=aux[1]

    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#    
#51: Função auxiliar para a função SmartAttack2
#    Detecta Posições possíveis de ataque ao hidroavião quando Smart1 está acima de Smart2
def DetectarDirecoesHidroaviao1(TabJog,TabCompAux,Smart1):

    # Direções nas quais é possivel atacar:
    # aproximadamente [N,E,S,W], em relação a Smart1 
    # 0 --> impossível
    # 1 --> possível
    DirecoesPossiveisHidroaviao=[0,0,0,0]
    
    i=Smart1[0]
    j=Smart1[1]

    # hidroavião encosta na quina superior esquerda
    if ((i==0) and (j==0)):
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i+2][j][1]==0 and TabCompAux[i+2][j]==0):
            DirecoesPossiveisHidroaviao[2]=1            

    # hidroavião encosta na quina superior direita
    elif ((i==0) and (j==13)):
        if (TabJog[i+2][j][1]==0 and TabCompAux[i+2][j]==0):
            DirecoesPossiveisHidroaviao[2]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1        
        
    # hidroavião encosta na quina inferior direita
    elif ((i==13) and (j==13)):
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveisHidroaviao[4]=1        

    # hidroavião encosta na quina inferior esquerda
    elif ((i==13) and (j==0)):
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1            

    # hidroavião encosta na borda superior, mas não na quina
    elif (i==0):
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i+2][j][1]==0 and TabCompAux[i+2][j]==0):
            DirecoesPossiveisHidroaviao[2]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1            

    # hidroavião encosta na borda inferior, mas não na quina
    elif (i==14):
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1            

    # hidroavião encosta na borda direita, mas não na quina
    elif (j==0):
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i+2][j][1]==0 and TabCompAux[i+2][j]==0):
            DirecoesPossiveisHidroaviao[2]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1            

    # hidroavião encosta na borda esquerda, mas não na quina
    elif (j==14):
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i+2][j][1]==0 and TabCompAux[i+2][j]==0):
            DirecoesPossiveisHidroaviao[2]=1            

    # hidroavião não encosta em nenhuma borda
    else:
        if (TabJog[i-1][j+1][1]==0 and TabCompAux[i-1][j+1]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i+2][j][1]==0 and TabCompAux[i+2][j]==0):
            DirecoesPossiveisHidroaviao[2]=1
        if (TabJog[i+1][j-1][1]==0 and TabCompAux[i+1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1

    return DirecoesPossiveisHidroaviao

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#    
#52: Função auxiliar para a função SmartAttack2
#    Detecta Posições possíveis de ataque ao hidroavião quando Smart1 está abaixo de Smart2
def DetectarDirecoesHidroaviao2(TabJog,TabCompAux,Smart1):

    # Direções nas quais é possivel atacar:
    # aproximadamente [N,E,S,W], em relação a Smart1 
    # 0 --> impossível
    # 1 --> possível
    DirecoesPossiveisHidroaviao=[0,0,0,0]
    
    i=Smart1[0]
    j=Smart1[1]

    # hidroavião encosta na quina superior esquerda
    if ((i==1) and (j==0)):
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveisHidroaviao[2]=1

    # hidroavião encosta na quina superior direita
    elif ((i==1) and (j==13)):
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveisHidroaviao[2]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1
            
    # hidroavião encosta na quina inferior direita
    elif ((i==14) and (j==13)):
        if (TabJog[i-2][j][1]==0 and TabCompAux[i-2][j]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1

    # hidroavião encosta na quina inferior esquerda
    elif ((i==14) and (j==0)):
        if (TabJog[i-2][j][1]==0 and TabCompAux[i-2][j]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1

    # hidroavião encosta na borda superior, mas não na quina
    elif (i==1):
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveisHidroaviao[2]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1

    # hidroavião encosta na borda inferior, mas não na quina
    elif (i==14):
        if (TabJog[i-2][j][1]==0 and TabCompAux[i-2][j]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1

    # hidroavião encosta na borda direita, mas não na quina
    elif (j==0):
        if (TabJog[i-2][j][1]==0 and TabCompAux[i-2][j]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveisHidroaviao[2]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1

    # hidroavião encosta na borda esquerda, mas não na quina
    elif (j==13):
        if (TabJog[i-2][j][1]==0 and TabCompAux[i-2][j]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveisHidroaviao[2]=1

    # hidroavião não encosta em nenhuma borda
    else:
        if (TabJog[i-2][j][1]==0 and TabCompAux[i-2][j]==0):
            DirecoesPossiveisHidroaviao[0]=1
        if (TabJog[i][j+2][1]==0 and TabCompAux[i][j+2]==0):
            DirecoesPossiveisHidroaviao[1]=1
        if (TabJog[i+1][j+1][1]==0 and TabCompAux[i+1][j+1]==0):
            DirecoesPossiveisHidroaviao[2]=1
        if (TabJog[i-1][j-1][1]==0 and TabCompAux[i-1][j-1]==0):
            DirecoesPossiveisHidroaviao[3]=1

    return DirecoesPossiveisHidroaviao

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#    
#53: Fornece as coordenadas para a realização de um ataque com base nas coordenadas
#    de dois ataques anteriores bem-sucedidos. Esta função foi a principal causadora do
#    atraso no lançamento da versão 2.0 e no surgimento de sentimentos homicidas/suicidas
#    no coração do programador.

def SmartAttack2(TabJog,TabCompAux):

    global Smart1
    global Smart2
    
    # Vetor que vai ser retornado com a próxima posição a ser atacada
    AuxPos=[-1,-1]

    # auxiliares de posição de ataque possivel
    AuxPosCandidato1=[-1,-1]
    AuxPosCandidato2=[-1,-1]

    # Auxiliares de referencia
    i=Smart1[0]
    j=Smart1[1]
    i2=Smart2[0]
    j2=Smart2[1]

    # Se as coordenadas não estão na mesma linha e nem na mesma coluna...

    #=-=-=-=-=-=-=-=-=-=-  Início do Procedimento para Hidroavião -=-=-=-=-=-=-=-=-=-=#
    if ((i!=i2) and (j!=j2)):

        # Direções nas quais é possivel atacar:
        # aproximadamente [N,E,S,W], em relação a Smart1 
        # 0 --> impossível
        # 1 --> possível
        DirecoesPossiveisHidroaviao=[0,0,0,0]

        # Inverte Smart1 com Smart2 se Smart2 estiver à esquerda de Smart1
        if (j>j2):
            SwitchSmart()
            i=Smart1[0]
            j=Smart1[1]
            i2=Smart2[0]
            j2=Smart2[1]

        # Se Smart2 está numa posição inferior a Smart1
        if (i<i2):

            DirecoesPossiveisHidroaviao=DetectarDirecoesHidroaviao1(TabJog,TabCompAux,Smart1)

            # Número de posições que podem ser atacadas a partir de Smart1(i,j)
            NPosPossiveis=0
            
            for x in range(0,4):
                if DirecoesPossiveisHidroaviao[x]==1:
                    NPosPossiveis+=1

            # Posição no vetor DirecoesPossiveis que representa a próxima jogada
            PosicaoEscolhida=-1
            # auxiliar para armazenar numero aleatorio
            aux_random=0
                
            # Das posições possíveis, escolhe-se uma aleatoriamente.
            # Notando que:   1<= NPosPossiveis <=4
            aux_random=(random.randint(1,NPosPossiveis))
            for x in range(0,4):
                if (DirecoesPossiveisHidroaviao[x]!=0):
                    aux_random-=1
                    if (aux_random==0):
                        PosicaoEscolhida=x

            # Atribui-se as posicoes escolhidas ao vetor de saída da função
            if (PosicaoEscolhida==0):
                AuxPos[0]=i-1
                AuxPos[1]=j+1
            elif (PosicaoEscolhida==1):
                AuxPos[0]=i
                AuxPos[1]=j+2
            elif (PosicaoEscolhida==2):
                AuxPos[0]=i+2
                AuxPos[1]=j
            elif (PosicaoEscolhida==3):
                AuxPos[0]=i+1
                AuxPos[1]=j-1
            else:
                print("ERRO NO CALCULO de PosicaoEscolhida para Hidroavião1!")

            return(AuxPos)

        # Se Smart1 está numa posição inferior a Smart2
        elif (i>i2):

            DirecoesPossiveisHidroaviao=DetectarDirecoesHidroaviao2(TabJog,TabCompAux,Smart1)

            # Número de posições que podem ser atacadas a partir de Smart1(i,j)
            NPosPossiveis=0
            
            for x in range(0,len(DirecoesPossiveisHidroaviao)):
                if DirecoesPossiveisHidroaviao[x]==1:
                    NPosPossiveis+=1

            # Posição no vetor DirecoesPossiveis que representa a próxima jogada
            PosicaoEscolhida=-1
            # auxiliar para armazenar numero aleatorio
            aux_random=0
                
            # Das posições possíveis, escolhe-se uma aleatoriamente.
            # Notando que:   1<= NPosPossiveis <=4
            aux_random=(random.randint(1,NPosPossiveis))
            for x in range(0,4):
                if (DirecoesPossiveisHidroaviao[x]!=0):
                    aux_random-=1
                    if (aux_random==0):
                        PosicaoEscolhida=x

            # Atribui-se as posicoes escolhidas ao vetor de saída da função
            if (PosicaoEscolhida==0):
                AuxPos[0]=i-2
                AuxPos[1]=j
            elif (PosicaoEscolhida==1):
                AuxPos[0]=i
                AuxPos[1]=j+2
            elif (PosicaoEscolhida==2):
                AuxPos[0]=i+1
                AuxPos[1]=j+1
            elif (PosicaoEscolhida==3):
                AuxPos[0]=i-1
                AuxPos[1]=j-1
            else:
                print("ERRO NO CALCULO de PosicaoEscolhida para Hidroavião2.")

            return(AuxPos)

        else:
            print("ERRO em SmartAttack2, na parte correspondente ao hidroavião.")

    #=-=-=-=-=-=-=-=-=-=-  Fim do Procedimento para Hidroavião -=-=-=-=-=-=-=-=-=-=#

    # as coordenadas de Smart1 e Smart2 pertencem a um encouraçado ou porta-aviões:
    # (ou seja, se elas compartilham uma linha ou uma coluna)
    else:

        # Se o veículo esta na HORIZONAL...
        if (i==i2):

           AuxPosCandidato1[0]=i
           AuxPosCandidato2[0]=i

           if (j>j2):
              j_aux=j
              j=j2
              j2=j_aux

           if (j==0):
              if (TabCompAux[i][j2+1]!=3 and TabJog[i][j2+1][1]==0):
                 AuxPosCandidato2[1]=j2+1
              elif (TabCompAux[i][j2+2]!=3 and TabJog[i][j2+2][1]==0 and TabJog[i][j2+1][2]!=0):
                 AuxPosCandidato2[1]=j2+2
              elif (TabCompAux[i][j2+3]!=3 and TabJog[i][j2+3][1]==0 and TabJog[i][j2+2][2]!=0):
                 AuxPosCandidato2[1]=j2+3

           elif (j==1):
              if (TabCompAux[i][j-1]!=3 and TabJog[i][j-1][1]==0):
                 AuxPosCandidato1[1]=j-1

              if (TabCompAux[i][j2+1]!=3 and TabJog[i][j2+1][1]==0):
                 AuxPosCandidato2[1]=j2+1
              elif (TabCompAux[i][j2+2]!=3 and TabJog[i][j2+2][1]==0 and TabJog[i][j2+1][2]!=0):
                 AuxPosCandidato2[1]=j2+2
              elif (TabCompAux[i][j2+3]!=3 and TabJog[i][j2+3][1]==0 and TabJog[i][j2+2][2]!=0):
                 AuxPosCandidato2[1]=j2+3

           elif (j==2):
              if (TabCompAux[i][j-1]!=3 and TabJog[i][j-1][1]==0):
                 AuxPosCandidato1[1]=j-1
              elif (TabCompAux[i][j-2]!=3 and TabJog[i][j-2][1]==0 and TabJog[i][j-1][2]!=0):
                 AuxPosCandidato1[1]=j-2

              if (TabCompAux[i][j2+1]!=3 and TabJog[i][j2+1][1]==0):
                 AuxPosCandidato2[1]=j2+1
              elif (TabCompAux[i][j2+2]!=3 and TabJog[i][j2+2][1]==0 and TabJog[i][j2+1][2]!=0):
                 AuxPosCandidato2[1]=j2+2
              elif (TabCompAux[i][j2+3]!=3 and TabJog[i][j2+3][1]==0 and TabJog[i][j2+2][2]!=0):
                 AuxPosCandidato2[1]=j2+3

           elif (j2==14):
              if (TabCompAux[i][j-1]!=3 and TabJog[i][j-1][1]==0):
                 AuxPosCandidato1[1]=j-1
              elif (TabCompAux[i][j-2]!=3 and TabJog[i][j-2][1]==0 and TabJog[i][j-1][2]!=0):
                 AuxPosCandidato1[1]=j-2
              elif (TabCompAux[i][j-3]!=3 and TabJog[i][j-3][1]==0 and TabJog[i][j-2][2]!=0):
                 AuxPosCandidato1[1]=j-3

           elif (j2==13):
              if (TabCompAux[i][j-1]!=3 and TabJog[i][j-1][1]==0):
                 AuxPosCandidato1[1]=j-1
              elif (TabCompAux[i][j-2]!=3 and TabJog[i][j-2][1]==0 and TabJog[i][j-1][2]!=0):
                 AuxPosCandidato1[1]=j-2
              elif (TabCompAux[i][j-3]!=3 and TabJog[i][j-3][1]==0 and TabJog[i][j-2][2]!=0):
                 AuxPosCandidato1[1]=j-3

              if (TabCompAux[i][j2+1]!=3 and TabJog[j2+1][1]==0):
                 AuxPosCandidato2[1]=j2+1

           elif (j2==12):
              if (TabCompAux[i][j-1]!=3 and TabJog[i][j-1][1]==0):
                 AuxPosCandidato1[1]=j-1
              elif (TabCompAux[i][j-2]!=3 and TabJog[i][j-2][1]==0 and TabJog[i][j-1][2]!=0):
                 AuxPosCandidato1[1]=j-2
              elif (TabCompAux[i][j-3]!=3 and TabJog[i][j-3][1]==0 and TabJog[i][j-2][2]!=0):
                 AuxPosCandidato1[1]=j-3

              if (TabCompAux[i][j2+1]!=3 and TabJog[i][j2+1][1]==0):
                 AuxPosCandidato2[1]=j2+1
              elif (TabCompAux[i][j2+2]!=3 and TabJog[i][j2+2][1]==0 and TabJog[i][j2+1][2]!=0):
                 AuxPosCandidato2[1]=j2+2
              
           else:
              if (TabCompAux[i][j-1]!=3 and TabJog[i][j-1][1]==0):
                 AuxPosCandidato1[1]=j-1
              elif (TabCompAux[i][j-2]!=3 and TabJog[i][j-2][1]==0 and TabJog[i][j-1][2]!=0):
                 AuxPosCandidato1[1]=j-2
              elif (TabCompAux[i][j-3]!=3 and TabJog[i][j-3][1]==0 and TabJog[i][j-2][2]!=0):
                 AuxPosCandidato1[1]=j-3

              if (TabCompAux[i][j2+1]!=3 and TabJog[i][j2+1][1]==0):
                 AuxPosCandidato2[1]=j2+1
              elif (TabCompAux[i][j2+2]!=3 and TabJog[i][j2+2][1]==0 and TabJog[i][j2+1][2]!=0):
                 AuxPosCandidato2[1]=j2+2
              elif (TabCompAux[i][j2+3]!=3 and TabJog[i][j2+3][1]==0 and TabJog[i][j2+2][2]!=0):
                 AuxPosCandidato2[1]=j2+3

           if AuxPosCandidato1[1]==(-1):
              AuxPos=AuxPosCandidato2
              return(AuxPos)
           elif AuxPosCandidato2[1]==(-1):
              AuxPos=AuxPosCandidato1
              return(AuxPos)
           else:
              aux_random=random.randint(0,1)
              if aux_random==0:
                 AuxPos=AuxPosCandidato1
                 return(AuxPos)
              else:
                 AuxPos=AuxPosCandidato2
                 return(AuxPos)

        # Se o veículo está na VERTICAL...
        elif (j==j2):
           AuxPosCandidato1[1]=j
           AuxPosCandidato2[1]=j
           if (i>i2):
              i_aux=i
              i=i2
              i2=i_aux
            
           if (i==0):
              if (TabCompAux[i2+1][j]!=3 and TabJog[i2+1][j][1]==0):
                 AuxPosCandidato2[0]=i2+1
              elif (TabCompAux[i2+2][j]!=3 and TabJog[i2+2][j][1]==0 and TabJog[i2+1][j][2]!=0):
                 AuxPosCandidato2[0]=i2+2
              elif (TabCompAux[i2+3][j]!=3 and TabJog[i2+3][j][1]==0 and TabJog[i2+2][j][2]!=0):
                 AuxPosCandidato2[0]=i2+3
                 
           elif (i==1):
              if (TabCompAux[i-1][j]!=3 and TabJog[i-1][j][1]==0):
                 AuxPosCandidato1[0]=i-1
              
              if (TabCompAux[i2+1][j]!=3 and TabJog[i2+1][j][1]==0):
                 AuxPosCandidato2[0]=i2+1
              elif (TabCompAux[i2+2][j]!=3 and TabJog[i2+2][j][1]==0 and TabJog[i2+1][j][2]!=0):
                 AuxPosCandidato2[0]=i2+2
              elif (TabCompAux[i2+3][j]!=3 and TabJog[i2+3][j][1]==0 and TabJog[i2+2][j][2]!=0):
                 AuxPosCandidato2[0]=i2+3

           elif (i==2):
              if (TabCompAux[i-1][j]!=3 and TabJog[i-1][j][1]==0):
                 AuxPosCandidato1[0]=i-1
              elif (TabCompAux[i-2][j]!=3 and TabJog[i-2][j][1]==0 and TabJog[i-1][j][2]!=0):
                 AuxPosCandidato1[0]=i-2

              if (TabCompAux[i2+1][j]!=3 and TabJog[i2+1][j][1]==0):
                 AuxPosCandidato2[0]=i2+1
              elif (TabCompAux[i2+2][j]!=3 and TabJog[i2+2][j][1]==0 and TabJog[i2+1][j][2]!=0):
                 AuxPosCandidato2[0]=i2+2
              elif (TabCompAux[i2+3][j]!=3 and TabJog[i2+3][j][1]==0 and TabJog[i2+2][j][2]!=0):
                 AuxPosCandidato2[0]=i2+3

           elif (i2==14):
              if (TabCompAux[i-1][j]!=3 and TabJog[i-1][j][1]==0):
                 AuxPosCandidato1[0]=i-1
              elif (TabCompAux[i-2][j]!=3 and TabJog[i-2][j][1]==0 and TabJog[i-1][j][2]!=0):
                 AuxPosCandidato1[0]=i-2
              elif (TabCompAux[i-3][j]!=3 and TabJog[i-3][j][1]==0 and TabJog[i-2][j][2]!=0):
                 AuxPosCandidato1[0]=i-3

           elif (i2==13):
              if (TabCompAux[i-1][j]!=3 and TabJog[i-1][j][1]==0):
                 AuxPosCandidato1[0]=i-1
              elif (TabCompAux[i-2][j]!=3 and TabJog[i-2][j][1]==0 and TabJog[i-1][j][2]!=0):
                 AuxPosCandidato1[0]=i-2
              elif (TabCompAux[i-3][j]!=3 and TabJog[i-3][j][1]==0 and TabJog[i-2][j][2]!=0):
                 AuxPosCandidato1[0]=i-3

              if (TabCompAux[i2+1][j]!=3 and TabJog[i2+1][j][1]==0):
                 AuxPosCandidato2[0]=i2+1

           elif (i2==12):
              if (TabCompAux[i-1][j]!=3 and TabJog[i-1][j][1]==0):
                 AuxPosCandidato1[0]=i-1
              elif (TabCompAux[i-2][j]!=3 and TabJog[i-2][j][1]==0 and TabJog[i-1][j][2]!=0):
                 AuxPosCandidato1[0]=i-2
              elif (TabCompAux[i-3][j]!=3 and TabJog[i-3][j][1]==0 and TabJog[i-2][j][2]!=0):
                 AuxPosCandidato1[0]=i-3

              if (TabCompAux[i2+1][j]!=3 and TabJog[i2+1][j][1]==0):
                 AuxPosCandidato2[0]=i2+1
              elif (TabCompAux[i2+2][j]!=3 and TabJog[i2+2][j][1]==0 and TabJog[i2+1][j][2]!=0):
                 AuxPosCandidato2[0]=i2+2
              
           else:
              if (TabCompAux[i-1][j]!=3 and TabJog[i-1][j][1]==0):
                 AuxPosCandidato1[0]=i-1
              elif (TabCompAux[i-2][j]!=3 and TabJog[i-2][j][1]==0 and TabJog[i-1][j][2]!=0):
                 AuxPosCandidato1[0]=i-2
              elif (TabCompAux[i-3][j]!=3 and TabJog[i-3][j][1]==0 and TabJog[i-2][j][2]!=0):
                 AuxPosCandidato1[0]=i-3

              if (TabCompAux[i2+1][j]!=3 and TabJog[i2+1][j][1]==0):
                 AuxPosCandidato2[0]=i2+1
              elif (TabCompAux[i2+2][j]!=3 and TabJog[i2+2][j][1]==0 and TabJog[i2+1][j][2]!=0):
                 AuxPosCandidato2[0]=i2+2
              elif (TabCompAux[i2+3][j]!=3 and TabJog[i2+3][j][1]==0 and TabJog[i2+2][j][2]!=0):
                 AuxPosCandidato2[0]=i2+3

           if AuxPosCandidato1[0]==(-1):
              AuxPos=AuxPosCandidato2
              return(AuxPos)
           elif AuxPosCandidato2[0]==(-1):
              AuxPos=AuxPosCandidato1
              return(AuxPos)
           else:
              aux_random=random.randint(0,1)
              if aux_random==0:
                 AuxPos=AuxPosCandidato1
                 return(AuxPos)
              else:
                 AuxPos=AuxPosCandidato2
                 return(AuxPos)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#            
#54: Rotina de combate. 
def ForfeAquatico(Nome,Homem,Trapaca):

   global TabJog
   global TabComp

   # Configuração automática do Tabuleiro do Computador
   AutoPreencherTabComp() 

   aux_i=-1 # variável auxiliar de linha
   aux_j=-1 # variável auxiliar de coluna

   Turno=1 # variável auxiliar que vai decidir de quem é o turno atual
           # se Turno==1, é a vez do jogador. Se Turno==(-1), é a vez do computador.

   CompVeiculosRestantes=13
   JogVeiculosRestantes=13

   # inicialização da Matriz auxiliar para que o computador não seja tão burro.
   # A idéia é que essa lista guarde as posições dos veículos destruídos, bem como suas
   # posições adjacentes, para que o computador não as ataque.
   TabCompAux = [[0 for j in range (0,15)] for i in range(0,15)]

   # Variáveis que vão ajudar o computador a ser menos burro.
   # A idéia é analisar posições quando o computador acertou um ou dois hits, e atacar posições
   # estratégicas a partir delas.
   global Smart1
   global Smart2

   print()
   print("O FORFÉ está para começar, ",Nome,"!! PREPARE-SE!!", sep="")
   if Trapaca:
      EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
   else:
      EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
   
   GameOver=False
   while (GameOver==False):

      if (Turno==1):

         #=-=-=-=-=-=-=-=-=- INÍCIO DO TURNO DO JOGADOR -=-=-=-=-=-=-=-=-=#

         print()
         print("Este turno é seu, ",Nome,".", sep="")

         #=-=-=- início de coleta e checagem de coordenadas -=-=-=#
         while True:

            Coord=[] # vetor auxiliar para coleta das coordenadas de ataque

            print("Informe a próxima posição a ser atacada: ", end="")
            Coord=PegaCoord(Coord)
            print()

            aux_i=Coord[0]
            aux_j=Coord[1]

            if (TabComp[aux_i][aux_j][1]==1):
               print("Essa já foi, ",Nome,". Escolhe outro lugar pra atacar! ", sep="")
            else:
               break               
         #=-=-=- fim de coleta e checagem de coordenadas -=-=-=#

         # jogador ataca posição vazia
         if (TabComp[aux_i][aux_j][2]==0):
            TabComp=AtingirPosicaoVazia(TabComp,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            print("ÁGUA! Não atingiu nada, ", Nome,"! Melhor sorte na próxima.", sep="")
            print("Pressione ENTER para prosseguir.", end="")
            input()            

         # jogador ataca e destrói um submarino
         elif (TabComp[aux_i][aux_j][2]==1):
            TabComp=AtingirSubmarino(TabComp,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            print("PUTA SORTE, ",Nome,"! Destruiu um submarino inimigo!", sep="")
            CompVeiculosRestantes-=1

         # jogador ataca um cruzador
         elif (TabComp[aux_i][aux_j][2]==2):
            TabComp=AtingirCruzador(TabComp,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            if (TabComp[aux_i][aux_j][0]==3):
               print("Você danificou um veículo adversário, ", Nome,"! Prega fogo no miserável!", sep="")
            elif (TabComp[aux_i][aux_j][0]==4):
               print("Um cruzador inimigo foi pro colo do Capirôto! Antes eles do que a gente.")
               CompVeiculosRestantes-=1

         # jogador ataca um hidroavião
         elif (TabComp[aux_i][aux_j][2]==3):
            TabComp=AtingirHidroaviao(TabComp,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            if (TabComp[aux_i][aux_j][0]==3):
               print("Você danificou um veículo adversário, ", Nome,"! Prega fogo no miserável!", sep="")
            elif (TabComp[aux_i][aux_j][0]==4):
               print("Boa, ",Nome,"! Destruiu um hidroavião do outro lado!!", sep="")
               CompVeiculosRestantes-=1

         # jogador ataca um encouraçado
         elif (TabComp[aux_i][aux_j][2]==4):
            TabComp=AtingirEncouracado(TabComp,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            if (TabComp[aux_i][aux_j][0]==3):
               print("Você danificou um veículo adversário, ", Nome,"! Prega fogo no miserável!", sep="")
            elif (TabComp[aux_i][aux_j][0]==4):
               print("Afundou um encouraçado do inimigo, ",Nome,"! Bênza Deus!", sep="")
               CompVeiculosRestantes-=1

         # jogador ataca um porta-aviões
         elif (TabComp[aux_i][aux_j][2]==5):
            TabComp=AtingirPortaAvioes(TabComp,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            if (TabComp[aux_i][aux_j][0]==3):
               print("Você danificou um veículo adversário, ", Nome,"! Prega fogo no miserável!", sep="")
            elif (TabComp[aux_i][aux_j][0]==4):
               print("Dá-lhe, ",Nome,"! Aniquilou o porta-aviões inimigo!", sep="")
               CompVeiculosRestantes-=1

         #=-=-=-=-=-=-=-=-=- FINAL DO TURNO DO JOGADOR -=-=-=-=-=-=-=-=-=#

      else:

         #=-=-=-=-=-=-=-=- INÍCIO DO TURNO DO COMPUTADOR -=-=-=-=-=-=-=-=#

         print()
         print("O computador realiza um ataque!")

         #=-=-=- Começo da Implementação da I.A. -=-=-=#

         # Se não houver NENHUM HIT registrado, o computador atira a esmo:   
         if (Smart1[0]==-1):
            while True:
               #Coord=[] # vetor auxiliar para armazenar as coordenadas de ataque
               aux_i=random.randint(0,14)
               aux_j=random.randint(0,14)
               # se a posição (i,j) ainda não foi atacada E não é adjacente a um veículo destruído
               if ((TabJog[aux_i][aux_j][1]==0) and (TabCompAux[aux_i][aux_j]!=1)):
                  break

         # Se houver apenas UM HIT registrado:
         elif (Smart2[0]==-1):
            Aux=[-1,-1]
            Aux=SmartAttack1(TabJog,TabCompAux)
            aux_i=Aux[0]
            aux_j=Aux[1]

         # Se houver DOIS HITS registrados:
         else:
            Aux=[-1,-1]
            # Ataca com base nas coordenadas de Smart1 e Smart2:
            Aux=SmartAttack2(TabJog,TabCompAux)
            aux_i=Aux[0]
            aux_j=Aux[1]
            
         #=-=-=- Final da Implementação da I.A. -=-=-=#

         # O computador ataca posição vazia
         if (TabJog[aux_i][aux_j][2]==0):
            TabJog=AtingirPosicaoVazia(TabJog,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            if (TabJog[aux_i][aux_j][0]==0):
               print("Pff computador vesgolino. Errou feio!")
            elif (TabJog[aux_i][aux_j][0]==1):
               print("EITA! Essa foi por pouco! O computador quase acertou um dos seus veículos!")

         # O computador ataca e destrói um submarino
         elif (TabJog[aux_i][aux_j][2]==1):
            TabJog=AtingirSubmarino(TabJog,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            print("O inimigo destruiu um dos seus submarinos!")
            JogVeiculosRestantes-=1
            print("Pressione ENTER para prosseguir.", end="")
            input()

         # O computador ataca um cruzador
         elif (TabJog[aux_i][aux_j][2]==2):
            TabJog=AtingirCruzador(TabJog,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            if (TabJog[aux_i][aux_j][0]==3):
               print("Alerta! Um cruzador aliado foi atingido!")
            elif (TabJog[aux_i][aux_j][0]==4):
               print("Um cruzador aliado foi destruído!")
               JogVeiculosRestantes-=1
            print("Pressione ENTER para prosseguir.", end="")
            input()

         # O computador ataca um hidroavião
         elif (TabJog[aux_i][aux_j][2]==3):
            TabJog=AtingirHidroaviao(TabJog,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            if (TabJog[aux_i][aux_j][0]==3):
               print("Alerta! Um hidroavião aliado foi atingido!")
            elif (TabJog[aux_i][aux_j][0]==4):
               print("Um hidroavião aliado foi pelos ares!")
               JogVeiculosRestantes-=1
            print("Pressione ENTER para prosseguir.", end="")
            input()

         # O computador ataca um encouraçado
         elif (TabJog[aux_i][aux_j][2]==4):
            TabJog=AtingirEncouracado(TabJog,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            if (TabJog[aux_i][aux_j][0]==3):
               print("Alerta! Um encouraçado aliado foi atingido!")
            elif (TabJog[aux_i][aux_j][0]==4):
               print("Um encouraçado aliado foi aniquilado!")
               JogVeiculosRestantes-=1
            print("Pressione ENTER para prosseguir.", end="")
            input()

         # O computador ataca um porta-aviões
         elif (TabJog[aux_i][aux_j][2]==5):
            TabJog=AtingirPortaAvioes(TabJog,aux_i,aux_j)
            if Trapaca:
               EscreverTabuleirosTrapaca(Nome, Homem, TabJog, TabComp)
            else:
               EscreverTabuleiros(Nome, Homem, TabJog, TabComp)
            if (TabJog[aux_i][aux_j][0]==3):
               print("Alerta geral! O porta-aviões aliado foi atingido!")
            elif (TabJog[aux_i][aux_j][0]==4):
               print("Desastre! O porta-aviões aliado foi destruído!")
               JogVeiculosRestantes-=1
            print("Pressione ENTER para prosseguir.", end="")
            input()

         #=-=-=-=-=-=-=-=- FINAL DO TURNO DO COMPUTADOR -=-=-=-=-=-=-=-=#

      #=-=-=-=-=-=-=-=-= INÍCIO DO TURNO DE MANUTENÇÃO =-=-=-=-=-=-=-=-=#

      # Se o número de veículos de qualquer lado atingir zero, o jogo acaba!
      # Se todos os veículos do computador foram destruídos...
      if (CompVeiculosRestantes==0):
         GameOver=True
      # Se todos os veículos do jogador foram destruídos...
      elif (JogVeiculosRestantes==0):
         GameOver=True

      else:
         # Se o último turno foi do jogador...
         if (Turno==1):
            # Se um veículo do computador acabou de ser destruído...
            if (TabComp[aux_i][aux_j][0]==4):
               print("Atencão! Recebemos a mensagem de um agente infiltrado:")
               if (CompVeiculosRestantes==1):
                  print("'CORAGEM! O inimigo só tem mais UM veículo no campo de batalha!'")
               elif (CompVeiculosRestantes==2):
                  print("'O inimigo está em desespero! Possui apenas dois veículos restantes!'")
               elif (CompVeiculosRestantes==3):
                  print("'As forças do inimigo sofreram graves baixas. Restam apenas três veículos!'")
               else:
                  print("'O inimigo ainda possui ", CompVeiculosRestantes," veículos no campo de batalha!'", sep="")
         # Se o último turno foi do computador...
         else:
            # Se um veículo do jogador acabou de ser danificado...
            if (TabJog[aux_i][aux_j][0]==3):
               TabCompAux[aux_i][aux_j]=3
               # Se não existe nenhum hit registrado, e esse hit foi ocasionado por um tiro a esmo...
               if (Smart1[0]==(-1)):
                  # Registra essa posição em Smart1
                  Smart1[0]=aux_i     
                  Smart1[1]=aux_j
               # Se só existe um hit registrado, e Smart2 está "vazio"...
               elif ((Smart1[0]!=(-1)) and (Smart2[0]==(-1))):
                  # Registra essa posição em Smart2
                  Smart2[0]=aux_i
                  Smart2[1]=aux_j

            # Se um veículo do jogador acabou de ser destruído, atualiza-se TabCompAux:
            elif (TabJog[aux_i][aux_j][0]==4):
               # Abandona-se os dois vetores auxiliares como guias para a próxima jogada
               Smart1[0]=-1
               Smart1[1]=-1
               Smart2[0]=-1
               Smart2[1]=-1
               # Atualiza-se a posição dos veículos destruídos para TabCompAux:
               for lin in range(0,15):
                  for col in range(0,15):
                     if (TabJog[lin][col][0]==4):
                        TabCompAux[lin][col]=4
               # Atribuem-se as devidas adjacências
               for lin in range(0,15):
                  for col in range(0,15):
                     # Se a posição (aux_i,aux_j) corresponde a um veículo destruído...
                     if (TabCompAux[lin][col]==4):
                        if (lin!=0): # checa as posições superiores
                           if (TabCompAux[lin-1][col]==0):        # posição Norte
                              TabCompAux[lin-1][col]=1            # [i][j][0]=1 --> flag de "adjacente"
                           if (col!=0):
                              if (TabCompAux[lin-1][col-1]==0):   # posição Noroeste
                                 TabCompAux[lin-1][col-1]=1
                           if (col!=14):
                              if (TabCompAux[lin-1][col+1]==0):   # posição Nordeste
                                 TabCompAux[lin-1][col+1]=1
                        if (lin!=14): #checa as posições inferiores
                           if (TabCompAux[lin+1][col]==0):        # posição Sul
                              TabCompAux[lin+1][col]=1
                           if (col!=0):
                              if (TabCompAux[lin+1][col-1]==0):   # posição Sudoeste
                                 TabCompAux[lin+1][col-1]=1
                           if (col!=14):
                              if (TabCompAux[lin+1][col+1]==0):   # posição Sudeste
                                 TabCompAux[lin+1][col+1]=1
                        # checa as posições laterais
                        if (col!=0):                                 # posição Oeste
                           if (TabCompAux[lin][col-1]==0):
                              TabCompAux[lin][col-1]=1
                        if (col!=14):                                # posição Leste
                           if (TabCompAux[lin][col+1]==0):
                              TabCompAux[lin][col+1]=1


      # Atualização de turno:
      # Se o turno foi do jogador
      if (Turno==1):
         # Se ele atingiu uma posição vazia
         if (TabComp[aux_i][aux_j][0]<=1):
            # Próximo turno é do computador
            Turno=Turno*(-1)
      # Se o turno foi do computador
      else:
         # Se ele atingiu uma posição vazia
         if (TabJog[aux_i][aux_j][0]<=1):
            # Próximo turno é do jogador
            Turno=Turno*(-1)

      #=-=-=-=-=-=-=-=-= FINAL DO TURNO DE MANUTENÇÃO =-=-=-=-=-=-=-=-=#

   # FIM DO COMBATE
   
   # Se o jogador perdeu:
   if (JogVeiculosRestantes==0):

      print("O forfé chegou ao fim, ", Nome,", e você perdeu.", sep="")
      print()
      print("            PER. DEU.")
      print()
      print("░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░")
      print("░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░") 
      print("░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░")
      print("░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░") 
      print("░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░") 
      print("█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█") 
      print("█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█") 
      print("░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░") 
      print("░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░") 
      print("░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░") 
      print("░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░") 
      print("░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░") 
      print("░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░") 
      print("░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░") 
      print("░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░")
      print()
      if (Homem==False):
         print("      Tá tristinha?")
      else:
         print("      Tá tristinho?")
      print()
      print("Enxugue as lágrimas e aperte ENTER.", end="")
      input()

   # Se o jogador ganhou:
   elif (CompVeiculosRestantes==0):
      print("O forfé chegou ao fim, ", Nome,", e você ganhou!!", sep="")
      print("Espero que não tenha trapaceado.")
      print()
      print("░░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░░░")
      print("░░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░░░")
      print("░░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░░░")
      print("░░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░░░")
      print("░░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░░░")
      print("░░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░░░")
      print("░░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░░░")
      print("░░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░░░")
      print("░░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░░░")
      print("░░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░░░")
      print("░░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░░░")
      print("░░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░░░")
      print("░░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░░░")
      print("░░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░░░")
      print("░░░░░█░░░░░░░░░░░░░░░░░░░░░█░░░░")
      print("░░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░░░")
      print("░░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░░░")
      print("Imagem: Você, feliz porque ganhou.")
      print()
      print("Aperte ENTER e corre contar pra sua família.", end="")
      input()

   # os tabuleiros são zerados
   ResetTotalTabJog()
   ResetTotalTabComp()

   return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
                                 #PROGRAMA PRINCIPAL

# Smart1 e Smart2 Variáveis que vão ajudar o computador a ser menos burro.
# Elas estão declaradas aqui porque eu não sabia se elas iriam funcionar caso eu apenas
# as declarasse dentro da função "ForfeAquatico" (que é onde elas são usadas). Como a
# funcionalidade delas foi resolvida literalmente horas antes da apresentação, vou deixá-las
# aqui mesmo e assim sendo conto com vossa compreensão e até, quem sabe, dó. - Inforzato
Smart1=[-1,-1]
Smart2=[-1,-1]

ShowLogo()

# Pede informações sobre o(a) jogador(a)
Nome=PegaNome()
Homem=PegaGenero(Nome)

# Inicialização das Matrizes 15x15x3
TabJog = [[[0 for k in range(0,3)] for j in range (0,15)] for i in range(0,15)]
TabComp = [[[0 for k in range(0,3)] for j in range (0,15)] for i in range(0,15)]

# Início do Loop Principal
Escolha=0
while True:
    
    MostraMenu()
    Escolha = VerificaEscolhaMenu(Escolha, Homem)
    
    if (Escolha==1): # Configura o tabuleiro
       ConfigurarTabuleiro(Nome, Homem)
        
    elif (Escolha==2): # Jogo com o tabuleiro do computador oculto
       if (TabuleiroVazio(TabJog)):
          ConfigurarTabuleiro(Nome, Homem)
          if (not TabuleiroVazio(TabJog)):
             ForfeAquatico(Nome,Homem,False)
       else:
          ForfeAquatico(Nome,Homem,False)

    elif (Escolha==3): # Jogo com o tabuleiro do computador aberto
       if (TabuleiroVazio(TabJog)):
          ConfigurarTabuleiro(Nome, Homem)
          if (not TabuleiroVazio(TabJog)):
             ForfeAquatico(Nome,Homem,True)
       else:
          ForfeAquatico(Nome,Homem,True)
        
    elif (Escolha==4): # Fornece informações sobre o jogo
       SobreOJogo()
        
    elif (Escolha==5): # Altera as informações sobre o jogador
       Nome=MudaNome(Nome, Homem)
       Homem=MudaGenero(Nome, Homem)
        
    elif (Escolha==6): # Sai do Jogo
       Tchau(Nome)
       break

print()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

