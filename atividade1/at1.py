import random

MIN = -999_999
MAX = 999_999
LENGTH = 20_000

def array_generator():
  array = []

  for _ in range(LENGTH):
    array.append(random.randint(MIN, MAX))

  return array

def test_array_generator():
  array = array_generator()

  assert len(array) == LENGTH
  
  for number in array:
    assert number >= MIN and number <= MAX