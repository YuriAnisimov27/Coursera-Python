s = input()
indexFirst = s.find('h')
indexLast = s.rfind('h')
print(s[:indexFirst + 1],
      s[indexFirst + 1:indexLast] * 2, s[indexLast:], sep='')
