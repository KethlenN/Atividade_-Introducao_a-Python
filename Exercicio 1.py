#Kethlen Nunes de Carvalho RA: 4251920401

                -(atividade 1.1)-

(Prazo: 14/10)

alunos_notas = []

for i in range(10):
    nome = input(f"Nome do {i+1}º aluno: ")
    nota = float(input(f"Nota do {i+1}º aluno: "))
    alunos_notas.append((nome, nota))

for aluno in alunos_notas:
    print(f"{aluno[0]}: {aluno[1]}")

               -(atividade 1.2)- 

alunos = []

for i in range(10):
    nome = input(f"Nome do {i+1}º aluno: ")
    nota = float(input("Nota: "))
    alunos.append({"nome": nome, "nota": nota})

media = sum(a["nota"] for a in alunos) / len(alunos)

print(f"\nA média das notas é: {media:.2f}")

                -(atividade 1.3)- 

notas = []

for i in range(10):
    nome = input(f"Nome do {i+1}º aluno: ")
    nota = float(input("Nota: "))
    notas.append(nota)

media = sum(notas) / 10

print(f"\nA média das notas é: {media:.2f}")

                 -(atividade 1.4)- 

alunos = []
notas = []

for i in range(10):
    nome = input(f"Nome do {i+1}º aluno: ")
    nota = float(input("Nota: "))
    alunos.append(nome)
    notas.append(nota)

media = sum(notas) / 10
maior = max(notas)
menor = min(notas)

alunos_maior = [alunos[i] for i in range(10) if notas[i] == maior]
alunos_menor = [alunos[i] for i in range(10) if notas[i] == menor]

print("\n- Resultados -")
print(f"Média das notas: {media:.2f}")
print(f"Maior nota: {maior} - Alunos: {', '.join(alunos_maior)}")
print(f"Menor nota: {menor} - Alunos: {', '.join(alunos_menor)}")

                  -(atividade 1.5)- 

nomes = []
notas = []

for i in range(10):
    nomes.append(input(f"Nome do {i+1}º aluno: "))
    notas.append(float(input("Nota: ")))

media = sum(notas) / 10

print(f"\nMédia das notas: {media:.2f}")
print("\nAlunos com nota abaixo da média:")

for i in range(10):
    if notas[i] < media:
        print(f"{nomes[i]} - {notas[i]}")
      
                   -(atividade 1.6)- 

nomes = []
notas = []

for i in range(10):
    nomes.append(input(f"Nome do {i+1}º aluno: "))
    notas.append(float(input("Nota: ")))

media = sum(notas) / 10

print(f"\nMédia das notas: {media:.2f}")
print("\nAlunos com nota maior ou igual à média:")

for i in range(10):
    if notas[i] >= media:
        print(f"{nomes[i]} - {notas[i]}")

