if __name__ == '__main__':
    import itertools

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    liste = list()

    for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                if (i + j + k != n):
                    ekle = [i, j, k]
                    liste.append(ekle)

print(liste)
