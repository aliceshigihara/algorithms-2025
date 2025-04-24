renda = float(input())
devido = 0

if (renda > 4500):
    devido += (renda - 4500) * 0.28
    renda = 4500

if (renda > 3000):
    devido += (renda - 3000) * 0.18
    renda = 3000

if (renda > 2000):
    devido += (renda - 2000) * 0.08
    renda = 2000

if devido == 0:
    print("Isento")

else:
    print(f"R$ {devido:.2f}")
