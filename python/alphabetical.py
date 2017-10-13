#!/usr/local/bin/python3
#not working
import sys

if len(sys.argv) < 2:
  print("Please add a list to sort")
  exit(1)

items = sys.argv[1].replace(',',' ').split()

print(items)
