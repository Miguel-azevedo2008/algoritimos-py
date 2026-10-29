import os

cotacao = 5.12
sair = False

def clear():
    # Limpa o terminal após o usuário pressionar Enter.
    input("Pressione Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")


def formatar(valor):
    # Formata o valor seguindo o padrão brasileiro:
    # ponto para milhares e vírgula para casas decimais.
    texto = f"{valor:,.2f}"
    return texto.replace(",", "#").replace(".", ",").replace("#", ".")


def idade():
    # Calcula a idade com base no ano atual e no ano de nascimento.
    try:
        ano = int(input("Em que ano estamos? "))
        data = int(input("Qual seu ano de nascimento? "))

        if data > ano or ano <= 1900 or data <= 1900:
            print("Ano inválido.")
            return

        soma = ano - data
        print(f"Você tem {soma} anos de idade.")

    except ValueError:
        print("Por favor, digite um número válido.")


def conversao():
    # Converte reais para dólares usando a cotação definida no início do programa.
    try:
        entrada = input("Quantos reais você possui? ").replace(",", ".")
        reais = float(entrada)

        if reais <= 0:
            print("O valor precisa ser maior que zero.")
            return

        dolares = reais / cotacao
        print(f"Você pode comprar {formatar(dolares)} dólares.")

    except ValueError:
        print("Por favor, digite um número válido.")


def temperatura():
    # Converte uma temperatura de Fahrenheit para Celsius.
    try:
        entrada = input("Qual a temperatura atual em Fahrenheit? ").replace(",", ".")
        f = float(entrada)

        # Limite físico aproximado do zero absoluto em Fahrenheit.
        if f < -459.67:
            print("Temperatura inválida.")
            return

        c = (f - 32) * 5 / 9
        print(f"A temperatura é {formatar(c)} °C.")

    except ValueError:
        print("Por favor, digite um número válido.")


def imposto():
    # Calcula o Imposto de Importação do Remessa Conforme.
    # Até US$ 50: 0% de Imposto de Importação.
    # Acima de US$ 50: 60%, com desconto de US$ 30 no imposto.
    # O cálculo abaixo não inclui ICMS.
    try:
        entrada = input("Quantos dólares foram gastos? ").replace(",", ".")
        gasto = float(entrada)

        if gasto < 0:
            print("Valor inválido.")
            return

        if gasto <= 50:
            print("Não haverá Imposto de Importação.")
        else:
            taxa = (gasto * 0.60 - 30) * cotacao
            print(f"O Imposto de Importação será de {formatar(taxa)}.")

    except ValueError:
        print("Por favor, digite um número válido.")


def emprestimo():
    # Calcula o valor total de um empréstimo usando juros simples.
    # A taxa informada é aplicada a cada parcela.
    try:
        entrada_v = input("Qual valor será preciso? ").replace(",", ".")
        entrada_t = input("Qual a taxa em %? ").replace(",", ".")

        taxa = float(entrada_t) / 100
        valor = float(entrada_v)
        parcelas = int(input("Em quantas parcelas você pode pagar? "))

        if valor <= 0:
            print("Valor inválido.")
            return

        if parcelas <= 0 or parcelas > 50:
            print("Número de parcelas inválido.")
            return

        if taxa < 0 or taxa > 0.50:
            print("Taxa inválida.")
            return

        # Fórmula de juros simples:
        # M = C × (1 + i × n)
        montante = valor * (1 + taxa * parcelas)
        valor_parcela = montante / parcelas

        print(
            f"Você irá pagar {formatar(montante)} "
            f"em {parcelas} parcelas de {formatar(valor_parcela)}."
        )

    except ValueError:
        print("Por favor, digite um número válido.")


if __name__ == "__main__":
    while not sair:
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
                sair = True
                clear()

            else:
                print("Opção inválida. Tente novamente.")
                clear()

        except ValueError:
            print("Por favor, digite um número válido.")
            clear()