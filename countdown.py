"""Executa uma contagem regressiva usando uma quantidade de segundos."""

# Importa a funcao que pausa a execucao por um segundo.
import time

# Solicita o tempo inicial em segundos.
t = input("Digite aqui a quantidade de tempo em segundos: ")

# Verifica se o valor informado e numerico.
if t.isdigit():
    # Converte o texto informado para um numero inteiro.
    t = int(t)
else:
    print("Entrada inválida!")
    quit()


# Continua enquanto houver segundos restantes.
while t: #0 >> False | 1, 2 .... >>>> True
    
    # Separa os segundos restantes em minutos e segundos.
    minutes, seconds = divmod(t, 60)
    
    # Formata o horario sempre com dois digitos em cada parte.
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    # Atualiza o temporizador na mesma linha do terminal.
    print(timer, end="\r")
    
    # Aguarda um segundo antes da proxima atualizacao.
    time.sleep(1)
    
    
    t = t - 1 ## o timer vai seguir a contagem até chegar no zero, quando marcar zero a resposta será = false, encerrando assim a contagem do while.
    
# Avisa que a contagem foi concluida.
print("O temporizador chegou ao final")
               
