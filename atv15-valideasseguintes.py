#numero maior que 3 caracteres
nome=str(input("Digite seu nome: "))
while len(nome) < 3:
    nome=str(input("Digite seu nome: "))
#Idade entre 0 e 150
idade = int(input("Digite sua IDade: "))
while idade > 150 or idade < 0:
    idade = int(input("Digite sua IDade: "))
#Salario MAIOR QUE ZERO:
salario = float(input("informe seu salario: "))
while salario < 0 :
    salario = float(input("informe seu salario: "))
#asexo f ou m
sexo=input("Informa a inicial do seu sexo: ").upper()

while sexo != "F" or sexo != "M":
    sexo=input("Informa a inicial do seu sexo: ").upper()
#estado civil s,c,v,d
estado_civil=input("Digite a inicial do seu estado Civil : ").upper()
while estado_civil != "S" or estado_civil != "C" or estado_civil != "V" or estado_civil != "D":
    estado_civil=input("Digite a inicial do seu estado Civil : ").upper()
