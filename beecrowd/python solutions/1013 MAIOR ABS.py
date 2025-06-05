A= int(input())
B= int(input())
C= int(input())

MAIORabs= (A + B + abs(A - B))//2

if C < MAIORabs:
    print(MAIORabs,"eh o maior")

if MAIORabs < C:
    print(C,"eh o maior")
