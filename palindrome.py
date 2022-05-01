# code to check if a number is palindrome or not.

def ispalindrome(number):
    stringNumber = str(number)
    listNumber = list(stringNumber)
    
    for i,j in zip(range(0,len(listNumber)),range(len(listNumber)-1,0,-1)):

        if listNumber[i] != listNumber[j]:
            return False
        
    return True

print(ispalindrome(1235321))

