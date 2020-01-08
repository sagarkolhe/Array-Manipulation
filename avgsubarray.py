def avg(arr,k,n):
    maxavg = 0
    minavg = 0
    for l in range(k):
        minavg += arr[l]
        
    for i in range(0,n-k+1):
        max = 0
        for j in range(i,i+k):
          max += arr[j]
    
        if(max >= maxavg):
            maxavg = max
        elif(minavg >= max):
            minavg = max
    return maxavg,minavg
    





arr = list(map(int,input().split()))
k = int(input())
n = len(arr)
M,m = avg(arr,k,n)
print("the maxavg is",M)
print("the minavg is",m)
