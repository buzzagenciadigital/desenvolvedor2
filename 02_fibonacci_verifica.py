def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num or num == 0:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = 21  # ou use: numero = int(input("Informe um número: "))
print(is_fibonacci(numero))
