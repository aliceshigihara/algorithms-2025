salario = float(input())

if salario >= 0 and salario <= 400:
    percentual = 15
    porcentagem = (salario/100) * percentual
    total_salario = salario + porcentagem
    print(f"Novo salario: {total_salario:.2f}")
    print(f"Reajuste ganho: {porcentagem:.2f}")
    print("Em percentual:",percentual,"%")

if salario >= 400.01 and salario <= 800:
    percentual = 12
    porcentagem = (salario/100) * percentual
    total_salario = salario + porcentagem
    print(f"Novo salario: {total_salario:.2f}")
    print(f"Reajuste ganho: {porcentagem:.2f}")
    print("Em percentual:",percentual,"%")

if salario >= 800.01 and salario <= 1200:
    percentual = 10
    porcentagem = (salario/100) * percentual
    total_salario = salario + porcentagem
    print(f"Novo salario: {total_salario:.2f}")
    print(f"Reajuste ganho: {porcentagem:.2f}")
    print("Em percentual:",percentual,"%")

if salario >= 1200.01 and salario <= 2000:
    percentual = 7
    porcentagem = (salario/100) * percentual
    total_salario = salario + porcentagem
    print(f"Novo salario: {total_salario:.2f}")
    print(f"Reajuste ganho: {porcentagem:.2f}")
    print("Em percentual:",percentual,"%")

if salario > 2000:
    percentual = 4
    porcentagem = (salario/100) * percentual
    total_salario = salario + porcentagem
    print(f"Novo salario: {total_salario:.2f}")
    print(f"Reajuste ganho: {porcentagem:.2f}")
    print("Em percentual:",percentual,"%")
