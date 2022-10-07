numero = int(input("Digite um numero para ver a tabuada : "))
count = 0
print(f"{numero} X 0 = 0")
for c in range(1,11):
    multi = numero*c
    count = count + 1
    print("{} X {} = {}".format(numero,count,multi)) 
