#!/usr/bin/env python

import artist

import os

import pygame

class PyGameArtist(artist.Artist):
  def __init__(self, size, pixel_width=12):
    self.size = size*pixel_width
    pygame.display.set_caption("Snake")
    self.screen = pygame.display.set_mode((self.size,
      self.size))

    self.font = pygame.font.Font(None, 32)

    self.color_fruit = (255, 0, 0)
    self.color_wall = (0, 0, 0)
    self.color_snake = (0, 0, 255)
    self.pixel_width = pixel_width
    return

  def __DrawRectangle(self, logical_position, color):
    (lx, ly) = logical_position
    self.screen.fill(color, (lx * self.pixel_width, 
                             ly * self.pixel_width,
                             self.pixel_width,
                             self.pixel_width))
    return

  def Draw(self, sl):
    if not sl.IsAlive():
      gameovertext = self.font.render("GAME OVER!", 1, (0, 0, 0))
      self.screen.blit(gameovertext,
          ((self.size - gameovertext.get_width())/2
          ,(self.size - gameovertext.get_height())/2))
    else:
      state = sl.state
      self.screen.fill((255, 255, 255))

      for fruit in state.fruits:
        self.__DrawRectangle(fruit, self.color_fruit)

      for wall in state.walls:
        self.__DrawRectangle(wall, self.color_wall)

      for s in state.snake_position:
        self.__DrawRectangle(s, self.color_snake)

      score = self.font.render("Score : %d"%sl.GetScore(), 1, (0, 0, 0))
      self.screen.blit(score, (5, 5))

    pygame.display.flip()
    return

