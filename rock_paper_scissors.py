import random

user_points = 0
computer_points = 0

options = ["r", "t", "p"]

while True:
    user_choice = input("Escolha R(Rock)/T(Tesoura)/P(Papel) ou Q para Quit!: ").lower()
    
    if user_choice == "q":
        print("Você escolheu sair do game!")
        break
    
    if user_choice not in options:
        print("Opção inválida. Digite R, T, P ou Q.")
        continue
    
    computer_choice = random.randint(0, 2)
    # 0: R, 1: T, 2: P.
    
    computer_option = options[computer_choice]
    
    print("O computador escolheu: "+ computer_option)
    
    if user_choice == computer_option:
        print("Empate!")
        
    elif user_choice == "r" and computer_option == "t":
        print("Você conseguiu vencer a máquina!")
        user_points = user_points + 1
        
    elif user_choice == "t" and computer_option == "p":
            print("Você conseguiu vencer a máquina!")
            user_points = user_points + 1
            
    elif user_choice == "p" and computer_option == "r":
            print("Você conseguiu vencer a máquina!")
            user_points = user_points + 1
    
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
