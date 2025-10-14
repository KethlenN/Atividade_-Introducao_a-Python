#Solicitando 10 números inteiros para o usuário
numeros = []
numeros.append(int(input("Digite um número inteiro: ")))
for n in range(1, 10):
  numeros.append(int(input("Digite mais um número inteiro: ")))

#Solicitando um número inteiro para verificar se está na lista
numero = 0
numero = int(input("Digite um número inteiro para verificar se ele está na lista: "))

#Verificando se está na lista e informando ao usuário
if numero in numeros:
  posicao = numeros.index(numero+1)
  print(f"Parabéns! O número {numero} está na {posicao}° posição da lista dos números! :)")
else:
  print(f"Infelizmente, o número {numero} não está na lista dos números. :(")
