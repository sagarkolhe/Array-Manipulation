
def bignum(arr):
    x = arr[0]
    for i in range(1,len(arr)):
        x = max(x,arr[i])

    return x
        
def max(x,y):
    strx = str(abs(x))
    stry = str(abs(y))
    x = int(strx+stry)
    y = int(stry+strx)
    if x > y:
        return x
    else:
        return y

arr = list(map(int,input().split()))
print(bignum(arr))
