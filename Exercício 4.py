#Solicitando os 6 números da Mega Sena
numeros = []
print("Digite os 6 números da Mega Sena")
for n in range(1, 7):
  numeros.append(int(input(f"Número {n}: ")))

#Solicitando os números do jogo
aposta = []
print("Digite os 6 números da sua aposta")
for n in range(1, 7):
  aposta.append(int(input(f"Número {n}: ")))

#Calculando a quantidade de pontos do jogo
pontos = 0
for a in aposta:
  if a in numeros:
    pontos += 1
if pontos == 6:
  print("VOCÊ GANHOU NA MEGA SENA!!!")
elif pontos > 1:
  print(f"Parabéns! Você acertou {pontos} pontos! :)")
elif pontos == 1:
  print(f"Parabéns! Você acertou {pontos} ponto! :)")
else:
  print("Não foi desa vez! Infelizmente, você não acertou nenhum número. :(")
