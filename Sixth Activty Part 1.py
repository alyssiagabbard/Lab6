# 25 points

print "How many numbers do you want to add together?"

userInput = int(raw_input ())
total = 0
for aNumber in range(userInput):
    print "Enter a number:"
    numberEntered = int(raw_input ())
    total = total + numberEntered

print "The answer is " + str (total)

