first=1
second=2
sum=2
while second<10:
    temp=second
    second=first+second
    first=temp
    if(second%2==0):
        sum+=second
print(sum)
    
