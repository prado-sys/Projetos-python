import json

# Carrega os dados dos animais cadastrados no arquivo JSON.
f = open("aquarium.json", encoding="utf8")

data_aquarium = json.load(f)
animals = data_aquarium["data"]


# Indica se o animal recebido e um peixe.
def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False


animals_fish = list(filter(verify_fish, animals))
# print(animals_fish)


# Extrai apenas o nome de um animal para formar uma lista simplificada.
def animal_name(animal):
    return animal["name"]

animals_fish_name = list(map(animal_name, animals_fish))
print(animals_fish_name)


# Move os animais selecionados para um novo tanque, preservando os demais dados.
def assign_to_tank(animals, names_selected, new_tank_number):
    # Atualiza o numero do tanque somente para os nomes selecionados.
    def change_tank_number(animal):
        if animal ["name"] in names_selected:
            animal ["tank number"] = new_tank_number
        return animal
    return list(map(change_tank_number, animals))

new_aquarium = assign_to_tank(animals, animals_fish_name, 42)

print(new_aquarium)
