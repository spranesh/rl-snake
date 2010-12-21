#!/usr/bin/env python
import game_state as G
import snake_logic as S
import directions as D

import unittest

class TestSnakeLogic(unittest.TestCase):

  def setUp(self):
    gs = G.GameState(20, num_fruits=0)
    self.sl = S.SnakeLogic(gs)

  def testInit(self):
    return
  
  def testCreateNewFruit(self):
    gs = G.GameState(20, num_fruits=5)
    assert(len(gs.fruits) == 0)
    sl = S.SnakeLogic(gs)
    assert(len(sl.state.fruits) == 5)
    return
  
  def testMoveUp(self):
    self.sl.Move(D.UP)
    assert(self.sl.IsAlive() == True)
    assert(self.sl.state.snake_position[0] == (10, 9))
    return

  def testMoveOutOfBounds(self):
    for i in range(self.sl.state.size/2+1):
      assert(self.sl.IsAlive())
      self.sl.Move(D.LEFT)
    assert(self.sl.IsAlive() == False)

  def testFruitLength(self):
    self.sl.state.fruits = [(10, 9)]
    l = self.sl.state.snake_length
    self.sl.Move(D.UP)
    assert(self.sl.state.snake_length == l+1)

  def testHitWall(self):
    self.sl.state.walls = [(9, 9), (10, 9), (11, 9)]
    self.sl.Move(D.UP)
    assert(self.sl.IsAlive() == False)

  def testNewFruitAfterFruitEaten(self):
    self.sl.state.fruits = [(10, 9)]
    self.sl.Move(D.UP)
    assert(len(self.sl.state.fruits) == 1)
    

