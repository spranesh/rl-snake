"""
Generic Value Based agent
"""

import cPickle
import random
import sys

class Agent():
  """
  Generic Value-based agent
  """
  Q = {}

  def __init__(self, trained_file = "", gamma = 0.9, alpha = 0.8, e = 0.1):
    self.gamma = gamma
    self.alpha = alpha
    self.e = e
    self.old_state = None
    self.old_action = None
    self.Q = {}

    if trained_file is not "":
      try:
        self.Q = cPickle.load(open(trained_file))
      except IOError, e:
        sys.stderr.write(("File " + trained_file + " not found. \n"))
        sys.exit(1)

    return


  def UpdateQ(self, state, action, state_, action_, reward):
    raise NotImplemented()

  def Act(self, state, actions, reward, episode_ended):
    # epsilon-greedy
    if not self.Q.has_key(state):
      self.Q[state] = {}
      for action in actions:
        self.Q[state][action] = 0

    # Explore
    if random.random() < self.e:
      action = actions[random.randint(0, len(actions)-1)]
      explore = True
    # Exploit
    else:
      action = max(actions, key = lambda x: self.Q[state][x])
      explore = False

    # Update actions
    if episode_ended:
      self.UpdateQ(self.old_state, self.old_action, None, None, reward,
          explore)
    else:
      self.UpdateQ(self.old_state, self.old_action, state, action, reward,
          explore)

    self.old_state = state
    self.old_action = action
    return action

  def WriteKnowledge(self, filename):
    fp = open(filename, "w")
    cPickle.dump(self.Q, fp)
    fp.close()
    return
