#Created by Elshad Karimov on 04/04/2020.
from array import *


4 #1. Create an array and traverse.
my_array = array('i',[1,2,3,4,5])
for i in my_array:
    print(i)    

5 #2. Access individual elements through indexes
print("step 2")
print(my_array[0])
print(my_array[3])
#3. Append any value to the array using append() method
print("step 3")
my_array.append(6)
print(my_array  )
#4. Insert value in an array using insert() method
print("step 4")
my_array.insert(0,11)
print(my_array)
8 #5. Extend python array using extend() method
print("step 5")
my_array1 = array('i',[7,8,9])
my_array.extend(my_array1)
print(my_array)
#6. Add items from list into array using fromlist() method
print("step 6")
temp_list = [10,11,12]
my_array.fromlist(temp_list)
print(my_array)
#7. Remove any array element using remove() method
print("step 7")
my_array.remove(11)
print(my_array)
11 #8. Remove last array element using pop() method
print("step 8")
my_array.pop()
print(my_array)
#9. Fetch any element through its index using index() method
print("step 9")
print(my_array.index(3))
print(my_array.index(5))
13 #10. Reverse a python array using reverse() method
print("step 10")
my_array.reverse()
print(my_array)

#11. Get array buffer information through buffer_info() method
print("step 11")
print(my_array.buffer_info())
15

#12. Check for number of occurrences of an element using count() method
print("step 12") 
my_array.append(11)
print(my_array.count(11))
print(my_array)
16 # 13. Convert array to string using tostring() method
# print("step 13")
# strTemp = my_array.tostring()
# print(strTemp)
# ints = array('i')
# ints.fromstring(strTemp)   
# print(ints)

# 14. Convert array to a python list with same elements using tolist() method
print("step 14")
print(my_array.tolist())

#15. Append a string to char array using fromstring() method

19

#16. Slice Elements from an array
Print("step 16")
print(my_array[1:4])