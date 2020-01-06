def seclar(arr):
    max = arr[0]
    secmax = 0
    result=[]
    for i in range(1,len(arr)):
        if arr[i] > max:
            secmax = max
            max = arr[i]
    return secmax,max



arr = list(map(int,input().split()))

secmax,max = seclar(arr)
print("max no is ",max)
print("secmax no is ",secmax)
