
def place(arr,m):
    n = len(arr)
    for i in range(n):
        if m <= arr[i]:
            arr.append(0)
            for j in range(n,i,-1):
                arr[j] = arr[j-1]
            arr[i] = m
            break
        elif arr[i] <= m and m <= arr[i+1]:
            arr.append(0)
            for j in range(n,i+1,-1):
                arr[j] = arr[j-1]
            arr[i+1] = m
            break

        else:
            continue

        
    return arr
    
def fun(arr,arr1):
    for i in range(len(arr1)):
        place(arr,arr1[i])
    
    return arr


    
arr = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
print(fun(arr,arr1))
