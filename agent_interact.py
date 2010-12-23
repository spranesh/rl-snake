#!/usr/bin/env python

import interact
import snake_game.directions

import sys

def DynamicImportMember(classpath):
  """ Imports a variable (function/class) dynamically, given its class path.
  For example, given state_mappers.quadrant_view.QuadrantView this function
  does
        from state_mappers.quadrant_view import quadrant_view
        return quadrant_view.QuadrantView """
  try:
    module_name, variable_name = classpath.rsplit('.', 1)
    module = __import__(module_name, fromlist = module_name)
    return module.__dict__[variable_name]
  except ImportError, e:
    sys.stderr.write("Import %s failed \n"%(classpath))
    sys.stderr.write(str(e) + "\n")
    sys.exit(1)
  except KeyError, e:
    sys.stderr.write("Module %s does not contain %s \n"%(
      module_name, variable_name))
    sys.stderr.write(str(e) + "\n")
    sys.exit(1)
  return None



class AgentInteract(interact.Interact):
  """ Interacts with a specified RL agent which is initialised using a given
  state_mapper. The agent uses the state mapper to map the state passed to it.

      This interactor also makes the agent backup its knowledge every so many
      moves."""
  def __init__(self, agent_string, state_mapper_string, 
      trained_filename, dump_filename, epsilon, backup_num_moves = 10000):
    self.trained_filename = trained_filename
    self.dump_filename = dump_filename

    self.state_mapper_class = DynamicImportMember(state_mapper_string)
    self.agent_class = DynamicImportMember(agent_string)

    self.agent = self.agent_class(epsilon, self.trained_filename)
    self.state_mapper = self.state_mapper_class(snake_game.directions)

    self.move_counter = 0
    self.backup_num_moves = backup_num_moves

    self.episode_ended = False
    self.reward = 0
    return

  def PerformAndReturnNextMove(self, sl):
    self.move_counter += 1

    if self.move_counter == self.backup_num_moves:
      print self.move_counter
      self.agent.WriteKnowledge(self.dump_filename)
      self.move_counter = 0

    state_ = self.state_mapper.TransformState(sl)
    move_ = self.agent.Act(state_, self.state_mapper.GetAllowedMoves(sl),
        self.reward, self.episode_ended)
    move = self.state_mapper.TransformMove(sl, move_)

    # Make the move
    sl.Move(move)

    # If nothing happens
    self.reward = -1 

    # Handle the case the snake died
    if not sl.IsAlive():
      self.reward = -100
      self.episode_ended = True
      # print
    else:
      self.episode_ended = False

    # If we ate a fruit
    if sl.WasFruitEaten():
      self.reward = 500
      # print '*',
    
    return move
