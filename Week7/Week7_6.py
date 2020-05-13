allSchoolchildrenKnow = set()
totalLanguages = set()
n = int(input())
a = int(input())
b = [input() for i in range(a)]
totalLanguages = totalLanguages | set(b)
allSchoolchildrenKnow = set(b)
for i in range(n - 1):
    a = int(input())
    b = [input() for i in range(a)]
    totalLanguages = totalLanguages | set(b)
    allSchoolchildrenKnow = allSchoolchildrenKnow & set(b)
allSchoolchildrenKnow = sorted(allSchoolchildrenKnow)
print(len(allSchoolchildrenKnow))
for i in allSchoolchildrenKnow:
    print(i)
totalLanguages = sorted(totalLanguages)
print(len(totalLanguages))
for i in totalLanguages:
    print(i)
