# Divide and conquer

# Combine the 2 sorted arrays
def combine(array1,array2):
  new_array=[]
  while len(array1)>0 and len(array2)>0:
    if array1[0]>=array2[0]:
      arr2_elem=array2.pop(0)
      new_array.append(arr2_elem)
    else:
      arr1_elem=array1.pop(0)
      new_array.append(arr1_elem)
  if len(array1)>0:
    new_array+=array1
  if len(array2)>0:
    new_array+=array2
  return new_array

# Divide the array
def merge_sort(array):
  if len(array)<=1:
    return array
  mid_idx=len(array)//2
  array1,array2=array[:mid_idx],array[mid_idx:]
  sorted_array1=merge_sort(array1)
  sorted_array2=merge_sort(array2)
  return combine(sorted_array1,sorted_array2)

user_input=input("Give an input of an array in form <no1 no2 no3>:\n")
array_input=[int(x) for x in user_input.split()]
print(merge_sort(array_input))
