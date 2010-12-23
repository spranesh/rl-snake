"""
Implements the Q-Learning
"""

import agent

class QLearning(agent.Agent):
  """
  Implements the Q-Learning
  """

  def UpdateQ(self, state, action, state_, action_, reward, explore):
    # if explore:
    #   return
    if not state:
      return

    q = self.Q[state][action]
    if not state_:
      q += self.alpha * (reward - q)
    else:
      q_ = max(self.Q[state_].values())
      q += self.alpha * (reward + self.gamma * q_ - q)

    self.Q[state][action] = q

