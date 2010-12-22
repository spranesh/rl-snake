import agent

class SARSA(agent.Agent):
  """
  Implements SARSA
  """
  def UpdateQ(self, state, action, state_, action_, reward, explore):
    if not state:
        return

    q = self.Q[state][action]
    if not state_:
     q += self.alpha * (reward - q)
    else:
      q_ = self.Q[state_][action_]
      q += self.alpha * (reward + self.gamma * q_ - q)

    self.Q[state][action] = q

