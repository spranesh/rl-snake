#!/usr/bin/env python

""" Possible Directions for the Snake """

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

def Reverse(direction):
  return {UP: DOWN,
          DOWN: UP,
          LEFT: RIGHT,
          RIGHT: LEFT}[direction]

def MoveInDirection(square, direction):
  """ Returns the given square moved in the given direction. """
  (x, y) = square
  if direction == UP:
    return (x, y-1)
  elif direction == DOWN:
    return (x, y+1)
  elif direction == LEFT:
    return (x-1, y)
  elif direction == RIGHT:
    return (x+1, y)
