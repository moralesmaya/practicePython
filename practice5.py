#take 2 lists
#write program that returns commmon numbers between lists 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  

def findCommonElements(list1,list2):
    commonElements = []
    for value in list1:
        if value in list2:
            if value not in commonElements:
                commonElements.append(value)
            
    return commonElements

commonNumbers = findCommonElements(a,b)
print(commonNumbers)