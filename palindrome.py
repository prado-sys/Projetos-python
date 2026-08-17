import math

# Compara os caracteres das extremidades em direcao ao centro da palavra.
def is_palindrome(workd):
    j = len(word)-1
    result = 0
    for i in range(len(word)):
        if word[i] == word[j]:
            result = result + 1
        if i >= j:
            break
        j = j - 1
        
    if result == math.ceil(len(word)/2):
        return True
    else:
        return False
    
# Resolve o mesmo problema removendo recursivamente os caracteres das extremidades.
def is_palindrome_recursive(word):
    if len (word) <=1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])
    
    
        

# Lista de palavras usada para demonstrar a verificacao de palindromos.
words = ["arara", "racecar", "carro", "cama", "level"]

# Exibe o resultado da verificacao para cada palavra da lista.
for word in words:
    print(word)
    print(is_palindrome(word)) 
    print("\n")
    
