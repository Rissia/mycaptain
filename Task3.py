a=0
b=1
n=eval(input("Enter number of numbers in fibanocii:"))
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
