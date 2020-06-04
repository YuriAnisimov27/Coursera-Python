a = float(input())
n = int(input())


def power(a, n):
    answer = a
    for i in range(abs(n) - 1):
        answer *= a
    if n > 0:
        return answer
    elif n == 0:
        return 1
    else:
        return 1 / answer


print(power(a, n))
