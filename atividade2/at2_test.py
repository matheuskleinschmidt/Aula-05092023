from at2 import sort, array_generator

def test_sort():
  array = array_generator()
  
  result1 = sort(array)                 
  result2 = sort(array)
  result3 = sorted(array)

  assert result1 == result2

  assert result1 == result3