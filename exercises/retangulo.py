l =  int(input("qual será a largura?: "))
a = int(input("qual será a altura?: "))

x = 1

print('+' + ('-' * (l-2) + '+'))

while x <= a-2:
    print('|' + (' ' * (l-2)) + '|')
    x += 1

print('+' + ('-' * (l-2) + '+'))