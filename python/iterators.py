#!/usr/bin/python3

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

#for i in range(len(names)):
#  count = letters[i]
#  if count > max_letters:
#    longest_name = names[i]
#    max_letters = count

for name, count in zip(names, letters):
  if count > max_letters:
    longest_name = name
    max_letters = count

print(longest_name)

a = 4
b = 9
for i in range(2, min(a, b) + 1):
  print('Testing', i)
  if a % i == 0 and b % i == 0:
    print('Not coprime')
    break
else:
  print('Coprime')
