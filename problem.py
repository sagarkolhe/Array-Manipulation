def solution(arr,x):
    res = []
    for i in range(len(arr) - x):
        if arr[i] >= arr[i+(x-1)]:
            a= []
            for j in range(i,i+x):
                a.append(arr[j])
            res.append(a)

    print(res)


arr = [0,4,10,6,15,9,18,35,40,-30,-90,99]
x = int(input())
solution(arr,x)
