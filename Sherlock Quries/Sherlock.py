def cal(arr):
     dic={}
     j=0
     
     for i in arr:
          try:
               dic[i].append(j)
          except:
               dic[i]=[]
               dic[i].append(j)
          j+=1
          
     return(dic)   

#f=open("Input.txt","r")
NM=input().split(" ")#f.readline().split(" ")
N=int(NM[0])
M=int(NM[1])
A=input().split(" ") #f.readline().split(" ")
B=input().split(" ") #f.readline().split(" ")
C=input().split(" ") #f.readline().split(" ")
#A[99999]=A[99999][:-1]
#B[99999]=B[99999][:-1]
#C[99999]=B[99999][:-1]

l=cal(B)

counti=0
for i in B:
     Bi=int(i)
     count=1
     
     while(True):
          #if(Bi==1):
              # A = [x * int(C[counti]) for x in A]
          if(Bi*count<=N):
               A[Bi*count-1]=str((int(A[Bi*count-1])*int(C[counti])%(10**9+7)))
               count+=1
          
          
          else:
               break
     counti+=1
          
print(' '.join(A))
