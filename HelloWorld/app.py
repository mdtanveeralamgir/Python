#WHILE LOOP
# index = 1
#
# while index <= 5:
#     print('*' * index)
#     index += 1

#SECRET NUMBER GAME

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
