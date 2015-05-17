import time
temp=[]
N=input()
for j in range(int(N)):
    temp.append(input())
 
     
#start=time.time()
data=dict(a=2,b=22,c=222,d=3,e=33,f=333,g=4,h=44,i=444,j=5,k=55,l=555,m=6,n=66,o=666,p=7,q=77,r=777,s=7777,t=8,u=88,v=888,w=9,x=99,y=999,z=9999)
data[" "] = 0
 
 
def converter(string):
     
    str1=string
    str2=""
    lst=[]
    index=0
 
    for i in str1:
        lst.append(data[i])
    if len(string)==1:
        str2+=str(lst[0])
 
    for j in range (len(str1)-1):
        A=str(lst[index])
        if index==0:
            str2+=A
        index+=1
        B=str(lst[index])
 
        if (A[0]==B[0]):
            str2+= str (" ")
        str2+=B
    return str2
     
 
case=1
while (len(temp) > 0):
     
    print("Case #" + str(case) + str(" : ") + str(converter(temp.pop(0))))
    case+=1
     
#end=time.time()
 
#print("time =",end - start)
