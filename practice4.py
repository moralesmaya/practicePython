#get number from user 
#print list of all divisors of that number 

def userinput():
    number = input("Please enter a number: ")
    return number

def findDivisors(inputNumber):
    results = []
    allNumbers = range(2,inputNumber)
    for value in allNumbers:
        if inputNumber%value == 0: 
            results.append(value)
    return results

userinput = userinput()

divisors = findDivisors(userinput)
print(divisors)
