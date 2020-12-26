def binary(a):
    return bin(a).replace("0b", "")


def octa(a):
    return oct(a).replace("0o", "")


def hexa(a):
    return hex(a).replace("0x", "")


def print_formatted(n):
    l1 = len(binary(n))



    for i in range(1, (n + 1)):

            print("{} {} {} {}".format(str(i).rjust(l1), str(octa(i)).rjust(l1), str(hexa(i)).upper().rjust(l1), str(binary(i)).rjust(l1)))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)