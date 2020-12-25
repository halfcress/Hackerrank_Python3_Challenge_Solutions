if __name__ == '__main__':
    n = int(input())

    analiste = list()

    for i in range((n + 1)):
        analiste.append(i)

    analiste.remove(0)
    anastring = ''.join(str(i) for i in analiste)

    print(anastring)
