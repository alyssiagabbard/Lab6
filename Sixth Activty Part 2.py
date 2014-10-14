# 50 points
print "How many numbers do you want to add together?"

totalList = []

userInput = int(raw_input())

for numberTotal in range(userInput):
    print "Enter a number, please:"
    theNumbers = int(raw_input ())
    totalList.append (theNumbers)

print "Your answer is: " + str(sum(totalList))