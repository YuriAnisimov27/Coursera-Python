for i in range(10, 100):
    if i == (i % 10) * (i // 10) * 2:
        print(i)
