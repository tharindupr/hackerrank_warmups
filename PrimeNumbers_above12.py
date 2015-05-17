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
