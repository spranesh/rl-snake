import directions as D

def testReverse():
  assert(D.Reverse(D.LEFT) == D.RIGHT)
  assert(D.Reverse(D.RIGHT) == D.LEFT)
  assert(D.Reverse(D.DOWN) == D.UP)
  assert(D.Reverse(D.UP) == D.DOWN)
  return

def testMoveInDirection():
  assert(D.MoveInDirection((0, 5), D.UP) == (0, 4))
  assert(D.MoveInDirection((0, 5), D.DOWN) == (0, 6))
  assert(D.MoveInDirection((0, 5), D.LEFT) == (-1, 5))
  assert(D.MoveInDirection((0, 5), D.RIGHT) == (1, 5))
  return
