from functools import reduce

# Demonstra como reduzir uma lista a um unico resultado acumulado.
# Define os valores que serao somados pelo reduce.
numbers = [1, 2, 3, 4, 5]

# Recebe o acumulador e o proximo valor, exibindo cada etapa da soma.
def sum(a, b):
    
    print("a = ", a)
    print("b = ", b)
    print("a+b = ", a+b)
    return a + b

print("A soma dos números dentro da lista de array é: " + str(reduce(sum, numbers)))
