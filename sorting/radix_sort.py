# Radis sort function
def radix_sort(my_list):
  if len(my_list)<=1:
    return my_list
  else:
    max_in_list=max(my_list)
    exponent=len(str(max_in_list))
    copy_my_list=my_list[:]
    for i in range(exponent):
      position=-(i+1)
      print("position"+str(position))
      digits=[[] for j in range(0,10)]
      for element in copy_my_list:
        element_str=str(element)
        try:
          digit_str=element_str[position]
          digit=int(digit_str)
        except:
          digit=0 
        digits[digit].append(element)
      copy_my_list=[]
      for numbers in digits:
         copy_my_list.extend(numbers)
    return copy_my_list

# user input request
user_input=input("Enter the list of +ve numbers to sort in <no1 no2 no3> format:\n")
my_list=[int(x) for x in user_input.split()]
print(radix_sort(my_list))
