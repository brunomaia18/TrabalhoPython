#Perguntar quantos dolar quer converter em real
valor = float(input("Quantos dolares você quer converter em real: "))
converter = valor * 5.26

if valor >= 100:
    desconto= valor * 5.78
    print(f"Como você vai converter mais de 100 dolares voce tem um total de 10% de desconto em vez de receber {converter} ira receber R${desconto}")
else:
    print(f"Você vai converter ${valor} em R${converter:,.2f}")