n=int(input("Enter number of terms:"))
a=0
b=1
c=0
print("fibonacci_series is :")
print(a)
print(b)
c=a+b
while c<n:
    print(c)
    a=b
    b=c
    c=a+b