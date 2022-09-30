import math

numero = int(input('''Digite um numero
para saber o seu fatorial: '''))
factor = math.factorial(numero)
cont = numero
print(f"Calculando {numero}!: ",end=" ")

for i in range(numero,0,-1):
  print(f"{i}", end=' ')
  print("x" if i > 1 else "=", end=" "  )
  cont -= 1

print(f"{factor}", end=' ')