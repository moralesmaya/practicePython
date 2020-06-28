#x = x + word   ---> x += word 

def reverse(string):
    result = ""
    for letter in range(len(string)):
        result += string[len(string)-1-letter]
        
    return result

userInput = input("Enter a word to check if it's a palindrome: ")

reversedWord = reverse(userInput)
if userInput == reversedWord: 
    print("The word " + userInput + " is a palindrome")