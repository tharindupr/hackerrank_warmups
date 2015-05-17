def decrypt(num):
    a=list(num)
    b=[]
    for k in range(0,len(a)):
        b.append(0)
     
    if len(a)>1:
        if a[1]==a[0]:
            b[1]=1
             
        else:
            b[1]=0
        b[0]=1
         
    i=2
    while(i<len(a)):
        if b[1]==1:
            #all similar symbols
            if checkSimilar(a[0:i])==True:
                if a[i]==a[i-1]:
                    b[i]=1
                else:
                    b[i]=0
                 
            #different
            else:
                #look for matches in [0:i]
                index=match(a[i],a[0:i])
                if index !=None:
                    b[i]=b[index]
                else:
                    b[i]= max(b[0:i])+1
                 
 
        elif b[1]==0:
            index=match(a[i],a[0:i])
            if index !=None:
                b[i]=b[index]
            else:
                b[i]= max(b[0:i])+1
        i+=1
     
    print(convert(b))
         
        
             
 
def checkSimilar(array):
    count=0
    for i in range(0,len(array)-1):
        if array[i]==array[i+1]:
            count+=1
    if count==len(array)-1:
        return True
    else:
        return False
             
             
             
 
 
def match(num,arr):
    for x in arr:
        if num==x:
            return arr.index(x)
 
def convert(arr):
    b=max(arr)+1
    i=0
    summ=0
    arr=reversed(arr)
    for x in arr:
        summ=summ+(x*(b**i))
        i+=1
    return summ
         
while(True):
    decrypt(input().strip())    
