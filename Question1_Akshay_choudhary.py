#Python code for question 1
#string = "BOOKKEEPER"
string = input("enter a string:")
new={}

newstring=""

for i  in string:
    if i in new:
        new[i]+=1
    else:
        new[i]=1


for i  in string:
    if new[i] == 2:
        newstring+="Z"
    elif new[i] >2:
        newstring+="X"
    else:
        newstring+=i
   
print(newstring,"\n")
