#!/usr/bin/python3

import sys

max_num=10

try: 
  max_num=int(sys.argv[1])
except ValueError:
  print("Invalid input. Using default value")
except IndexError:
  print("No input. Using default value")
finally:
  print("Processing for %d" % max_num)

for i in range(1, max_num + 1):
  if i%2 == 0:
    print("%d is even"% i)
  else:
    print("%d is odd" % i)
