import os
import math

cotacao = 5.12

def clear():
    # Limpa o terminal após o usuário pressionar Enter.
    input("Pressione Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")


def formatar(valor):
    # Formata o valor seguindo o padrão brasileiro, com vírgula como separador decimal e ponto como separador de milhar.
    texto = f"{valor:,.2f}"
    return texto.replace(",", "#").replace(".", ",").replace("#", ".")


def idade():
    # estima a idade do usuário com base no ano atual e no ano de nascimento informado.
    while True:
        try:
            ano = int(input("Em que ano estamos? "))
            data = int(input("Qual seu ano de nascimento? "))

            if data > ano or ano <= 1900 or data <= 1900 or data == ano:
                print("Ano inválido.")
                continue

            soma = ano - data
            print(f"Você tem {soma} anos de idade.")
            break

        except ValueError:
            print("Por favor, digite um número válido.")


def conversao():
    # Converte reais para dólares usando a cotação definida no início do programa.
    while True:
        try:
            entrada = input("Quantos reais você possui? ").replace(",", ".")
            reais = float(entrada)

            if not math.isfinite(reais):
                print("O valor precisa ser um número finito.")
                continue
            elif reais <= 0:
                print("O valor precisa ser maior que zero.")
                continue

            dolares = reais / cotacao
            print(f"Você pode comprar {formatar(dolares)} dólares.")
            break

        except ValueError:
            print("Por favor, digite um número válido.")


def temperatura():
    # Converte uma temperatura de Fahrenheit para Celsius.
    while True:
        try:
            entrada = input("Qual a temperatura atual em Fahrenheit? ").replace(",", ".")
            f = float(entrada)

            # Limite físico aproximado do zero absoluto em Fahrenheit.
            
            if not math.isfinite(f):
                print("O valor precisa ser um número finito.")
                continue
            elif f < -459.67:
                print("Temperatura inválida.")
                continue

            c = (f - 32) * 5 / 9
            print(f"A temperatura é {formatar(c)} °C.")
            break

        except ValueError:
            print("Por favor, digite um número válido.")


def imposto():
    # Simula o Imposto de Importação para pessoa física em compras
    # de plataformas certificadas pelo Remessa Conforme.
    # Até US$ 50: alíquota de 0%.
    # Acima de US$ 50: alíquota de 60%, com desconto de US$ 30 no imposto.
    # O cálculo não inclui ICMS e utiliza a cotação definida no programa.
    while True:
        try:
            entrada = input("Quantos dólares foram gastos? ").replace(",", ".")
            gasto = float(entrada)

            if not math.isfinite(gasto):
                print("O valor precisa ser um número finito.")
                continue
            elif gasto < 0:
                print("Valor inválido.")
                continue
            if gasto > 3000:
                print("Valor acima do limite.")
                continue
            if gasto <= 50:
                print("Não haverá Imposto de Importação.")
            else:
                taxa = (gasto * 0.60 - 30) * cotacao
                print(f"O Imposto de Importação será de {formatar(taxa)}.")
            break

        except ValueError:
            print("Por favor, digite um número válido.")


def emprestimo():
    # Calcula o valor total a ser pago em um empréstimo com juros simples.
    # A taxa informada é aplicada por período, conforme o número de parcelas.
    while True:
        try:
            entrada_v = input("Qual valor será preciso? ").replace(",", ".")
            entrada_t = input("Qual a taxa em %? ").replace(",", ".")

            taxa = float(entrada_t) / 100
            valor = float(entrada_v)
            parcelas = int(input("Em quantas parcelas você pode pagar? "))

            if not math.isfinite(valor):
                print("O valor precisa ser um número finito.")
                continue
            elif valor <= 0:
                print("Valor inválido.")
                continue
            
            if parcelas <= 0 or parcelas > 50:
                print("Número de parcelas inválido.")
                continue

            if not math.isfinite(taxa):
                print("A taxa precisa ser um número finito.")
                continue
            elif taxa < 0 or taxa > 0.50:
                print("Taxa inválida.")
                continue
            
            # Fórmula de juros simples:
            # M = C × (1 + i × n)
            montante = valor * (1 + taxa * parcelas)
            valor_parcela = montante / parcelas

            print(
                f"Você irá pagar {formatar(montante)} "
                f"em {parcelas} parcelas de {formatar(valor_parcela)}."
            )
            break

        except ValueError:
            print("Por favor, digite um número válido.")


if __name__ == "__main__":
    while True:
        print("==== MENU ====")
        print("1 - Idade")
        print("2 - Dólares")
        print("3 - Temperatura")
        print("4 - Imposto")
        print("5 - Empréstimo")
        print("6 - Sair")

        try:
            acao = int(input("Digite sua opção: "))

            if acao == 1:
                idade()
                clear()

            elif acao == 2:
                conversao()
                clear()

            elif acao == 3:
                temperatura()
                clear()

            elif acao == 4:
                imposto()
                clear()

            elif acao == 5:
                emprestimo()
                clear()

            elif acao == 6:
                os.system("cls" if os.name == "nt" else "clear")
                break

            else:
                print("Opção inválida. Tente novamente.")
                clear()

        except ValueError:
            print("Por favor, digite um número válido.")
            clear()