import json
from pathlib import Path
from functools import reduce


# Monta um caminho absoluto para o JSON, independente da pasta de execucao.
arquivo_json = (
    Path(__file__).resolve().parent.parent
    / "Filtrando e Mapeando"
    / "aquarium.json"
)

with arquivo_json.open(encoding="utf8") as f:
    # Converte o conteudo JSON em um dicionario Python.
    data_aquarium = json.load(f)

# Seleciona a lista de animais presente na chave "data".
animals = data_aquarium["data"]

# Transforma cada animal em um par: tipo do animal e uma unidade para contagem.
def pick_animal_type(animal):
    return animal ["type"], 1


# Acumula as unidades por tipo em um unico dicionario.
def reducer(acc, val):
    print(val)
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
        
    print(acc)
    return(acc)
    

# Aplica a transformacao a todos os animais antes de realizar a reducao.
type_animals = list(map(pick_animal_type, animals))
print(type_animals)

# Inicia a contagem com um dicionario vazio.
animals_type_count = reduce(reducer, type_animals, {})
print(animals_type_count)

