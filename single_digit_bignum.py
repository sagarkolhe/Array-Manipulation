
def assemble(num):
    a = []
    rem = 0
    while num > 0:
        rem = num%10
        a.append(rem)
        num = num//10
    a.sort()
    print(a)
    a.reverse()
    temp = 0
    if a[len(a)-1]%2 != 0:
        temp = a[len(a)-1]
        a[len(a)-1] = a[len(a)-2]
        a[len(a)-2] = temp
        
        
        
    res = 0
    for i in a:
        res = res*10 + i
    print(res)
num = int(input())
assemble(num)
