#!/usr/bin/env python

import cPickle
import sys

def ExitWithError():
  sys.stderr.write("Usage : <program> training file")
  sys.exit(1)

if len(sys.argv) != 2:
  ExitWithError()

try:
  fp = open(sys.argv[1])
except IOError, e:
  sys.stderr.write(e + "\n")
  ExitWithError()

(e, count, Q) = cPickle.load(fp)
fp.close()

print "e = ", e
print "count", count

items = Q.items()
items.sort()
for (state, q_a) in items:
  for s in state:
    print "%3d"%s,
  for a in q_a:
    print "%10s : %+10.3f"%(a, q_a[a]),
  print

