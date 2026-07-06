import array

my_array1 = array.array('i',[1,2,3,4,5])
print(my_array1)
my_array1.insert(0,6) # time complexity O(n)
print(my_array1)
my_array1.insert(3,7) # time complexity O(n)


# array traversal
from array import *
arr1 = array('i',[1,2,3,4,5])
arr2 = array('i',[6,7,8,9,10])
def traverseArray(array):# o(1)
    for i in array:#o(1)
        print(i)

traverseArray(my_array1)


#Accessing array elements
from array import *
arr1 = array('i',[1,2,3,4,5])
def accesElement(array,index):#o(1)
    if index >= len(array):
        print("There is  not any element in this index")
    else:
        print(array[index])
accesElement(arr1,6) # time complexity O(1