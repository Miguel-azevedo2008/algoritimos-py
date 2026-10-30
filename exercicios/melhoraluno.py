import math
melhoraluno = ""
maiornota = -1
na = 0

while True:
    try:
        na = int(input("Digite o número de alunos: "))
        if na <= 0:
            print("Por favor, digite um número inteiro positivo.")
            continue
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

for i in range(na):
    while True:
        try: 
            nome = input(f"Digite o nome do aluno {i + 1}: ")
            nota = float(input(f"Digite a nota do aluno {i + 1}: "))
            if not math.isfinite(nota):
                print("A nota precisa ser um número finito.")
                continue
            if nota <0 :
                print("Por favor, digite uma nota válida (não negativa).")
                continue
            break
        except ValueError:
            print("Por favor, digite uma nota válida.")

    if nota > maiornota:
        maiornota = nota
        melhoraluno = nome


print(f"O aluno com a melhor nota é: {melhoraluno} com nota {maiornota}")
