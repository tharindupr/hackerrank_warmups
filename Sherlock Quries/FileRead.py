

f=open("Input1.txt","r")
NM=f.readline().split(" ")
N=int(NM[0])
M=int(NM[1])
A=f.readline().split(" ")
B=f.readline().split(" ")
C=f.readline().split(" ")
A[N-1]=A[N-1][:-1]
B[M-1]=B[M-1][:-1]
C[M-1]=C[M-1][:-1]

counti=0
for i in B:
     Bi=int(i)
     count=1
     
     while(True):
          if(Bi*count<=N):
               A[Bi*count-1]=str(int(A[Bi*count-1])*int(C[counti]))
               count+=1
          
          
          else:
               break
     counti+=1
          
#print(' '.join(A))
