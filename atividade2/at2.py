import random

MIN = -999_999
MAX = 999_999
LENGTH = 20_00


def array_generator():
  array = []

  for _ in range(LENGTH):
    array.append(random.randint(MIN, MAX))

  return array


def sort(array):
  for number in range(len(array) - 1, 0, -1):
    for i in range(number):
      if array[i] > array[i + 1]:
        temp = array[i]
        array[i] = array[i + 1]
        array[i + 1] = temp
  return array
