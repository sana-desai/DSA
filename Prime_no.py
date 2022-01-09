for i in range(t):
    count=0
    n=int(input())
    j=2
    while j<n:
        if n%j==0:
            count+=1
            break
        j+=1
    if count==0:
        print("prime")
    else:
        print("not prime")
