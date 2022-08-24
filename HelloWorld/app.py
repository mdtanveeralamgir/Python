#TUPLES

#Tuples are immutable
"""
num = (1,2,3) #First brakets for tuples
print(num.count(1))
print(num.index(2))

"""

#Unpacking
"""
coordinates = (1,2,3)
x, y, z = coordinates #Each item starting from index 0 - end will assign to x,y,z respectavly
print(y) #prints 2
"""

#Dictionary

customer = {
    "name": "john smith",
    "age": 30,
    "is_verified": True
}

print(customer['name']) #Returns 'keyerror' if key not exists
print(customer.get('age')) #returns None if key does not exists. No error/exception thorwn
print(customer.get('city', 'Montreal')) #prints default value Montreal if city not exists

customer['name'] = "Opel" #assign new value
customer['city'] = 'Brossard' #assign new key value
print(customer['name'])
