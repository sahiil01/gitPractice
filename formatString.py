#10000000 format string to 10,000,000

def formatString(number):
    stringNumber = str(number)
    numberList = list(stringNumber)

    returnList = numberList
    counter = 1
    
    for index in range(len(numberList)-1,0,-1):
        
        if counter % 3 == 0:
            returnList.insert(index,',')
        
        counter += 1 

    return ''.join(returnList)
    
    
print(formatString(458965236))

