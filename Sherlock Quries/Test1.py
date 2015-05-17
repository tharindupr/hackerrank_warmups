f=open("Input.txt","r")
NM=f.readline().split(" ")
N=int(NM[0])
M=int(NM[1])
A=f.readline().split(" ")
B=f.readline().split(" ")
C=f.readline().split(" ")
A[N-1]=A[N-1][:-1]
B[M-1]=B[M-1][:-1]
C[M-1]=C[M-1][:-1]

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

l=cal(B)

counti=0
for i in l:
     Bi=int(i)
     count=1
     
     while(True):
          
          if(Bi*count<=N):

               for j in l[i]:
                    print(j)                    
                    #A[Bi*count-1]=str((int(A[Bi*count-1])*int(C[int(l[i][0])])%(10**9+7)))
          
          
          
          else:
               break
          count+=1
     counti+=1
          
#print(' '.join(A))

