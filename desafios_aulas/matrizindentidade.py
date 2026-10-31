matriz = []
while True:
    try:
        ordem = int(input("Digite a ordem da matriz: "))
        if ordem <= 0:
            print("A ordem da matriz deve ser um número positivo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

for i in range(ordem):
    linha = []
    for j in range(ordem):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()