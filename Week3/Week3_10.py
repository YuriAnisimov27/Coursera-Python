s = input()
first = s.find('f')
last = s.rfind('f')
if first != -1 and last != -1 and first != last:
    print(first, last)
elif first != -1 and first == last:
    print(first)
