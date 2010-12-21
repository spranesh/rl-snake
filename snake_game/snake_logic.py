#!/usr/bin/env python
import directions

import random

class SnakeLogic:
  def __init__(self, state):
    self.state = state
    self.alive = True
    for i in range(self.state.num_fruits - len(self.state.fruits)):
      self.state.fruits.append(self.__CreateNewFruit())

  def __GetUpdateAlive(self):
    head = self.state.snake_position[0]

    # Check if the snake is still in bounds.
    (x, y) = head
    if x < 0 or self.state.size <= x: return False
    if y < 0 or self.state.size <= y: return False

    # Check whether the snake hit itself.
    if head in self.state.snake_position[1:]:
      return False

    # Check if the snake hit wall.
    if head in self.state.walls:
      return False
    return True

  def __WasFruitEaten(self):
    head = self.state.snake_position[0]
    if head in self.state.fruits:
      return True
    return False

  def __CreateNewFruit(self):
    while True:
      x = random.randint(0, self.state.size-1)
      y = random.randint(0, self.state.size-1)
      if (x, y) in self.state.snake_position:
        continue
      if (x, y) in self.state.fruits:
        continue
      if (x,y) in self.state.walls:
        continue
      return (x, y)

  def Move(self, direction):
    if direction == directions.Reverse(self.state.direction):
      direction = directions.Reverse(self.state.direction)

    head = self.state.snake_position[0]
    self.state.snake_position.insert(0, 
        directions.MoveInDirection(head, direction))
    head = self.state.snake_position[0]

    self.state.direction = direction

    self.alive = self.__GetUpdateAlive()

    if self.alive is False:
      return

    # Check if the new head is at a fruit. If so, we make the snake grow
    # larger, and create a new fruit. Otherwise, we move the snake one step
    # by popping the last coordinate.
    if self.__WasFruitEaten():
      i = self.state.fruits.index(head)
      self.state.fruits[i] = self.__CreateNewFruit()
      self.state.snake_length += 1
    else:
      self.state.snake_position.pop()
    return

  def GetState(self):
    return self.state

  def GetScore(self):
    return self.state.snake_length - self.state.initial_length

  def IsAlive(self):
    return self.alive

