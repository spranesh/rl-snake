#!/usr/bin/env python
import keyb_interact
import snake_game.game_state
import snake_game.maze_conf_reader
import snake_game.pygame_artist
import snake_game.snake_logic

import sys

import pygame

def Initialise(size = 30):
  if len(sys.argv) == 2:
    state = snake_game.maze_conf_reader.ReadConfigurationFile(sys.argv[1])
  else:
    state = snake_game.maze_conf_reader.GetDefaultConfiguration()
  sl = snake_game.snake_logic.SnakeLogic(state)
  artist = snake_game.pygame_artist.PyGameArtist(state.size)
  interact = keyb_interact.KeyBInteract()
  return (sl, artist, interact)

def MainLoop():
  (sl, artist, interact) = Initialise()
  while True:
    artist.Draw(sl)
    move = interact.GetNextMove(sl)
    sl.Move(move)
    pygame.time.wait(100)
    if not sl.IsAlive():
      artist.Draw(sl)
      (sl, artist, interact) = Initialise()
      pygame.time.wait(900)

if __name__ == '__main__':
  MainLoop()
