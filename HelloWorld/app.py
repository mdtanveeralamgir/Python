#WHILE LOOP
# index = 1
#
# while index <= 5:
#     print('*' * index)
#     index += 1

#SECRET NUMBER GAME
"""
secretNumber = 12
userInput = int(input('Guess a number: '))
inputCount = 0

while inputCount < 2:
    inputCount += 1
    if userInput > secretNumber:
        print('Too big')
        userInput = int(input('Guess a number: '))
    elif userInput < secretNumber:
        print("Too small")
        userInput = int(input('Guess a number: '))
    else:
        print('You got it.')
        break
else: #Executes only if the while loop condition returns false, if loop breaks before conditon is false then else will not execute
    print('Oops, you ran out of chance')
"""

#HELP GAME
command = ""
prevCommand = ""

while True:
    command = input(f"Enter your command: \n").lower()
    if command == 'start':
        if prevCommand == command:
            print('The car is already on')
        else:
            print('The car has started!')
    elif command == 'stop':
        if prevCommand == command:
            print('The car is already off')
        else:
            print('The car has stopped!')
    elif command == 'help':
        print("""
            > Type 'start' to start the car
            > Type 'stop' to stop the car
        """)
    elif command == 'quit':
        print('bye')
        break
    else:
        print('Sorry I don\'t understand your command, type help to get available commands')

    prevCommand = command