def john(N):
    if N<4:
        return 1   
    else:
        f=john(N-4)+ john(N-1)
        return f
         
 
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
 
def output(m):
    tot=0
    n=1
    while(n<m):
        if(isPrime(n)==True):
            tot=tot+1
            n=n+1
        else:
            n=n+1
    print(tot)
 
def prob():
    a=int(input())
    b=0
    while(a!=b):
        m=int(input())
        f=john(m)
        output(f)
        b=b+1
 
prob()        
 
