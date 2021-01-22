import itertools

x = list(map(int,input().split(" ")))
y = list(map(int,input().split(" ")))

z =list(itertools.product(x,y))

print(*z)
