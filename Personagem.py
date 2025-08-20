class Personagem:
    def __init__(self, nome: str, vida: int, posicaox: float, posicaoy: float, pular: bool):
        self.direcao = None
        self. nome = nome
        self. vida = vida
        self. posicaox = posicaox
        self. posicaoy = posicaoy
        self. pular = pular

    def mover (self, direcao: str, ):
        self.direcao = direcao