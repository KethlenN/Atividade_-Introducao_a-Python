#Kethlen Nunes de Carvalho RA:4251920401

        -(atividade 5.)-

def soma(a, b):
    return a + b
  
def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    resultado = 0
    for _ in range(abs(b)):
        resultado = soma(resultado, a)
    if b < 0:
        resultado = -resultado
    return resultado

def potencia(a, b):
    resultado = 1
    for _ in range(b):
        resultado = multiplicacao(resultado, a)
    return resultado

print("= Calculadora simples =")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Potência")

op = input("Digite o número da operação: ")

if op == "1":
    print("Resultado:", soma(a, b))
elif op == "2":
    print("Resultado:", subtracao(a, b))
elif op == "3":
    print("Resultado:", multiplicacao(a, b))
elif op == "4":
    print("Resultado:", potencia(a, b))
else:
    print("Opção inválida!")
