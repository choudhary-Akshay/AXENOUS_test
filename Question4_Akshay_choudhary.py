#python3 code which will input a positive integer n and output the number of divisors of n and sum of those divisors.
n=int(input("Enter positive integer n: "))
sum=0
array=[]
for i in range(1,n+1):
    if(n%i==0):
        sum+=i
        array.append(i)
print("Divisors are as follows:")
for i in range(0,len(array)):
    print(array[i], end=" ")
print("\n Sum of divisors is ",sum)
