# classe principal do jogo
import pygame

pygame.init()

window = pygame.display.set_mode(size= (600, 480))

pygame.display.set_caption("Minha Janela Pygame")
print("setup")
while True:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         pygame.quit()
         quit()

 window.fill((25, 25, 112))

 pygame.display.update()



