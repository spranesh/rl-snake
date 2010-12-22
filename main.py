#!/usr/bin/env python
import agent_interact
import mainloop
import keyb_interact
import snake_game.maze_conf_reader
import snake_game.pygame_artist
import snake_game.snake_logic

import optparse
import os
import pygame
import sys
import time


def ParseCommandLineOptions(args):
  default_help_string = "[Default : %default]"
  parser = optparse.OptionParser()

  fps_options_group = optparse.OptionGroup(parser,
      "Play the game yourself.")
  fps_options_group.add_option("-f", "--fps", 
      action="store_true", dest="fps",
      help="Play! [Default: Off]")
  parser.add_option_group(fps_options_group)

  rl_options_group = optparse.OptionGroup(parser,
      "Make a reinforcement agent play the game.")
  rl_options_group.add_option("-a", "--agent", 
      type="string", dest="agent", 
      default="rl_agents.q_learning.QLearning",
      help = "The RL agent " + default_help_string)
  rl_options_group.add_option("-s", "--state_mapper", 
      type="string", dest="state_mapper", 
      default="state_mappers.quadrant_view.QuadrantView",
      help= "The State Mapper " + default_help_string)
  rl_options_group.add_option("-t", "--use-trained-file", 
      type="string", dest="trained_filename", 
      default="",
      help= "Restore the old (previously trained) Q/V values from a file ")
  rl_options_group.add_option("-w", "--dump-in-file", 
      type="string", dest="dump_filename",
      default="",
      help= "Store the Q/V values in the dump file every few moves \
      [Default: train/[chosen statemapper].[chosen agent].[time]]")
  parser.add_option_group(rl_options_group)

  parser.add_option("-m", "--maze", type="string",
      dest="maze_filename", help="Use a mazefile.")
  parser.add_option("-n", "--no_graphics", 
      action="store_true", dest="no_graphics",
      help = "Turn off Graphics [Default: Off]")
  parser.add_option("-p", "--speed", 
      type="int", dest="speed", default=10,
      help = "Speed of the game (higher is faster). Use 0 for infinity. "
      + default_help_string)

  (options, args) = parser.parse_args(args)

  # Exit with error 1, if left over arguments are found.
  if len(args) is not 0:
    sys.stderr.write("Error passing arguments. \
        Leftover arguments found : %s"%(",".join(args)))
    sys.exit(1)


  # Fill in the dump file if it is empty.
  if options.dump_filename is "":
    options.dump_filename = "train/%s-%s-%s.dump"%(
        options.state_mapper,
        options.agent,
        time.strftime("%d-%m:%H:%M"))

  return options

def Main():
  # Initialise PyGame
  os.environ["SDL_VIDEO_CENTERED"] = "1"
  pygame.init()

  options = ParseCommandLineOptions(sys.argv[1:])

  if not options.fps:
    options.speed = 0

  # Figure out the speed
  if options.speed is 0:
    delay = 0
  else:
    delay = 1000/options.speed

  # Set up a function to create a new snake logic.
  if options.maze_filename:
    new_sl_function = lambda: snake_game.snake_logic.SnakeLogic(
        snake_game.maze_conf_reader.GetNewStateAccordingToConfigurationFile(
          options.maze_filename))
  else:
    new_sl_function = lambda: snake_game.snake_logic.SnakeLogic(
        snake_game.maze_conf_reader.GetNewStateAccordingToDefaultConfiguration())

  # Set up an aritst
  if options.no_graphics:
    artist = snake_game.artist.Artist(
        new_sl_function().state.size)
  else:
    artist = snake_game.pygame_artist.PyGameArtist(
        new_sl_function().state.size)

  # If fps, start the gui mainloop
  if options.fps:
    interact = keyb_interact.KeyBInteract()
    return mainloop.MainLoop(interact, artist, new_sl_function, delay)

  else:
    interact = agent_interact.AgentInteract(options.agent, options.state_mapper, 
        options.trained_filename, options.dump_filename, backup_num_moves = 100)
    return mainloop.MainLoop(interact, artist, new_sl_function, delay)

  # sys.stderr.write("""Oops! The RL algorithms havent been implemented yet.
  #   Run with -p!\n""")
  # sys.exit(1)

if __name__ == '__main__':
  Main()
