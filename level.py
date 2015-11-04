# -*- coding: utf-8 -*-

import os

import pytmx

import pygame
from pygame.locals import *

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

class Level(object):	# Level class

	def __init__(self, fname):

		self.width, self.height = 800, 600
		self.tile_width, self.tile_height = 64, 32

		self.screen = pygame.display.set_mode((self.width, self.height))

		self.load(fname)

	def load(self,name):
		self.tiled_map = pytmx.TiledMap(os.path.join('data', '%s.tmx'% name))
		self.tileset = load_image("iso-64x64-outside.png")
		

	def draw(self, screen):

		for layer in self.tiled_map.layers:
			for x, y, image in layer.tiles():
				
				self.tile = pygame.Surface((self.tile_width,self.tile_height), pygame.SRCALPHA, 32).convert_alpha()
				self.tile.blit(self.tileset, (0, 0), image[1])

				xPos = (( x - y ) * self.tile_width/2) + self.width/2
				yPos = (( x + y ) * self.tile_height/2) + self.height/2

				screen.blit(self.tile, (xPos, yPos - self.width/2))