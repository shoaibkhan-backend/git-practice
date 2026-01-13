n=int(input("Enter a number:"))
p=n
s=0
while p>0:
    r=p%10
    s=s+r*r*r
    p=p//10
if s==n:
    print("Armstrong Number:")
else:
    print("Not Armstrong Number:")