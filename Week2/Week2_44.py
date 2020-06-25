n = int(input())
count_plus = count_minus = 1
max_count = 1
last_n = n
while n:
    if last_n < n:
        count_plus += 1
        count_minus = 1
        if count_plus > max_count:
            max_count = count_plus
    elif last_n > n:
        count_minus += 1
        count_plus = 1
        if count_minus > max_count:
            max_count = count_minus
    else:
        count_plus = count_minus = 1
    last_n = n
    n = int(input())

print(max_count)
