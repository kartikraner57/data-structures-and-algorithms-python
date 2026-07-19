myList = ["a","b","c","d","e"]
print(myList)
myList[0:2] = ["x","y"]
print(myList[:])


# pop
print(myList)
print(myList.pop(1))
print(myList)

# delete
del myList[1]
print(myList)
del myList[1:3]
print(myList)

#remove
myList.remove("e")
print(myList)

#clear
myList.clear()
print(myList)