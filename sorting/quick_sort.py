from random import randrange

# Quick sort function
def quick_sort(my_list,start,end):
  if start>=end:
    return my_list
  else:
    pivot_index=randrange(start,end)
    pivot_element=my_list[pivot_index]
    my_list[pivot_index],my_list[end]=my_list[end],my_list[pivot_index]
    current_pointer=start
    lesser_than_pointer=start
    while current_pointer<end:
      if my_list[current_pointer]<=my_list[end]:
        if current_pointer!=lesser_than_pointer:
          my_list[current_pointer],my_list[lesser_than_pointer]=my_list[lesser_than_pointer],my_list[current_pointer]
        current_pointer+=1
        lesser_than_pointer+=1
      else:
        current_pointer+=1
    my_list[lesser_than_pointer],my_list[end]=my_list[end],my_list[lesser_than_pointer]
    quick_sort(my_list,start,lesser_than_pointer-1)
    quick_sort(my_list,lesser_than_pointer+1,end)
  return my_list

# Taking a user input
user_input=input("Enter list of numbers in <no1 no2 no3 ..> format:\n")
my_list=[int(x) for x in user_input.split()]
print(quick_sort(my_list,0,len(my_list)-1)) 
