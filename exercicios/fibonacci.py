t1 = False
n1 = 0
n2 = 1
n3 = 0

while not t1:
    try:
        n = int(input("Digite quantos números da sequência de Fibonacci você deseja ver: "))
        t1 = True
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

for i in range(n):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3