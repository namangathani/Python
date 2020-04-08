i=1
n=int(input())
sum=0
while i<=n:
    sum+=i
    i+=1
avg=sum//n  # '/' is float division and '//' is integer division
print(avg)