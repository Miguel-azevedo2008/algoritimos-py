n1 = 0
n2 = 1
n3 = 0

while True:
    try:
        n = int(input("Digite quantos números da sequência de Fibonacci você deseja ver: "))
        if n <= 0:
            print("Por favor, digite um número inteiro positivo.")
            continue
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

for i in range(n):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3