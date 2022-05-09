for i in range(int(input())):
    n, k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    x = k%n
    print(*(arr[n-x:]+arr[:n-x]))