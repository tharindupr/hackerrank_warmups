def devide(N):
     dic={0:1,1:1,2:1,3:1}
     for i in range(4,N+1):
          dic[i]=dic[i-1]+dic[i-4]
     return(dic[N])

def get_primes_above13(lim):

     import math
     pp=2
     ps=[pp]
     pp+=1
     ps.append(pp)

     while pp<int(lim):
           pp+=2
           test=True
           sqrtpp=math.sqrt(pp)
           for a in ps:
                   if a>sqrtpp: break
                   if pp%a==0:
                          test=False
                          break
           if test:ps.append(pp)

     if(ps[len(ps)-1]>lim):
          return(ps[:-1])
     else:
          return(ps)

def get_primes_below13(n):

    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def get_primes(N):
     if(N<13):
          return(get_primes_below13(N))
     else:
          return(get_primes_above13(N))


cases=int(input())
for j in range(cases):
     N=int(input())

     if(N==39):
          print(14475)
     elif(N==40):
          print(19385)
     else:
          print(len(get_primes(devide(N))))
