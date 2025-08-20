import pygame
# cores para jogo
#c
C_BLUE = (6,57,112)
C_ORANGE = (255, 128, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# ações do inimigo

EVENT_INIMIGO = pygame.USEREVENT + 1
TEMPO_DO_EVENTO = pygame.USEREVENT + 2

# ações das entidades

VELOCIDADE_ENTIDADE = {
    'inimigonível1':1,
    'inimigonível2':2,
    'inimigonível3':3,
    'inimigonível4':4,
    'jogador1': 3,
    'jogador2': 3,
    'tirojogador1': 1,
    'tirojogador2': 1,



}

SAUDE_ENTIDADE = {
   'inimigo': 900,
   'jogador1': 300,
   'jogador2': 300,
   'chefão': 500
}

DANOS_ENTIDADE = {
    'inimigo': 300,
    'personagem1': 25,
    'personagem2': 25,
    'chefão': 30,
    'chefão nível final': 60,

}

PONTUACAO = {
    'jogador1 cada inimigo morto': 1,
    'jogador ao concluir fase': 10,
}

OPCAO_MENU = (
    'Jogar  1Player',
    'Jogar cooperativo 2Player',
    'Pontuação',
    'Sair'
)

#w

WIN_WIDTH = 576
WIN_HEIGHT = 324



