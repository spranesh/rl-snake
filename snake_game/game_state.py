#!/usr/bin/env python

""" Definition of the Snake Game State."""

import directions

import sys

class GameState:
  def __init__(self, size, initial_length=3, num_fruits=1):
    if initial_length >= size/2:
      sys.stderr.write("Too large an initial size. No point playing. Bye!")
      sys.exit(1)

    self.size = size
    self.initial_length = initial_length
    self.snake_length = initial_length
    self.num_fruits = num_fruits
    self.direction = directions.UP

    self.fruits = []
    self.snake_position = []
    self.walls = []

    for i in range(initial_length):
      self.snake_position.append((size/2, size/2+i))
    return
