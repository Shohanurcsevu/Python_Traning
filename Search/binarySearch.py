def bin_search(arr, left, high, key):
    # Code here
    while left <= high:
        mid = left + (high - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            high = mid - 1

    return -1


t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    print(bin_search(arr, 0, len(arr) - 1, k))
    t = t - 1



{
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        x=int(input())
        print (bin_search(arr, 0, 0, x))
}
