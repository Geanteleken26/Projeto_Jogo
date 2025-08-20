from abc import ABC, abstractmethod

import pygame.image


class Entidade(ABC):
 def __init__(self, nome: str, posicao: int):
     self.nome = nome
     self.surf = pygame.image.load()
     self.reto =
     self.posicao = posicao
     self.nome = nome

@abstractmethod
def mover(self):
 pass

