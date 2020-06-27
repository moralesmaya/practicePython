#display message to user 
#ask the user for their age 
#take user input and store 
#tell them when they turn 100 
import datetime
#user input step 
age = input("Please enter your age")
currentYear = datetime.datetime.now().year
birthYear = currentYear - int(age)
Yearwhen100 = birthYear + 100
print("You will turn 100 on year:" + str(Yearwhen100))


#calculate when user turns 100 

#calculate current age 
#subtract from current year 

