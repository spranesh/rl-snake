#!/usr/bin/env python

import interact

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
      trained_filename, dump_file, backup_num_moves = 100):
    self.trained_filename = trained_filename
    self.dump_file = dump_file

    self.state_mapper_class = DynamicImportMember(state_mapper_string)
    self.agent_class = DynamicImportMember(agent_string)

    self.agent = self.agent_class(self.state_mapper_class(), 
        self.trained_filename)

    self.move_counter = 0
    self.backup_num_moves = backup_num_moves
    return

  def GenNextMove(self, sl):
    self.move_counter += 1

    if self.move_counter == self.backup_num_moves:
      self.agent.WriteKnowledge(self.dump_file)
      self.move_counter = 0

    return self.agent.GetMove(sl)
