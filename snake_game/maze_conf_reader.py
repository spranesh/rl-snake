#!/usr/bin/env python
import game_state

import json
import sys

""" Reads a maze configuration file. These files are written in json,
    and an example is as follows:

    { "num_fruits" : 3,
      "initial_length" : 3,
      "size" : 500,
      "walls" : [[20, 20], [20, 21], [20, 22], [20, 23]]
    }
"""

def GetDefaultConfiguration():
  return game_state.GameState(20)


def ReadConfigurationFile(filename):
  if not filename:
    return GetDefaultConfiguration()

  try:
    config_fp = open(filename).read()
  except IOError, e:
    sys.stderr.write(("Configuration File %s not found"%(filename)))
    sys.exit(1)

  return ReadConfigurationString(config_fp)

def ReadConfigurationString(config_data):

  config = json.loads(config_data)

  try:
    size = config['size']
    num_fruits = config['num_fruits']
    initial_length = config['initial_length']
    walls = config['walls']
  except KeyError, e:
    sys.stderr.write("Missing Data in configuration file \n")
    sys.stderr.write(str(e))
    sys.exit(1)

  walls = map(tuple, walls)
  state = game_state.GameState(size, initial_length=initial_length,
      num_fruits=num_fruits)

  state.walls = walls
  return state

