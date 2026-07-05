import array

my_array1 = array.array('i',[1,2,3,4,5])
print(my_array1)
print(f"Initial array: {my_array1}")
my_array1.insert(0,6) # time complexity O(n)
print(my_array1)
print(f"After inserting 6 at index 0: {my_array1}")
my_array1.insert(3,7) # time complexity O(n)
print(f"After inserting 7 at index 3: {my_array1}")


# array traversal
from array import *
arr1 = array('i',[1,2,3,4,5])
arr2 = array('i',[6,7,8,9,10])
def traverseArray(array):
    for i in array:
def traverse_array(arr):
    """
    This function traverses through an array and prints each element.
    Time complexity: O(n)
    """
    for i in arr:
        print(i)

traverseArray(my_array1)
if __name__ == "__main__":
    print("\nTraversing the array:")
    traverse_array(my_array1)