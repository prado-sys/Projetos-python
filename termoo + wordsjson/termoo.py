import json
import random

# Jogo de adivinhar uma data com base em uma dica carregada do JSON.

# Carrega as datas e suas dicas a partir do arquivo JSON.
f = open("words.json", encoding="utf8")

words = json.load(f)

# Escolhe uma data aleatoria que sera a resposta da rodada.
choice_c = random.choice(list(words.keys()))

print("Olá, seja bem vindo!")
print("####################################")

n_choices = 5
win = False

# Mantem o jogo ativo enquanto houver tentativas e a data nao for acertada.
while n_choices > 0 and win is not True:
    
    print("Dica: " + words[choice_c])
    answer_user = input("Data: DDMMAA\n")
    
    if len (answer_user) !=8:
        print("Erro na entrada. A data deve conter 8 dígitos!")
        continue
    
    if answer_user.isdigit():
        # Compara cada digito informado com a posicao correspondente da resposta.
        check = []
        pontuation = 0
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("✅")
                pontuation = pontuation + 1
            else:
                check.append("💢")
        
        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(answer_user))
        print("#######################\n")
        
        if pontuation == 8:
            win = True        
        
    else:
        print("Erro na entrada. A resposta deve ser uma data!")
        continue

    # Desconta uma tentativa depois de processar uma resposta valida.
    n_choices = n_choices - 1
    
    if win == True:
        print("Vitória, Parabéns!!")
    else:
        print("Derrota!")
        print("A Resposta correta era: " + choice_c)
