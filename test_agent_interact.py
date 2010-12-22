#!/usr/bin/env python

import agent_interact as A

def testDynamicImportMember1():
  # Check with a function
  relpath = A.DynamicImportMember("os.path.relpath")
  import os.path
  assert(relpath == os.path.relpath)
  return

def testDynamicImportMember2():
  # Check with a class
  option_parser = A.DynamicImportMember("optparse.OptionParser")
  import optparse
  assert(option_parser == optparse.OptionParser)
  return

def testDynamicImportMember3():
  # Check with a snake_game module
  import snake_game.pygame_artist as S
  artist = A.DynamicImportMember("snake_game.pygame_artist.PyGameArtist")
  assert(S.PyGameArtist == artist)
  return
