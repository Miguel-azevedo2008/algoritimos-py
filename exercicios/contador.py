m = False

while not m:
    try:
        n1 = int(input("Digite o número inicial: "))
        n2 = int(input("Digite o número final: "))
        m = True
    except ValueError:
        print("Por favor, digite números inteiros válidos.")

if n1 <= n2:
    for i in range(n1, n2 + 1):
       print(i)
else:
    for i in range(n1, n2 - 1, -1):
        print(i)