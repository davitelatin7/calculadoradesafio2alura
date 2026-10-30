# =======================================================
# CALCULADORA EM PYTHON PARA INICIANTES
# Aprenda: Funções, Conversão de Tipos, Condicionais e Porcentagem
# =======================================================

# 1. FUNÇÕES DAS OPERAÇÕES MATEMÁTICAS
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração entre dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto da multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """Retorna a divisão. Protegido contra divisão por zero!"""
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b


def porcentagem(a, b):
    """Retorna b% de a. Exemplo: 15% de 200 = 30.0"""
    return (a * b) / 100


# 2. FUNÇÃO PRINCIPAL DO PROGRAMA
def calculadora():
    print("=" * 35)
    print("   CALCULADORA DIDÁTICA EM PYTHON")
    print("=" * 35)
    print("Operações disponíveis:")
    print("  1 -> Adição (+)")
    print("  2 -> Subtração (-)")
    print("  3 -> Multiplicação (*)")
    print("  4 -> Divisão (/)")
    print("  5 -> Porcentagem (%)")
    print("  0 -> Sair do programa")
    print("-" * 35)

    opcao = input("Escolha uma opção (0 a 5): ")

    if opcao == '0':
        print("Até logo! Bons estudos em Python!")
        return

    if opcao not in ['1', '2', '3', '4', '5']:
        print("Opção inválida! Escolha um número de 1 a 5.")
        return

    # Entrada de números com tratamento de erro
    try:
        num1 = float(input("Digite o primeiro número (ou valor base): "))
        num2 = float(input("Digite o segundo número (ou percentual): "))
    except ValueError:
        print("Erro: Digite apenas números válidos!")
        return

    # Execução baseada na escolha do usuário
    if opcao == '1':
        res = somar(num1, num2)
        print(f"\nResultado: {num1} + {num2} = {res}")
    elif opcao == '2':
        res = subtrair(num1, num2)
        print(f"\nResultado: {num1} - {num2} = {res}")
    elif opcao == '3':
        res = multiplicar(num1, num2)
        print(f"\nResultado: {num1} * {num2} = {res}")
    elif opcao == '4':
        res = dividir(num1, num2)
        print(f"\nResultado: {num1} / {num2} = {res}")
    elif opcao == '5':
        res = porcentagem(num1, num2)
        print(f"\nResultado: {num2}% de {num1} = {res}")


if __name__ == "__main__":
    calculadora()