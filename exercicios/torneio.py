times = []
t1 = False

while not t1:
    try:
        n = int(input("Digite o número de times: "))
        t1 = True
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

for i in range(n):
    time = input(f"Digite o nome do time {i + 1}: ")
    times.append(time) 

i = 0
while i < n:
    for j in range(n):
        if times[j] != times[i]:
            print(f"{times[i]} x {times[j]}")
    i += 1