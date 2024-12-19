print("enter a number")
n=int(input())
l=[]
def isprime(a):
    c=0
    for i in range(2,a+1):
        if a%i==0:
            c+=1
    return c==1
for i in range(2,n+1):
    if n%i==0:
        if isprime(i):
            l.append(i)
print(l)
