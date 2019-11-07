# Function to sort
def bubble_sort(array):
  array_len=len(array)
  for i in range(array_len-1):
    for j in range(array_len-1-i):
      if array[j]>array[j+1]:
        array[j],array[j+1]=array[j+1],array[j]
  return array

# User input array
array=input("Enter an array of numbers to sort in <no1 no2 no3> format:\n")
array_input=[int(x) for x in array.split()]
print(bubble_sort(array_input))

