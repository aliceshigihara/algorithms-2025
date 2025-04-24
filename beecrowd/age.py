DIAS = int(input())

ANO = DIAS // 365
DIAS %= 365
print(ANO,"ano(s)")

MES = DIAS // 30
MES %= 30
print(MES,"mes(es)")

DIAS = DIAS % 30
print(DIAS,"dia(s)")
