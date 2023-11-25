import random
import string
import pygame
import sys
import time

pygame.init()

# Methinks lógica variaveis
probabilidade_de_mutacao = 5
letras_maiusculas = string.ascii_uppercase + ' '
frase_alvo = 'METHINKS IT IS LIKE A WEASEL'
primeira_string = ''
geracao = 0

# Tela do pygame variaveis
largura_tela = 800
altura_tela = 700
branco = (255, 255, 255)
preto = (0, 0, 0)
fonte = pygame.font.Font(None, 36)
doninha_fonte = pygame.font.SysFont("monospace", 10)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Dawkins’ Weasel Program")
doninha_ascii = """
                              -+*##*+:                .=*###*=.    
                          :*#%%%%%##+:-=++++++++=-:-##%%%%%##=   
                         .##%###%%##*****************#%%###%%#=  
                         :#%%#%#************************##%#%**  
                          #*%#****#++=+#**********+=+******###-  
                          *******+.    .+#*****#:     -#*****#:  
                         +#*****#.   -*- #****#-.++.   +******#. 
                         #******#-   +#+:#*****+:##:  .#******%- 
                         ********#+-::-+#**##****-:.:=*******#%: 
                         :#*************#@@@@@@%************##*  
                          -#*************%@@@@%#************#*.  
                           :#***************#*************##+    
                            .=#**************************#*:     
                              .+#**********************##:       
                               **###****************####%:       
                              =#*****#####*###*#####****##.      
                             :#******+==--------==+******#*      
                            .#******====--------=--=+*****#-     
                            +******=====------------=*****##.    
                           :#*****+=====-------------+*****#+    
                           ****#####***+==---=-==***######*#%.   
                          :#*##********##==--=-*#*********%##*   
                          **##**********#*=--==#**********#%#%.  
                         .%*##**********#*=---=%**********#%##+  
                         +***%*********#%==--=-#*****#****#####  
                         #****#*#*%**#*#*====--=#**#*#**##%*##%- 
                        .#*****#%#%##%#+-=====-==*#%*%##%#****#+ 
                        -#******=======-=====---=--=====*****### 
                        +*******=-============-------=--*****##%:
                        ********======================--+****##%+
                        #*******========================+****##%%
                        #*******========================*****###@
                        %*******+=-=====================*****##%%
                       :@*******+=---==================+*****##%=
                       *#********+==-==============-==+******##%.
                      +**#********+==-===============+*******##* 
                    .****%***********++==========++*********##%: 
                  :+#****##*******#####***********#####*****##*  
           .:--=+*********#****##******###*****##******###*##%.  
    .-=++*##***************%*##**********#%**##**********#%##:   
 :+*#*********************####*****%******#%##******##****#%:    
+#*****************######*=.:#*#**##**##*#*%%#***%***%**%##*     
-=+***#########***++==-.     +#%#**%**#####:.+#**%**##*#%#*:     
                              .+#%@@@@@%*-    .+#%@@@@@%*:              """


# Variavel de tempo
tempo = pygame.time.Clock()


# Criando a primeira string aleatória.
def criar_string_inicial():
    global primeira_string
    for _ in range(len(frase_alvo)):
        primeira_string += random.choice(letras_maiusculas)
    return primeira_string


criar_string_inicial()


# Fazer cópias das strings
def fazer_copias(primeira_string):
    copias_da_primeira_string = []
    for _ in range(100):
        copias_da_primeira_string.append(primeira_string)
    return copias_da_primeira_string


# Gerar as mutações randomicas
def gerar_mutacoes(proximas_geracoes_de_strings):
    for i in range(len(proximas_geracoes_de_strings)):
        string_com_mutacao = ''
        for letra in proximas_geracoes_de_strings[i]:
            if random.randint(1, 100) <= probabilidade_de_mutacao:
                # Chance de 5% de mutação de uma das letras da string
                string_com_mutacao += random.choice(letras_maiusculas)
            else:
                string_com_mutacao += letra
        proximas_geracoes_de_strings[i] = string_com_mutacao
    return proximas_geracoes_de_strings


# Gerador de pontuação das frases
def gerar_pontuacao(proximas_geracoes_de_strings):
    global frase_alvo
    todas_as_pontuacoes = []
    for i in range(len(proximas_geracoes_de_strings)):
        pontos = 0
        for letra in range(len(proximas_geracoes_de_strings[i])):
            if proximas_geracoes_de_strings[i][letra] == frase_alvo[letra]:
                pontos += 1
        todas_as_pontuacoes.append(pontos)
    return todas_as_pontuacoes


# Achar frase com maior pontuação
def achar_maior_nota(todas_as_pontuacoes):
    maior_ponto = 0
    indice_do_maior = 0
    for i in range(len(todas_as_pontuacoes)):
        if todas_as_pontuacoes[i] > maior_ponto:
            maior_ponto = todas_as_pontuacoes[i]
            indice_do_maior = i
    return maior_ponto, indice_do_maior


# Logica de exibição da doninha com pygame
def exibir_doninha():
    art_doninha = doninha_ascii.split('\n')
    y = 120
    for haa in art_doninha:
        textd = doninha_fonte.render(haa, True, preto)
        tela.blit(textd, (150, y))
        y += 12
    pygame.display.flip()


# Logica de exibição dos resultados com pygame#
def exibir_resultados(resultados):

    tela.fill(branco)

    text_frase = fonte.render("Frase inicial: " + primeira_string, True, preto)
    tela.blit(text_frase, (10, 20))

    text_genv = fonte.render("Geração: " + str(geracao), True, preto)
    tela.blit(text_genv, (10, 50))

    text_pont = fonte.render("Pontuação: " + str(melhor_pontuacao),
                             True, preto)
    tela.blit(text_pont, (400, 50))

    text_result = fonte.render(str(resultados), True, preto)
    tela.blit(text_result, (150, 90))

    # Atualizar a tela
    pygame.display.flip()


# Declaração de variaveis que recebem funções
novas_str_mutadas = gerar_mutacoes(fazer_copias(primeira_string))
lista_de_pontos = gerar_pontuacao(novas_str_mutadas)
melhor_pontuacao, ind_do_maior = achar_maior_nota(lista_de_pontos)
print('A primeira string, gerada de forma aleatória, foi a:\n',
      primeira_string)

# Logica final do programaa
while melhor_pontuacao < 28:
    novas_str_mutadas = gerar_mutacoes(
        fazer_copias(novas_str_mutadas[ind_do_maior]))
    geracao += 1
    lista_de_pontos = gerar_pontuacao(novas_str_mutadas)
    melhor_pontuacao, ind_do_maior = achar_maior_nota(lista_de_pontos)
    resultados = [novas_str_mutadas[ind_do_maior]]

    # Exibição usando terminal
    print(f"Geração {geracao}: {novas_str_mutadas[ind_do_maior]},"
          f" Pontuação Atual: {melhor_pontuacao} ")

    # Exibição usando pygame
    exibir_resultados(resultados)
    time.sleep(0.3)

# Exibir doninha
if melhor_pontuacao == 28:
    exibir_doninha()

# Final usando terminal pyco
print(f"A frase alvo foi alcançada após a {geracao}° geração, "
      f"partindo da frase inicial: {primeira_string}.")
print(doninha_ascii)


# Loop pygame para tela só fechar com comando
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
