def soma (a1,a2,a3):
    operacao = a1 + a2 + a3
    print(f"A soma desses tres numeros são {operacao}")
    return a1, a2, a3

numero1 = float(input("Digite um numero:"))
numero2 = float(input("Digite um numero:"))
numero3 = float(input("Digite um numero:"))

print(soma(numero1,numero2,numero3))
