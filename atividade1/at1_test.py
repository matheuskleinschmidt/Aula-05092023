from at1 import array_generator

MIN = -999_999
MAX = 999_999
LENGTH = 20_000

def test_array_generator():
  array = array_generator()

  assert len(array) == LENGTH
  
  for number in array:
    assert number >= MIN and number <= MAX