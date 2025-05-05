ItemCorrespondente, QuantidadeItem = [int(x) for x in input().split(' ')]

CachorroQuente = 1
XSalada = 2
XBacon = 3
TorradaSimples = 4
Refrigerante = 5

if ItemCorrespondente == CachorroQuente:
    ValorTotalCachorroQuente = QuantidadeItem * 4
    print(f"Total: R$ {ValorTotalCachorroQuente:.2f}")

if ItemCorrespondente == XSalada:
    ValorTotalXSalada = QuantidadeItem * 4.50
    print(f"Total: R$ {ValorTotalXSalada:.2f}")

if ItemCorrespondente == XBacon:
    ValorTotalXBacon = QuantidadeItem * 5
    print(f"Total: R$ {ValorTotalXBacon:.2f}")

if ItemCorrespondente == TorradaSimples:
    ValorTotalTorrada = QuantidadeItem * 2
    print(f"Total: R$ {ValorTotalTorrada:.2f}")

if ItemCorrespondente == Refrigerante:
    ValorTotalRefrigerante = QuantidadeItem * 1.50
    print(f"Total: R$ {ValorTotalRefrigerante:.2f}")
