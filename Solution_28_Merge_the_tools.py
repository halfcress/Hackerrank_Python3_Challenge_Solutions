def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        a = string[i:i + k]
        ozan = ""
        for j in a:
            if j not in ozan:
                ozan += j
        print(ozan)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)