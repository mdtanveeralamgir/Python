#IF STATEMENT
isHot = False
isClod = True
isSnowing = False

if isHot:
    print("It's a hot day")
elif isClod:
    print("Don't go out")
else:
    print("Pray for sun")
print("Enjoy your day")

#AND OPERATOR
if isHot and isClod:
    print("Error")

#OR OPERATOR
if isHot or isClod:
    print("normal")

#NOT OPERATOR
if isClod and not isSnowing:
    print("Tolerable")