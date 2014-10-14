#100 points

print "What number would you like to find the factors of?"
userInput = int(raw_input ())

for aNumber in range(1,userInput,1):
    if userInput%aNumber == 0:
        print aNumber