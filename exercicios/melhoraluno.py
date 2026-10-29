t1 = False
melhoraluno = ""
maiornota = -1
na = 0

while not t1:
    try:
        na = int(input("Digite o número de alunos: "))
        t1 = True
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

for i in range(na):
    t2 = False
    while not t2:
        try: 
            nome = input(f"Digite o nome do aluno {i + 1}: ")
            nota = float(input(f"Digite a nota do aluno {i + 1}: "))
            t2 = True
        except ValueError:
            print("Por favor, digite uma nota válida.")

    if nota > maiornota:
        maiornota = nota
        melhoraluno = nome


print(f"O aluno com a melhor nota é: {melhoraluno} com nota {maiornota}")
