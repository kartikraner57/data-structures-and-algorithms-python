# list operation and funtion
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

#
a = [0,1]
a = a * 4
print(a)

a = [0,1,2,3,4,5,6,7,8,9]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))

#)
total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

#
my_List = list()
total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)
#
myList = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    myList.append(value)

average = sum(myList) / len(myList)
print('Average:', average)
