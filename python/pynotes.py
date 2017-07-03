def to_str(bytes_or_str):
  if isinstance(bytes_or_str, bytes):
    value = bytes_or_str.decode('utf-8')
  else:
    value = bytes_or_str
  return value # Instance of str

def to_bytes(bytes_or_str):
  if isinstance(bytes_or_str, str):
    value = bytes_or_str.encode('utf-8')
  else:
    value = bytes_or_str
  return value # Instance of bytes

# Sequence slicing [start:end:stride]
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

a[:] # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:5] # ['a', 'b', 'c', 'd', 'e']
a[:-1] # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
a[4:] # ['e', 'f', 'g', 'h']
a[-3:] # ['f', 'g', 'h']
a[2:5] # ['c', 'd', 'e']
a[2:-1] # ['c', 'd', 'e', 'f', 'g']
a[-3:-1] # ['f', 'g']
a[::2] # ['a', 'c', 'e', 'g']
#Avoid using stride along with start and end
a[-2:-2] # ['g', 'e', 'c', 'a']
a[-2:2:-2] # ['g', 'e']
a[2:2:-2] # []

a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
a[::2] # ['red', 'yellow', 'blue'] #evens
a[1::2] # ['orange', 'green', 'purple'] #odds

# Reversing order works for byte strings but breaks unicode
x = b'mongoose'
y = x[::-1]
print(y) # b'esoognom'

# List comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
even_squares = [x**2 for x in a if x % 2 == 0]

# Dictionaries
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict) # {1: 'ghost', 2: 'habanero', 3: 'cayenne'}
print(chile_len_set) # {8, 5, 7}

# Multiple loops in list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = [[x**2 for x in row] for row in matrix]
print(squared) # [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
#Avoid using more than two expressions in a list comprehension

#Use Generator Expressions for large comprehensions to avoid tying up memory
it = (len(x) for x in open('my_file.txt'))
print(it) # Returns only iterator
print(next(it)) # iterator advanced one step and returns value
#use iterator as input for another generator. 
roots = ((x, x**0.5) for x in it) #When 'root' iterator is advanced...
print(next(roots)) #...the interior operator 'it' will also advance

#Prefer enumerate to range
#These two are equivalent and allow the index 'i' to be tracked
flavor_list= ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i in range(len(flavor_list)):
  flavor = flavor_list[i]
  print('%d: %s' % (i + 1, flavor))

for i, flavor in enumerate(flavor_list):
  print('%d: %s' % (i + 1, flavor))

#Use zip to process iterators in parallel
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

#for i in range(len(names)):
#  count = letters[i]
#  if count > max_letters:
#    longest_name = names[i]
#    max_letters = count
#Equivalent to
for name, count in zip(names, letters):
  if count > max_letters:
    longest_name = name
    max_letters = count

print(longest_name)
#But watch out if the two lists don't match size

#Avoid else blocks after for and while loops.
for i in range(3):
  print('Loop %d' % i) #Loop 0, Loop 1, Loop 2...
else:
  print('Else block!') #...Else block! Only prints if loop completes! V. Confusing

#Use try/except/else/finally
try:
  attempt_to_do_this_thing()
except SpecificError:
  print("I ran into a SpecificError!")
except:
  print("I ran into some other Error!")
else:
  print("The attempt_to_do_this_thing succeeded!")
finally:
  print("I print in any case!")

#Raise exceptions from Functions rather than returning None
def divide(a, b)
  try:
    return a / b
  except ZeroDivisionError as e:
    raise ValueError('Invalid inputs') from e
