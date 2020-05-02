def xor(x, y):
    if x != y:
        return True
    else:
        return False


x, y = int(input()), int(input())
xor(x, y)
if xor(x, y):
    print('1')
else:
    print('0')
