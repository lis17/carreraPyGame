import pygame
import sys


class Game():
    corredores = []
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
     
    def competir(self):
        while True:
             #comprobación de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #refrescar / renderizar la pantalla        
            self.__screen.blit(self, background,(0,0))
            pygame.display.flip()
            
    
if __name__=='__main__':
    pygame.init() # esto hay que hacerlo siempre
    game = Game()
    game.competir()
    
    