#the most easy solution is this 
"""
    miss = sum(range(1,n+1)) - sum(arr)
    return miss
"""


def missing (arr,n):

    tot = 0
    for i in range(len(arr)):
        tot = tot + arr[i]
   

    sum1 =0
    for i in range (n+1):
        sum1 = sum1 + i 
   
    miss = sum1 - tot

    return miss
    
n =10
arr = [1,2,3,5,6,7,8,9,10]
print(missing(arr,n))

