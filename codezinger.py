def duplicate(arr):  #function for duplicate elements 
    final = []
    res = []
    for i in range(len(arr)):
        if arr[i] not in final:
            final.append(arr[i])
            
        else:
            res.append(arr[i])
            
    print(res)


def uniq(line):
    dict = {}
    for i in line:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    print(str(dict))


def freq(arr):
    freq = {}
    one = []
    for item in arr:
        if (item in freq):
            freq[item] +=1
        else:
            freq[item] = 1

    for key, value in freq.items():
        if value > 1:
            one.append(key)
    print(one)
            


arr = list(map(int, input().split()))
#duplicate(arr)
line = "sagar"
#uniq(line)
freq(arr)

