#ACCESSING ITEMS IN LISTS
"""
names = ['opel', 'tanveer', 'alamgir']
print(names[-1]) #prints last item in the list
print(names[-2]) #prints 2nd last item
print(names[0:-1]) #prints from index 0 to the 2nd last. not the last one

"""
#2D LISTS
"""
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for items in range(len(matrix)):
    for item in range(len(matrix[items])):
        print(matrix[items][item])
"""

#APPEND IN LIST

num = [12, 23, 45, 12, 90]
num.append(48) #Append at the end
num.insert(1, 90) #inserted at index 1 and pusehd the rest
num.remove(90) #Remove the item 90
num.pop() #removes the last item from list
print(num.index(23)) #Returns the index of 23
print(12 in num) #Returns true of false
print(num.count(12)) #Returns total occurance of num 12
num.sort() #Does not return anything instead sorts the value in original list. pass by reference
num.reverse() #Desc order
num2 = num.copy() #Simply returns the copy of list
# num.clear() #Remove everything
print(num)