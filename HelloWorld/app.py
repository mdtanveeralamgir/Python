#STRING
#can use both "" or ''
#but needs to stick with one type

#tripple quotes for multiple lines string

course = '''Hi Jon,
    
    Thank you for your support.
    Thank you
    John'''
# print(course)

#STRING TO CHAR
"""
print(course[0]) #First character from beginning
print(course[-1]) #First character from end
print(course[-2]) #Second last character
print(course[0:3]) #from index 0 to 2
print(course[0:]) #from index 0 to end
print(course[:5]) #from 0 to 4th index
print(course[:]) #from beginning to end
name = 'Tanveer'
print(name[1:-1]) #start from index 1 till the second last char
"""

#FORMATED STRING

"""
first = 'Tanveer'
last = 'Alamgir'

message = f'{first} [{last}] is a coder' #Starts with "f''" and the variables goes inside '' wraped with {}
print(message)
"""

#STRING METHODS
#len is a generic function to get the length of lists
print(len(course)) #length of the str
print(course.upper()) #Uppoer case all char, returns a new string
print(course.find('H')) #returns the index of first occurance of H
print(course.find('Hi')) #returns the index of first occurance of Hi
print(course.replace('Hi', 'Hello'))
print('Thank you' in course) #returns bool if string exists
print(course.title()) #First character of every word is uppercase



