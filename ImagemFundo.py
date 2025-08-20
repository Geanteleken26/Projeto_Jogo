import pygame


class Fundo:
    def __init__(self, imagem):
        self.imagem = imagem
        self.parar = None
        self.mover = None


    def mover(self, imagem):
        self.mover.direita = None
        self.mover.esquerda = None
        self.mover.cima= None
        self.mover.baixo = None

        if pygame.K_DOWN:
            self.mover.cima =
