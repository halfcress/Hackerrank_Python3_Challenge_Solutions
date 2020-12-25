if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    x = sorted(set(arr))

    x = list(x)

    print(x[-2])
