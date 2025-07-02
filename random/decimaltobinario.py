x = int(input("digite um numero decimal: "))
l = []

while x > 0:
    r = x % 2
    l.append(r)
    x = x // 2

l.reverse()
print(l)