def combine(li1,li2):
  """
  Combines two sorted lists into one sorted list with all of their elements

  @param li1: list (sorted)
  @param li2: list (sorted)
  @return list (sorted) with all elements of li1 and li2
  """
  i,j = 0,0
  combined = []
  while i < len(li1) and j < len(li2):
    if li1[i] < li2[j]:
      combined.append(li1[i])
      i+=1
    else:
      combined.append(li2[j])
      j+=1
  if i < len(li1): combined.extend(li1[i:])
  else: combined.extend(li2[j:])
  return combined

def merge_sort(array):
  """
  Sorts an array by recursively sorting and merging sub-arrays

  @param array: list of ints and/or floats to be sorted
  @return list with the same elements, but sorted list
  """
  if len(array) <=1: return array
  left = merge_sort(array[:int(len(array)/2)])
  right = merge_sort(array[int(len(array)/2):])
  return combine(left,right)