##definindo como vai começar 
lados = 0
soma = 0
while lados < 4:
    #Perguntando os 4 lados do triangulo
    lado1 = float(input("Digite o lado do Retângulo : "))
    #vai somar o lados que começa com zero a cada repetiçao
    lados += 1
    #Somando cada lado dito pelo cliente
    soma += lado1
print(f"A soma do perimetro é {soma}")