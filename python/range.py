#!/usr/bin/python3

for i in range(4):
  print(i+1)

flavor_list= ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i in range(len(flavor_list)):
  flavor = flavor_list[i]
  print('%d: %s' % (i + 1, flavor))

for i, flavor in enumerate(flavor_list):
  print('%d: %s' % (i + 1, flavor))

