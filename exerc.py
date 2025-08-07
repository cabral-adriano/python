## Programa simples de calculadora

# Ask for two numbers to user
num1 = float(input("Insert the first number please: "))
num2 = float(input("Insert the second number please: "))

# Ask for to select operation
operacao = input("Please select the operation to execute! (+, -, *, /): ")

# Execute operation and show the result
if operacao == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operacao == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operacao == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operacao == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida.")