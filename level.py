# -*- coding: utf-8 -*-

import os

import pygame

import pyscroll
import pyscroll.data

from pyscroll.group import PyscrollGroup
from pytmx.util_pygame import load_pygame

if not pygame.font:
    print 'Warning, fonts disabled'
if not pygame.mixer:
    print 'Warning, sound disabled'


def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert_alpha()
    except pygame.error, message:
        print 'Cannot load image: ', name
        raise SystemExit, message

    return image


class Level(object):

    def __init__(self, fname):

        self.width, self.height = 800, 600
        self.tile_width, self.tile_height = 64, 32

        self.fullname = os.path.join('data', '%s.tmx' % fname)

        self.tmx_data = load_pygame(self.fullname)

        self.map_data = pyscroll.TiledMapData(self.tmx_data)

        self.tileset = load_image("iso-64x64-outside.png")

        self.map_layer = pyscroll.IsometricBufferedRenderer(self.map_data, (self.width, self.height))

        self.group = PyscrollGroup(map_layer=self.map_layer, default_layer=2)