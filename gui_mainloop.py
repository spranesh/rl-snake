#!/usr/bin/env python
import pygame

def GUIMainLoop(interact, artist, new_sl_function):
  """ Takes an interact object, artist object, and a function that returns a
  new snake logic."""
  sl = new_sl_function()
  while True:
    artist.Draw(sl)
    move = interact.GetNextMove(sl)
    sl.Move(move)
    pygame.time.wait(100)
    if not sl.IsAlive():
      artist.Draw(sl)
      sl = new_sl_function()
      pygame.time.wait(900)
