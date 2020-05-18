import math
def isPrime(n):
    flag=0
    i=2;
    while i<n:
        if(n%i==0):
            flag=1
            break
        else:
            i=i+1
    if(flag==0):
        return True
    else:
        return False

n = (int)(input())
max = 0
i=2;
while i<=math.sqrt(n):
    if(n%i==0):
      if(isPrime(i)):
          print("prime"+(str)(i))
          if(i>max):
              max=i
      if(isPrime(n//i)):
          print("prime/"+(str)(n//i))
          if(n//i>max):
              max=n//i
          
    i=i+1
print(max)



    

                
