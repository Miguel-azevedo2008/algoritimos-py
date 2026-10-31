import os
import math

def clear():
    # Limpa o terminal após o usuário pressionar Enter.
    input("Pressione Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")


def formatar(valor):
    # Formata o valor seguindo o padrão brasileiro, com vírgula como separador decimal e ponto como separador de milhar.
    texto = f"{valor:,.2f}"
    return texto.replace(",", "#").replace(".", ",").replace("#", ".")

def ler_cotacao():
    while True:
        try:
            cotacao = input("Qual a cotação do dólar? ").replace(",", ".")
            cotacao = float(cotacao)
            if not math.isfinite(cotacao):
                print("A cotação precisa ser um número finito.")
                continue
            elif cotacao <= 0:
                print("A cotação precisa ser maior que zero.")
                continue
            return cotacao
        except ValueError:
            print("Por favor, digite um número válido.")

def idade():
    # estima a idade do usuário com base no ano atual e no ano de nascimento informado.
    while True:
        try:
            ano = int(input("Em que ano estamos? "))
            data = int(input("Qual seu ano de nascimento? "))

            if data >= ano or ano <= 1900 or data <= 1900:
                print("Ano inválido.")
                continue

            soma = ano - data
            print(f"Você tem {soma} anos de idade.")
            break

        except ValueError:
            print("Por favor, digite um número válido.")


def conversao(cotacao):
    # Converte reais para dólares
    while True:
        try:
            reais = input("Quantos reais você possui? ").replace(",", ".")
            reais = float(reais)

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
            f = input("Qual a temperatura atual em Fahrenheit? ").replace(",", ".")
            f = float(f)

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


def imposto(cotacao):
    # Simula o Imposto de Importação para pessoa física em compras
    # de plataformas certificadas pelo Remessa Conforme.
    # Até US$ 50: alíquota de 0%.
    # Acima de US$ 50: alíquota de 60%, com desconto de US$ 30 no imposto.
    # O cálculo não inclui ICMS e utiliza a cotação definida no programa.
    while True:
        try:
            dolares = input("Quantos dólares foram gastos? ").replace(",", ".")
            dolares = float(dolares)

            if not math.isfinite(dolares):
                print("O valor precisa ser um número finito.")
                continue
            elif dolares < 0:
                print("Valor inválido.")
                continue
            if dolares > 3000:
                print("Valor acima do limite.")
                continue
            if dolares <= 50:
                print("Não haverá Imposto de Importação.")
            else:
                taxa = (dolares * 0.60 - 30) * cotacao
                print(f"O Imposto de Importação será de {formatar(taxa)}.")
            break

        except ValueError:
            print("Por favor, digite um número válido.")


def emprestimo():
    # Calcula o valor total a ser pago em um empréstimo com juros simples.
    # A taxa informada é aplicada por período, conforme o número de parcelas.
    while True:
        try:
            valor = input("Qual valor será preciso? ").replace(",", ".")
            valor = float(valor)
            if not math.isfinite(valor):
                print("O valor precisa ser um número finito.")
                continue
            elif valor <= 0:
                print("Valor inválido.")
                continue

            taxa = input("Qual a taxa por período em %? ").replace(",", ".")
            taxa = float(taxa) / 100
            if not math.isfinite(taxa):
                print("A taxa precisa ser um número finito.")
                continue
            elif taxa < 0 or taxa > 0.50:
                print("Taxa inválida.")
                continue

            parcelas = int(input("Em quantas parcelas você pode pagar? "))
            if parcelas <= 0 or parcelas > 50:
                print("Número de parcelas inválido.")
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