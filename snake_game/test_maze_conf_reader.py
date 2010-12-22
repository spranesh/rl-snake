import maze_conf_reader as M

def testDefaultConfiguration():
  g = M.GetNewStateAccordingToDefaultConfiguration()
  assert(g.size == 20)

def testConfigurationFile():
  g = M.GetNewStateAccordingToConfigurationFile('')
  assert(g.size == 20)

def testConfigurationString():
  state = M.GetNewStateAccordingToString(""" {
      "num_fruits" : 3,
      "initial_length" : 3,
      "size" : 500,
      "walls" : [[20, 20], [20, 21], [20, 22], [20, 23]]
    }
  """)

  assert(state.size == 500)
  assert(state.walls == [(20, 20), (20, 21), (20, 22), (20, 23)])
  assert(state.num_fruits == 3)
  assert(state.initial_length == 3)
  return
