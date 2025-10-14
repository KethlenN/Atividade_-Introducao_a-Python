#Kethlen Nunes de Carvalho RA: 4251920401

            -(atividade 3.1)-
numeros = []

for i in range(10):
    n = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(n)

print("\nNúmeros digitados:", numeros)

             -(atividade 3.2)-

numeros = []

for i in range(10):
    n = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(n)

for i in range(10):
    if numeros[i] < 0:
        numeros[i] = 0

             -(atividade 3.3)-

print("\nVetor com valores alterados (negativos substituídos por 0):")
print(numeros)
