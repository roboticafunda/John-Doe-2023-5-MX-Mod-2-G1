import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship

# Game "tiene" un Spaceship (una instancia de un clase Spaceship)

# Game puede decirle al spaceship que se actualice llamando a su metodo update(), 
# el update del spaceship espera una lista que contiene los eventos de teclado que pudo haber capturado el game
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("Something ocurred to quit the game!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        # pygame.event.get() es un iterable (lista)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #el QUIT event es el click en el icono que cierra ventana
                self.playing = False

    def update(self):
        # el update llama al update de los objetos de algunos de los objetos de mi juego
        #cpass # pass equivale a hacer nada 
        events = pygame.key.get_pressed() # pygame.key.get_pressed() comtiene todos los eventos de teclado que pudieron ocurrir en un game loop
        self.spaceship.update(events)

    def draw(self):
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        
        # Yo "Game "se dibujar mi propioescenario
        self.draw_background()

        # Yo "Game" le ordeno al spaceship dibujarse llamando a un metodo llamado draw del Spaceship
        # el metodo draw del spaceship espera que le pasa el screen
        self.spaceship.draw(self.screen)


        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()# alto de la imagen
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) # blit "dibuja"
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
