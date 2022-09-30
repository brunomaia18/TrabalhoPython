count = 1
soma = 0
nome = input("Digite o seu nome :")
while count <=4: 
    nota = float(input(f"Digite a nota do seu {count}º Bimestre: "))
    count +=1
    soma += nota
media = soma/4
print(f"{nome} a sua media foi {media}")

