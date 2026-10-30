import os

def clear():
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

gabarito = []
nquestão = int(input("Digite o número de questões: "))
for i in range(nquestão):
    gabarito.append(input(f"Digite a resposta da questão {i+1}: "))

clear()

alunos = []
notas = []

while True:
    prox = input("Deseja adicionar um aluno? (s/n): ").strip().lower()
    if prox == 'n':
        break 
    else:
        clear()
        aluno = input("Digite o nome do aluno : ")
        respostas = []
        for i in range(nquestão):
            resposta = input(f"Digite a resposta da questão {i+1} para {aluno}: ")
            respostas.append(resposta)
    
        alunos.append(aluno)
    
    nota = 0
    for j in range(nquestão):
        if respostas[j].strip().lower() == gabarito[j].strip().lower():
            nota += 1
    notas.append(nota)

for i in range(len(alunos)):
    print(f"Aluno: {alunos[i]} - Nota: {notas[i]}/{nquestão}")

input("Pressione Enter para sair...")
os.system('cls' if os.name == 'nt' else 'clear')