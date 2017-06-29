#!/usr/local/bin/python3
import sys

files = sys.argv[1:]

fds = [open(file, 'r') for file in files]

while 1 :
  line = "\t".join([fd.readline().strip() for fd in fds])
  if not line.strip() :
    break
  print (line)

for fd in fds:
  fd.close()
