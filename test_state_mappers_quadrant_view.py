""" Tests for the quadrant view file. """
import state_mappers.quadrant_view as Q
import snake_game.directions as D

def testSigNum():
  assert(Q.SigNum(-1) == -1)
  assert(Q.SigNum(-5) == -1)

  assert(Q.SigNum(0) == 0)

  assert(Q.SigNum(1) == 1)
  assert(Q.SigNum(5) == 1)
  return

def testGetQuadrant():
  assert(( 1,  1) == Q.GetQuadrant(( 5,  5)))
  assert((-1,  1) == Q.GetQuadrant((-5,  5)))
  assert((-1, -1) == Q.GetQuadrant((-5, -5)))
  assert(( 1, -1) == Q.GetQuadrant(( 5, -5)))

  assert(( 1,  0) == Q.GetQuadrant(( 5,  0)))
  assert(( 0,  0) == Q.GetQuadrant(( 0,  0)))
  return

def testTransformQuadrantBasedOnDirectionUP():
  assert(( 1,  1) == Q.TransformQuadrantBasedOnDirection((5, 4),   D.UP, D))
  assert(( 1, -1) == Q.TransformQuadrantBasedOnDirection((5, -5),  D.UP, D))
  assert((-1,  1) == Q.TransformQuadrantBasedOnDirection((-5, 3),  D.UP, D))
  assert((-1, -1) == Q.TransformQuadrantBasedOnDirection((-5, -3), D.UP, D))

  assert(( 0,  0) == Q.TransformQuadrantBasedOnDirection((0, 0),   D.UP, D))
  assert((-1,  0) == Q.TransformQuadrantBasedOnDirection((-5, 0),  D.UP, D))

def testTransformQuadrantBasedOnDirectionDOWN():
  assert((-1, -1) == Q.TransformQuadrantBasedOnDirection((5, 4),   D.DOWN, D))
  assert((-1,  1) == Q.TransformQuadrantBasedOnDirection((5, -5),  D.DOWN, D))
  assert(( 1, -1) == Q.TransformQuadrantBasedOnDirection((-5, 3),  D.DOWN, D))
  assert(( 1,  1) == Q.TransformQuadrantBasedOnDirection((-5, -3), D.DOWN, D))

  assert(( 0,  0) == Q.TransformQuadrantBasedOnDirection((0, 0),   D.DOWN, D))
  assert(( 1,  0) == Q.TransformQuadrantBasedOnDirection((-5, 0),  D.DOWN, D))

def testTransformQuadrantBasedOnDirectionLEFT():
  assert(( 1, -1) == Q.TransformQuadrantBasedOnDirection((5, 4),   D.LEFT, D))
  assert((-1, -1) == Q.TransformQuadrantBasedOnDirection((5, -5),  D.LEFT, D))
  assert(( 1,  1) == Q.TransformQuadrantBasedOnDirection((-5, 3),  D.LEFT, D))
  assert((-1,  1) == Q.TransformQuadrantBasedOnDirection((-5, -3), D.LEFT, D))

  assert(( 0,  0) == Q.TransformQuadrantBasedOnDirection((0, 0),   D.LEFT, D))
  assert(( 0,  1) == Q.TransformQuadrantBasedOnDirection((-5, 0),  D.LEFT, D))

def testTransformQuadrantBasedOnDirectionRIGHT():
  assert((-1,  1) == Q.TransformQuadrantBasedOnDirection((5, 4),   D.RIGHT, D))
  assert(( 1,  1) == Q.TransformQuadrantBasedOnDirection((5, -5),  D.RIGHT, D))
  assert((-1, -1) == Q.TransformQuadrantBasedOnDirection((-5, 3),  D.RIGHT, D))
  assert(( 1, -1) == Q.TransformQuadrantBasedOnDirection((-5, -3), D.RIGHT, D))

  assert(( 0,  0) == Q.TransformQuadrantBasedOnDirection((0, 0),   D.RIGHT, D))
  assert(( 0, -1) == Q.TransformQuadrantBasedOnDirection((-5, 0),  D.RIGHT, D))
