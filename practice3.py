#retrieve list 
#Write program that prints numbers less than 5

numberList =  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
resultsList = []
for x in numberList:
    if x < 5: 
        resultsList.append(x)
    
print(resultsList)