integers = [1,2,3,4]
print(integers)
stringlist = ['a','b','c','d']
print(stringlist)
mixedlist = [1,2,3,'a','b','c']
print(mixedlist)
nestedlist = [[1,2,3],[4,5,6],[7,8,9]]
print(nestedlist)
emptylist = []
print(emptylist)

# Accessing elements in a list
shoppingList = ['milk','bread','eggs','butter']
print(shoppingList[0])
print(shoppingList[1])

print("milk" in shoppingList)
print(shoppingList[-1])


for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
empty = []
for i in empty:
   print('I an empty list')

#    updating elements in a list and inserting elements in a list
mylist = [1,2,3,4,5]
print(mylist)
mylist[2] =33
mylist[4] = 55
print(mylist)

#insert an element in a list
myList= [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)
print(myList)

#appending an element in a list
myList.append(65)
print(myList)
#extending a list with another list
myList.extend([100,200,300])
newLIst = [11,12,13,15]
myList.extend(newLIst)
print(myList)

#removing elements from a list