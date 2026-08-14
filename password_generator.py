"""Gera uma senha aleatoria com letras, numeros e caracteres especiais."""

# Importa recursos para sortear caracteres da senha.
import random
# Importa conjuntos prontos de letras, numeros e caracteres especiais.
import string

# Define uma funcao que gera uma senha de 12 caracteres por padrao.
def password_generator(len_pass = 12):
    
    # Guarda todas as letras maiusculas e minusculas disponiveis.
    ascii_options = string.ascii_letters
    # Guarda todos os algarismos disponiveis.
    number_options = string.digits
    # Guarda os caracteres especiais disponiveis.
    punt_options = string.punctuation
    # Une todos os tipos de caracteres que podem ser sorteados.
    options = ascii_options + number_options + punt_options
    
    # Inicia a senha como uma string vazia.
    password_user = ""
    
    # Repete o sorteio ate atingir o tamanho solicitado.
    for i in range(0, len_pass):
        # Sorteia um caractere entre todas as opcoes.
        digit = random.choice(options)
        
        # Acrescenta o caractere sorteado a senha em construcao.
        password_user = password_user + digit
        
    # Devolve a senha pronta para quem chamou a funcao.
    return password_user
    
# Solicita a quantidade de caracteres desejada na senha.
choice_user = input("Quantos digitos na senha?: ")
# Verifica se a resposta contem somente numeros.
if choice_user.isdigit():
    # Converte o texto informado em um numero inteiro.
    choice_user = int(choice_user)
    
else:
    print("Entrada inválida")
    quit()   


# Chama a funcao usando o tamanho escolhido pelo usuario.
response = password_generator(len_pass = choice_user)
# Exibe a senha gerada na tela.
print(f"Senha gerada:\n{response}")
