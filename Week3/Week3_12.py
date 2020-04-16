s = input()
a = s[s.find('f') + 1:]
index = a.find('f')
if s.find('f') == -1:
    print(-2)
elif index == -1:
    print(-1)
elif index != -1:
    print(index + len(s[:s.find('f') + 1]))
