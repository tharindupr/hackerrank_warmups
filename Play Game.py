sums={}
def summ(i):
          total=0
          
          for k in range(i+1):
               total=total+int(a[k])

               
          return(total)


def do(n):
     if(n<4):
          return(summ(len(a)-1))

     else:
          dp={0:int(a[0]),1:int(a[0])+int(a[1]),2:int(a[0])+int(a[1])+int(a[2])}
          k=3
          while(k<n):
               dp[k]=max((sums[k-1] - dp[k-1] + int(a[k])),(sums[k-2] - dp[k-2] +int(a[k])+int(a[k-1])),(sums[k-3] - dp[k-3] + int(a[k])+int(a[k-1])+int(a[k-2])))

               k+=1

          return(dp[k-1])

         


T=int(input())

for x in range(T):

     N=int(input())

     a=input().split(" ")
     
     a.reverse()
     sums={}
     total=0
     i=0
     for b in a:
          total=total+int(b)
          sums[i]=total
          i+=1


         
     print(do(N))

     
