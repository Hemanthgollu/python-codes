#Runner up score
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])
