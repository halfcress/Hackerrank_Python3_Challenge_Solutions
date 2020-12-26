def print_rangoli(size):
    import string
    a = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(a[i:size])
        L.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    print('\n'.join(L[:0:-1] + L))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)