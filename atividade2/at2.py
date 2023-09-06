import random
import sys
from at1 import array_generator
sys.path.append('../')

def sort(array):
  for number in range(len(array) - 1, 0, -1):
    for i in range(number):
      if array[i] > array[i + 1]:
        temp = array[i]
        array[i] = array[i + 1]
        array[i + 1] = temp
  return array
