def isPalindrome(n):
    k=n
    sum=0
    while(n>0):
        sum=sum*10+n%10
        n=n//10;
    if(sum==k):
        return True
    else:
        return False
i=999
j=999
max=0
while i>=100:
    j=999
    while j>=100:
        if(isPalindrome(i*j)):
            if(i*j)>max:
                max=i*j
        j=j-1
    i=i-1
print(max)
