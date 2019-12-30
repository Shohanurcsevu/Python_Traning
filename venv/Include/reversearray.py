arr = [2,4,6,8,10,12,14,16,18,20]
n = 3
r1 = []
r2 = []
r2 = []

for i in range(n,len(arr)):
    r2.append(arr[i])

for j in range (0,n):
    r1.append(arr[j])

r3 =r2+r1
print(r3)
arr = []
t1 = []
t2 = []
result = []
temp = []


def reverse(arr,r):
    temp = arr
    for i in range(r, len(arr)):
        t1.append(arr[i])
    for j in range(0, r):
        t2.append(arr[j])

    return t1+t2




t =int(input())
while t>0:
    n,r=map(int, input().split())
    arr= list(map(int, input().split()))
    result = reverse(arr,r)
    print(list(result))
    t1 = []
    t2 = []
    result = []


    t= t-1


arr = [1,2,3,4,5]
temp= []
for i in range(0,2):
    temp.append(arr[i])


print(list(temp))