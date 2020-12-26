if __name__ == '__main__':
        N, M = map(int, input().split(" "))

        for i in range(N):
                pattern = ".|."
                if i < (N-1)/2:
                        print((pattern * (2*i+1)).center(M, "-"))
                elif i == (N-1)/2:
                        print("WELCOME".center(M, "-"))
                else:
                        print((pattern * (2*(N-1-i)+1)).center(M, "-"))