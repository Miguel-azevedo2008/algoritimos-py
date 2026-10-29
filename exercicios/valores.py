t1 = False
soma = 0
media = 0
valoresnull = 0
somapar = 0

while not t1:
    try:
        n = int(input("Digite um número inteiro: "))
        t1 = True
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

for i in range(n):
    t2 = False
    while not t2:
        try:
            valor = float(input(f"Digite o valor {i + 1}: "))
            t2 = True
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