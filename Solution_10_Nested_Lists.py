if __name__ == '__main__':
    analiste=[]
    for _ in range(int(input())):
        isim = input()
        puan = float(input())
        analiste.append([puan, isim])

    analiste.sort()
    b = [i for i in analiste if i[0] != analiste[0][0]]
    c = [j for j in b if j[0] == b[0][0]]


for i in range(len(c)):
    print(c[i][1])