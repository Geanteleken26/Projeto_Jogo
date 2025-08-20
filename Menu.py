import pygame
from pygame import Surface, Rect
from pygame.font import Font

# Importando constantes
from Const import C_BLUE, WIN_WIDTH, OPCAO_MENU, C_CYAN, WIN_HEIGHT, C_ORANGE, C_GREEN

# --- Início da inicialização do Pygame (melhor lugar para isso)
pygame.init()
pygame.display.set_caption("Minha Janela Pygame")
window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT) )
imagem = pygame.image.load('./assets/MenuBg.png')




# --- Fim da inicialização

class Menu:
    def __init__(self, janela):
        self.janela = janela
        self.surf = imagem


        self.retangulo = self.surf.get_rect(left=0, top=0)

        font_titulo: Font = pygame.font.SysFont(name='Arial', size=50)
        self.titulo_surface = font_titulo.render('Jogo da Velha', True, C_BLUE)
        self.titulo_organizado = self.titulo_surface.get_rect(center=(WIN_WIDTH / 2, 10))


    def rodar(self):
        try:
            opcao_menu = 0
            pygame.mixer_music.load('./assets/377314__bambumusico__drum-song-mid-to-wav.wav')
            pygame.mixer_music.play(-1)
            pygame.display.set_caption('Jogo da Velha')
            C_CYAN




        # Verifique se o caminho do arquivo e o formato estão corretos.
        # pygame.mixer.music.load('./assets/sua_musica.ogg')
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print({e})


        while True:
            self.janela.blit(source=self.surf, dest=self.retangulo)
            self.menu_text(50, 'Jogo', C_ORANGE , ((WIN_WIDTH /2),70))
            self.menu_text(50, 'da Velha', C_ORANGE, ((WIN_WIDTH /2),120))

            for i in range(len(OPCAO_MENU)):

             self.menu_text(18, OPCAO_MENU[i], C_BLUE, ((WIN_WIDTH / 2), 200 + 25 * i))




                # Atualiza a tela
            pygame.display.flip()


            pygame.display.flip()





            # Atualiza a tela
            pygame.display.flip()

            # Processando eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if opcao_menu < len(OPCAO_MENU) - 1:
                            opcao_menu += 1
                        else:
                            opcao_menu = 0  # Corrige a variável

                    elif event.key == pygame.K_UP:
                        if opcao_menu > 0:
                            opcao_menu -= 1
                        else:
                            opcao_menu = len(OPCAO_MENU) - 1  # Corrige a variável

                    elif event.key == pygame.K_RETURN:
                        return OPCAO_MENU[opcao_menu]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.janela.blit(source=text_surf, dest=text_rect)


# --- Exemplo de uso
# Crie a instância do menu e passe a janela para ele
menu_principal = Menu(window)
# Chame o método rodar para iniciar o menu
opcao_selecionada = menu_principal.rodar()
print(f'A opção selecionada foi: {opcao_selecionada}')

# Exemplo de loop principal do jogo após o menu
# while True:
#    # Lógica do jogo aqui...
#    pygame.display.update()