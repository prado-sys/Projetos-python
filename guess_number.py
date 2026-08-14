"""Jogo em que o usuario tenta adivinhar um numero aleatorio."""

# Importa recursos para gerar o numero secreto.
import random

print("Seja bem vindo ao programa do Prado!")

choice_number = input ("Digite o número máximo do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)

else:
    print("Erro: Valor informado não é númerico. Por favor execute novamente informando um número.")
    quit()
    
# Sorteia o numero que deve ser adivinhado entre zero e o limite.
random_number = random.randint(0, choice_number)

# Inicia o contador de tentativas do jogador.
n_choices = 0 

"""Mantem o jogo ativo ate o jogador acertar o numero."""
while True:
    answer_user = input("Advinhe o número: ")
    
    # Confere se o palpite contem apenas digitos.
    if answer_user.isdigit():
        # Converte o palpite para inteiro para poder compara-lo.
        answer_user = int(answer_user)
    else:
        print("Erro: Valor informado não é número. Favor informe um número!")
        continue
    
    # Soma uma tentativa valida ao placar.
    n_choices = n_choices + 1
    
    # Verifica se o palpite corresponde ao numero sorteado.
    if answer_user == random_number:
        print("Você acertou, parabéns!!")
        # Define a pontuacao de acordo com a quantidade de tentativas.
        if n_choices == 1:
                print("Pontuação máxima: 100 pontos")
        elif n_choices > 1 and n_choices < 3:
            print("Pontuação: 80 Pontos")
        elif n_choices > 4 and n_choices < 6:
            print("Pontuação: 50 pontos")
        else:
            print("Pontuação: 20 Pontos")
            
        
        
        
        break #O break fica aqui pra quebrar o loop caso o usuário acerte.
    
    elif answer_user > random_number:
        print("Chutou alto! O número randômico é menor que isso...")
    else:
        print("Chutou baixo! O número randômico é maior que isso...") 
        
    print(f"Nº de tentativas: {n_choices}")
    
       
