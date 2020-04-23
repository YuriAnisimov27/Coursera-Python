def Numbers():
    n = int(input())
    if n != 0:
        Numbers()
        print(n)
    if n == 0:
        print(0)


Numbers()
