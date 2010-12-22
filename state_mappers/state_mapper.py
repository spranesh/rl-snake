#!/usr/bin/env python

class StateMapper:
  """ An abstract state mapper class."""
  def __init__(self, directions):
    self.directions = directions
    return

  def TransformState(self, sl):
    pass

  def GetPossibleMoves(self, sl):
    pass

  def TransformMove(self, sl):
    pass
