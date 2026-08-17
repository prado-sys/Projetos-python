from datetime import datetime

# Retorna a data e hora atuais para comparar com o vencimento informado.
def today():
    today = datetime.now()
    return today

# Converte uma data no formato dd-mm-aaaa e informa quando ela e invalida.
def verify_date(date):
    try:
        date_format = datetime.strptime(date, "%d-%m-%Y")
        return date_format
    except:
        raise Exception("Entrada inválida! Tente esse formato: dd-mm-yyyy; Respeitando os traços, não barras.")

    

# Verifica se a data de vencimento ja passou em relacao a data atual.
def verify_due(date_ref):
    due_date = verify_date(date=date_ref)
    
    if today() > due_date:
        print("Seu produto venceu, verificar data de validade!")
    else:
        print("Seu produto se encontra em validade!")
        return 
    
    
    
