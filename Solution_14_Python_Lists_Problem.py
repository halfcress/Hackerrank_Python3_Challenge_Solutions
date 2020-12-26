if __name__ == '__main__':
    directlist = []


    def ekleme(list, x):
        list.append(x)


    N = int(input())
    for _ in range(N):
        islem = input().split()
        if islem[0] == "insert":
            x = int(islem[1])
            y = int(islem[2])
            directlist.insert(x, y)
        elif islem[0] == "print":
            print(directlist)
        elif islem[0] == "remove":
            x1 = int(islem[1])
            directlist.remove(x1)
        elif islem[0] == "append":
            x2 = int(islem[1])
            directlist.append(x2)
        elif islem[0] == "sort":
            directlist.sort()
        elif islem[0] == "reverse":
            directlist.reverse()
        elif islem[0] == "pop":
            directlist.pop()