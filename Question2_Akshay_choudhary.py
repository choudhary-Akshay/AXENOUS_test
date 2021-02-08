#Python3 code for finding number of small and capital letters in string and replace all capital letters by same small letter and all small letters by same capital letters.

string = "EduCatiON"
#comment above line and uncomment line after this text to check output for user entered strings.
#string = input("Enter a string: ")
newString=""

for i  in string:
    if (i.isupper()) == True:
        newString+=(i.lower()) 
    elif (i.islower()) == True:
        newString+=(i.upper())
    
print (newString)
