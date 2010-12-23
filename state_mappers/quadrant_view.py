#!/usr/bin/env python

import state_mapper

def SigNum(x):
  if x < 0:
    return -1
  if x > 0:
    return 1
  else: return 0

def GetQuadrant(coord):
  (sign_x, sign_y) = (SigNum(coord[0]), SigNum(coord[1]))

  if sign_x == 0: qx = 0
  elif sign_x == 1: qx = 1
  else: qx = -1

  if sign_y == 0: qy = 0
  elif sign_y == 1: qy = 1
  else: qy = -1

  return (qx, qy)
  
def TransformQuadrantBasedOnDirection(coord, d, directions):
  # Transform it relative to the snake
  (x, y) = coord

  if d == directions.LEFT:  (x, y) = ( y, -x)
  if d == directions.RIGHT: (x, y) = (-y,  x)
  if d == directions.DOWN:  (x, y) = (-x, -y)

  return GetQuadrant((x, y))

class QuadrantView(state_mapper.StateMapper):
  """ 
    The Quandrant View class maps the snake board as follows:

      * The resultant view is RELATIVE to the snake's head.
      * It returns a five-tuple
        + The first three elements of the pair form a description vector
          indicating whether there is a wall adjacent to the snake in each of
          the allowed directions.
        + The fourth and fifth elements indicates which quadrant the fruit is
          in. This can take on one of four possible values for each of the four
          quadrants.
  """

  def __SquareDescription(self, sl, square):
    """ Returns -1 if the square is a wall, snake_position, or a corner.
        Returns 1 if it is a fruit. 0 otherwise."""
    if square in sl.state.walls: return -1
    if square in sl.state.snake_position: return -1

    (x, y) = square
    if x < 0 or sl.state.size <= x: return -1
    if y < 0 or sl.state.size <= y: return -1

    if (x, y) in sl.state.fruits: return 1
    return 0


  def TransformState(self, sl):
    all_directions = self.directions.GetAllDirections()
    head = sl.state.snake_position[0]

    square_description = []
    for move in self.GetAllowedMoves(sl):
      transformed_direction = self.TransformMove(sl, move)
      n = self.directions.MoveInDirection(head, transformed_direction)
      square_description.append(self.__SquareDescription(sl, n))

    fruit = sl.state.fruits[0]

    # print "head: ", head, "fruit: ", fruit

    # The state's y axes is oriented in the opposite direction.
    head = (head[0], -head[1])
    fruit = (fruit[0], -fruit[1])

    (x, y) = (fruit[0] - head[0], fruit[1] - head[1])

    (qx, qy) = TransformQuadrantBasedOnDirection((x, y), 
        sl.state.direction, self.directions)

    mapped_state = (square_description[0], square_description[1], 
        square_description[2], qx, qy)
    # print (x, y), sl.state.direction, mapped_state
    # print
    return mapped_state

  def GetAllowedMoves(self, sl):
    return ['GO_LEFT', 'GO_RIGHT', 'GO_STRAIGHT']
  
  def TransformMove(self, sl, move):
    if move == 'GO_STRAIGHT':
      return sl.state.direction

    if sl.state.direction == self.directions.UP:
      go_left_direction = self.directions.LEFT
    if sl.state.direction == self.directions.DOWN:
      go_left_direction = self.directions.RIGHT
    if sl.state.direction == self.directions.LEFT:
      go_left_direction = self.directions.DOWN
    if sl.state.direction == self.directions.RIGHT:
      go_left_direction = self.directions.UP

    if move == 'GO_LEFT':
      return go_left_direction
    elif move == 'GO_RIGHT':
      return self.directions.Reverse(go_left_direction)
    assert(false)
    return
