def rotate(arr,t,n):
        for i in range(0,t):
                rotateleft(arr,n)
        return arr
def rotateright(arr,n):
        temp =  arr[n-1]
        for i in range(0,n-1):
                arr[n-1] = arr[n-2]
                n-=1
        arr[0] = temp
        return arr

def rotateleft(arr,n):
        temp = arr[0]
        for i in range(0,n-1):
                arr[i] = arr[i+1]
        arr[n-1] = temp
        #return arr



n = int(input())
array = []
for i in range(n):
        x = int(input())
        array.append(x)    
#print(rotateright(array,n))
#print(rotateleft(array,n))
print(rotate(array,3,n))
