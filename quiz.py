print("Olá seja bem vindo ao quiz do Vinícius Prado!")

# Pergunta se o usuario quer comecar e padroniza a resposta.
answer_user = input("Deseja iniciar agora?  (S/N) ").strip().upper()

# Encerra o programa quando o usuario nao confirma o inicio.
if answer_user != "S":

    quit()
    
# Inicia a pontuacao do participante.
score = 0
    
print("Começando...")
    
print("Qual empresa desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Activision \n (B) Ubisoft \n (C) Rockstar Games \n (D) EA")
    
# Le e padroniza a resposta da primeira pergunta.
answer_1 = input("Resposta: ").strip().upper()
    
# Confere se a resposta para a primeira pergunta esta correta.
if answer_1 == "C":
    print("Resposta correta, parabéns!")
    # Adiciona um ponto por uma resposta correta.
    score = score + 1
    
else:
    print("Infelizmente a resposta está incorreta, tente novamente!")
    
print("Qual o nome do protagonista do jogo GTA San Andreas?\n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n")

# Le e padroniza a resposta da segunda pergunta.
answer_2 = input("Resposta: ").strip().upper()

# Confere se a resposta para a segunda pergunta esta correta.
if answer_2 == "B":
    print("Parabéns, resposta correta!")
    score = score + 1

else:
    print("Infelizmente a resposta está incorreta, tente novamente!")
    

print("Qual é o nome da cidade fictícia baseada em Miami onde se passa o jogo GTA Vice City? \n (A) Liberty city \n (B) Los Santos \n (C) Vice City \n (D) San Fierro \n")

# Le e padroniza a resposta da terceira pergunta.
answer_3 = input("Resposta: ").strip().upper()
      
# Confere se a resposta para a terceira pergunta esta correta.
if answer_3 == "C":
    print("Parabéns, resposta correta!")
    score = score + 1


else:
    print("Infelizmente a resposta está incorreta, tente novamente!")
    
print(f"O Quiz chegou ao fim... Pontuação total: {score} Pontos")
"""Aplica um quiz de tres perguntas sobre a serie de jogos GTA."""
