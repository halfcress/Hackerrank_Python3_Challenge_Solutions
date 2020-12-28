def minion_game(string):
    Stuart = 0
    Kevin = 0
    vovels = "AEIOU"

    for i in range(len(string)):
        if string[i] in vovels:
            Kevin += int(len(s) - i)
        else:
            Stuart += int(len(s) - i)
    if Stuart > Kevin:
        print("{} {}".format("Stuart", Stuart))
    elif Kevin > Stuart:
        print("{} {}".format("Kevin", Kevin))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)