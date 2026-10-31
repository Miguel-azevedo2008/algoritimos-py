import os
alunos = []
notas = []
gabarito = []
respostas = []

def clear():
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def nao(nao):

    if nao.strip().lower() in ['n', 'nao', 'não']:
        nao = "n"
    else:
        nao = "s"
    return nao

while True:
    try:
        nquestão = int(input("Digite o número de questões: "))
        if nquestão <= 0:
            print("Por favor, digite um número inteiro positivo.")
            exit()
        for i in range(nquestão):
            gabarito.append(input(f"Digite a resposta da questão {i+1}: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro positivo.")

while True:
    prox = input("Deseja adicionar um aluno? (s/n): ")
    prox = nao(prox)
    if prox == 'n':
        break 
    else:
        clear()
        aluno = input("Digite o nome do aluno : ")
        alunos.append(aluno)
        for i in range(nquestão):
            resposta = input(f"Digite a resposta da questão {i+1} para {aluno}: ")
            respostas.append(resposta)
    
        nota = 0
    for j in range(nquestão):
        if respostas[j].strip().lower() == gabarito[j].strip().lower():
            nota += 1
    notas.append(nota)

for i in range(len(alunos)):
    print(f"Aluno: {alunos[i]} - Nota: {notas[i]}/{nquestão}")

input("Pressione Enter para sair...")
os.system('cls' if os.name == 'nt' else 'clear')