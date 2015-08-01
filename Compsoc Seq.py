in1=raw_input().split(" ")
x=int(in1[0])
y=int(in1[1])
n=int(input())

abc=[x,y]
dic2={}
if(x==0 and y==0):
     print(0)
else:
     for i in range(3,n+1):
          temp=abc[1]
          abc[1]=abc[1]-abc[0]
          abc[0]=temp
          

     print(abc[1]% 1000000007)
