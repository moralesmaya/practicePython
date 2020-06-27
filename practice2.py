#Get number from user 
#Calculate if even or odd 
#Use modulus, remainder should be 0 
#Print message 

inputNumber = int(input("Please enter a number: "))

status2 = inputNumber%2
status4 = inputNumber%4
if(status4 == 0):
    print("The number " + str(inputNumber) + " is a multiple of 4")
elif(status2 == 0):
    print("The number " + str(inputNumber)+ " is even!")
else:
    print("The number " + str(inputNumber)+ " is odd!")

#this is a file change