#EXCEPTION

"""
Exit code 0 = executed successfully
Exit code 1 = error happened

"""

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError: #Only catching ValueError
    print('Invalid value')
