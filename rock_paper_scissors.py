"""Jogo de pedra, papel e tesoura contra o computador."""

# Importa recursos para escolher a jogada do computador aleatoriamente.
import random

# Inicia a pontuacao do jogador.
user_points = 0
# Inicia a pontuacao do computador.
computer_points = 0

# Define as letras aceitas: r para pedra, t para tesoura e p para papel.
options = ["r", "t", "p"]

"""Repete rodadas ate o usuario escolher sair."""
while True:
    user_choice = input("Escolha R(Rock)/T(Tesoura)/P(Papel) ou Q para Quit!: ").lower()
    
    # Encerra o jogo quando o usuario digita q.
    if user_choice == "q":
        print("Você escolheu sair do game!")
        break
    
    # Rejeita entradas diferentes das opcoes permitidas.
    if user_choice not in options:
        print("Opção inválida. Digite R, T, P ou Q.")
        continue
    
    # Sorteia o indice referente a uma das opcoes do computador.
    computer_choice = random.randint(0, 2)
    # 0: R, 1: T, 2: P.
    
    # Usa o indice sorteado para obter a letra escolhida pelo computador.
    computer_option = options[computer_choice]
    
    print("O computador escolheu: "+ computer_option)
    
    # Verifica se os dois escolheram a mesma opcao.
    if user_choice == computer_option:
        print("Empate!")
        
    # Verifica a vitoria de pedra contra tesoura.
    elif user_choice == "r" and computer_option == "t":
        print("Você conseguiu vencer a máquina!")
        user_points = user_points + 1
        
    # Verifica a vitoria de tesoura contra papel.
    elif user_choice == "t" and computer_option == "p":
            print("Você conseguiu vencer a máquina!")
            user_points = user_points + 1
            
    # Verifica a vitoria de papel contra pedra.
    elif user_choice == "p" and computer_option == "r":
            print("Você conseguiu vencer a máquina!")
            user_points = user_points + 1
    
    # Nos outros casos, o computador venceu a rodada.
    else:
        print("Ih rapaz, o computador te venceu, tente novamente!")
        computer_points = computer_points + 1

print("Sua pontuação: " + str(user_points))
print("Pontuação da máquina: " + str(computer_points))

if computer_points > user_points:
    print("Perdesse pra máquina, amigo?")
    
elif user_points > computer_points:
    print("Você declarou o fim da era das máquinas, muauahuahauha!")

else:
    print("Bixo, sério que deu empate?")

print("Fallow! Até a próxima!")
