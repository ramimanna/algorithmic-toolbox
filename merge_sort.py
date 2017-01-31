def combine(li1,li2):
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
  if len(array) <=1: return array
  left = merge_sort(array[:int(len(array)/2)])
  right = merge_sort(array[int(len(array)/2):])
  return combine(left,right)