import maze_conf_reader as M

def testDefaultConfiguration():
  g = M.GetDefaultConfiguration()
  assert(g.size == 20)

def testReadConfigurationFile():
  g = M.ReadConfigurationFile('')
  assert(g.size == 20)

def testReadConfigurationString():
  state = M.ReadConfigurationString(""" {
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
