from .system import System
import pygame


class GameWindowSystem(System):
    def __init__(self):
        System.__init__(self)
        pygame.init()

    def update(self, component):
        if 'screen' not in component:
            component['screen'] = pygame.display.set_mode((
                component['width'],
                component['height']
            ))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'

            component['screen'].fill((0, 0, 0))
            pygame.display.flip()
