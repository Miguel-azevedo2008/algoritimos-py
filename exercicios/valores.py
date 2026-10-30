soma = 0
media = 0
valoresnull = 0
somapar = 0

while True:
    try:
        n = int(input("Digite um número inteiro: "))
        if n <= 0:
            print("Por favor, digite um número inteiro positivo.")
            continue
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

for i in range(n):
    while True:
        try:
            valor = float(input(f"Digite o valor {i + 1}: "))
            break
        except ValueError:
            print("Por favor, digite um valor válido.")
    soma += valor
    if valor == 0:
        valoresnull += 1
    if valor % 2 == 0:
        somapar += valor

media = soma / n if n > 0 else 0
print(f"A soma dos valores é: {soma}")
print(f"A média dos valores é: {media}")
print(f"A quantidade de valores nulos é: {valoresnull}")    
print(f"A soma dos valores pares é: {somapar}")