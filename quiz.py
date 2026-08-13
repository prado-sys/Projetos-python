print("Olá seja bem vindo ao quiz do Vinícius Prado!")

answer_user = input("Deseja iniciar agora?  (S/N) ").strip().upper()

if answer_user != "S":

    quit()
    
score = 0
    
print("Começando...")
    
print("Qual empresa desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Activision \n (B) Ubisoft \n (C) Rockstar Games \n (D) EA")
    
answer_1 = input("Resposta: ").strip().upper()
    
if answer_1 == "C":
    print("Resposta correta, parabéns!")
    score = score + 1
    
else:
    print("Infelizmente a resposta está incorreta, tente novamente!")
    
print("Qual o nome do protagonista do jogo GTA San Andreas?\n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n")

answer_2 = input("Resposta: ").strip().upper()

if answer_2 == "B":
    print("Parabéns, resposta correta!")
    score = score + 1

else:
    print("Infelizmente a resposta está incorreta, tente novamente!")
    

print("Qual é o nome da cidade fictícia baseada em Miami onde se passa o jogo GTA Vice City? \n (A) Liberty city \n (B) Los Santos \n (C) Vice City \n (D) San Fierro \n")

answer_3 = input("Resposta: ").strip().upper()
      
if answer_3 == "C":
    print("Parabéns, resposta correta!")
    score = score + 1


else:
    print("Infelizmente a resposta está incorreta, tente novamente!")
    
print(f"O Quiz chegou ao fim... Pontuação total: {score} Pontos")
