N=int(input())
S=input()

counts={}
total=0


for j in range(0,N-2):
     counts['S']=0
     counts['C']=0
     #print(j)
     for i in range(j,N):
          if(S[i]=='C'):
               counts['C']+=1
     
          if(S[i]=='S'):
               counts['S']+=1

          if((i+1-j)%3==0 and counts['S']!=0 and (counts['C']/counts['S']==2) ):
               total+=1
          
print(total)     


