import time

t = input("Digite aqui a quantidade de tempo em segundos: ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida!")
    quit()


while t: #0 >> False | 1, 2 .... >>>> True
    
    minutes, seconds = divmod(t, 60)
    
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    
    time.sleep(1)
    
    
    t = t - 1 ## o timer vai seguir a contagem até chegar no zero, quando marcar zero a resposta será = false, encerrando assim a contagem do while.
    
print("O temporizador chegou ao final")
               