#Python3 code for retrieving the positions of numbers which are divisible by 2. 
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

positionOfNumbers=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        positionOfNumbers.append(i)
        
# Note: prinitng actual positions of numbers not positions according to array index.
print("The positions of Numbers divisible by 2 are \n")   
for i in  positionOfNumbers:
    print(i+1,end=" ")
print("\n")
