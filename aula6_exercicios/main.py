from func_exercicios import*

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
                cotacao = ler_cotacao()
                conversao(cotacao)
                clear()
            elif acao == 3:
                temperatura()
                clear()

            elif acao == 4:
                cotacao = ler_cotacao()
                imposto(cotacao)
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