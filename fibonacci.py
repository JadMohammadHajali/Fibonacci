n=int(input("Enter the value of n : "))
num1=0
num2=1

for i in range(n):
    print(num1,end=' ')
    next= num1+num2
    num1=num2
    num2=next

