def soma_ate_indice(indice):
    soma = 0
    k = 0
    while k < indice:
        k = k + 1
        soma = soma + k
    print("A soma até o índice", indice, "é:", soma)

def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        print(numero, "pertence à sequência de Fibonacci.")
    else:
        print(numero, "não pertence à sequência de Fibonacci.")

def inverte_string(s):
    return ''.join(s[i] for i in range(len(s) - 1, -1, -1))

# Menu principal
while True:
    print("\nEscolha uma opção:")
    print("1. Calcular a soma até um índice")
    print("2. Verificar se um número pertence à sequência de Fibonacci")
    print("3. Inverter uma string")
    print("0. Sair do programa")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        indice = int(input("Digite o índice para calcular a soma: "))
        soma_ate_indice(indice)
    elif opcao == "2":
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        verifica_fibonacci(numero)
    elif opcao == "3":
        string_original = input("Digite uma string para inverter: ")
        string_invertida = inverte_string(string_original)
        print("String invertida:", string_invertida)
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
