from functions import * ##Do módulo functions import today, que é a funçao


# Exibe as instrucoes para que o usuario informe uma data de vencimento.
print("##########################")
print("Qual a data de vencimento? ")
print("Formato: DIA-MES-ANO. Exemplo: 01-01-2001\n")
print("##########################")

due_date = input("")

# So consulta a validade quando a data possui os dez caracteres esperados.
if len (due_date) == 10:
    print(verify_due(due_date))
    

