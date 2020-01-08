
def shift(arr,len):
    for i in range(len):
        if arr[i]%3 == 0:
            len -=1
            for j in range(i,len):
                arr[j] = arr[j+1]
           

    return len

arr = list(map(int,input().split()))
n = len(arr)

n = shift(arr,n)
for i in range(n):
    print(arr[i],end=' ')
