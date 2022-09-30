#Perguntar quantos dolar quer converter em real
valor = float(input("Quantos dolares você quer converter em real: "))
cota = 5.65
real = valor * cota

if valor >= 100:
    desconto= valor * (cota + (cota*0.1))
    print(f"Como você vai converter mais de 100 dolares voce tem um total de 10% de desconto em vez de receber {real} ira receber R${desconto:,.2f}")
else:
    
    print(f"Você vai converter ${valor} em R${real:,.2f}")
