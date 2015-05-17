H=int(input())
M=int(input())

numbers=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven',
         'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty',
         'twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight',
         'twenty nine']
if(M==0):
     print(numbers[H]+" o' clock")
elif(M<30):
     if(M==1):
          print(numbers[M]+" minute past "+numbers[H])
     elif(M==15):
          print("quarter past "+numbers[H])
     else:
          print(numbers[M]+" minutes past "+numbers[H])
elif(M==30):
     print("half past "+numbers[H])
else:
     R=60-M
     if(R==1):
          print(numbers[R]+" minute to "+numbers[H+1])
     elif(R==15):
          print("quarter to "+numbers[H+1])
     else:
          print(numbers[R]+" minutes to "+numbers[H+1])
     
