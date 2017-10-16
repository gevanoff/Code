#!/usr/local/bin/python3
#gevanoff@gmail.com
import sys

def csv_to_list(text):
  word_list = text.replace(',',' ').replace('\\',' ').split()
  return word_list

if len(sys.argv) < 2:
  print("Please add a list to sort")
  exit(1)

items = []
for set in sys.argv[1:]:
  for item in csv_to_list(set):
    items.append(item)

items.sort()

print(", ".join(items))
