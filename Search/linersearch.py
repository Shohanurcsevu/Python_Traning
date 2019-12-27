def search(arrget, d):

    for v in range(len(arrget)):
        if arrget[v] == d:
            return v

    return -1



t = int(input())

while t > 0:
    n,x=map(int, input().split())
    arr=list( map(int,input().split()))


    print(search(arr, x))

    t = t - 1


