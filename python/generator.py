#!/usr/local/bin/python3

def index_words(text):
  result = []
  if text:
    result.append(0)
  for index, letter in enumerate(text):
    if letter == ' ':
      result.append(index + 1)
  return result

def index_words_iter(text):
  if text:
    yield 0
  for index, letter in enumerate(text):
    if letter == ' ':
      yield index + 1

address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])

result = list(index_words_iter(address))
print(result[:3])
