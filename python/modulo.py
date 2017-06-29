#!/usr/bin/python

upperlimit = int(raw_input("Upper limit: "))

for number in range(1, upperlimit + 1):
  if number%2 == 1:
    print "%d Odd" % number
  else:
    print "%d Even" % number
