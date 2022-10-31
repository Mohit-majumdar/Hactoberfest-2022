t = int(input())
for _ in range(t):
    s = input()
    l = []
    l2 = []
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            l.append(i)
    for i in range(len(s)):
        if i not in l:
            l2.append(s[i])

    print(l)
    print(l2)
