# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from pytmx.util_pygame import load_pygame

from level import Level
from player import Player

if not pygame.font:
    print 'Warning, fonts disabled'
if not pygame.mixer:
    print 'Warning, sound disabled'

BLACK = (0x00, 0x00, 0x00)


class MainGame(object):  # Game class

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)  # sounds
        pygame.init()
        pygame.display.set_caption("IsoGame")  # Set app name
        pygame.key.set_repeat(1, 20)

        self.width, self.height = 800, 600

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.temp_surface = pygame.Surface((self.width / 1.5, self.height / 1.5)).convert()

        self.clock = pygame.time.Clock()

        self.player = Player("player", (100, 100))

        self.level = Level("level1")

        self.levelGroup = self.level.group
        self.levelGroup.add(self.player)

    def draw(self, screen):

        # center the map/screen on our Hero
        self.levelGroup.center(self.player.rect.center)

        # draw the map and all sprites
        self.levelGroup.draw(screen)

    def update(self, dt):
        """ Tasks that occur over time should be handled here """

        self.levelGroup.update()

    def main(self):
        while True:
            dt = self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                # this will be handled if the window is resized
                elif event.type == VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                self.player.handle_event(event)

            self.update(dt)

            self.temp_surface.fill(BLACK)
            self.draw(self.temp_surface)

            pygame.transform.scale(self.temp_surface, self.screen.get_size(), self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    game = MainGame()
    game.main()
