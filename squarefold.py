c=int(input())
for i in range(c):
     t=int(input())
     
     ans=4
     two=1
     four=1
     for j in range(1,t+1):
          
          two=two*2.0
          
          ans=ans+(1/(two)*(two*two))
          
     print(int(ans)%(10**9 +7))
