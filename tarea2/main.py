import requests
def print_list(lista):
    for i,elem in enumerate(lista,start=1):
        if i%3==0:
            print(i,elem,end='\n')
        else:
            print(i,elem,end=' \t ')



#Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) 
# y se listan todos los pokemon respectivos.

generation=int(input("Ingrese la generación de pokemones a mostrar (1,2,..,8): "))
data=requests.get(f"https://pokeapi.co/api/v2/generation/{generation}")

data=data.json()
pokemons_in_generation=[i['name'] for i in data['pokemon_species']]
print_list(pokemons_in_generation)

# Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores)
# y se listan todos los pokemons respectivos.
forma_in=input("ingrese una forma: ")
data_form=requests.get(f"https://pokeapi.co/api/v2/pokemon-form/?offset=0&limit=1320")
resp_form=data_form.json()

form_pokemon={v['name']:v['url'] for v in resp_form['results']}
if forma_in in form_pokemon:
    data_of_forms=requests.get(form_pokemon[forma_in])
    data_of_forms=data_of_forms.json()
    pokemon_s=data_of_forms['pokemon']['name']

#Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a 
# ingresar para interactuar.
ability=input("Ingrese una habilidad: ")
# data_forms=requests.get(f"https://pokeapi.co/api/v2/ability/{ability}")
data_ability=requests.get(f"https://pokeapi.co/api/v2/ability/?offset=0&limit=330")
data_ability=data_ability.json()

val_abilities=data_ability['results']
list_of_abilities={i['name']:i['url'] for i in val_abilities}
if ability in list_of_abilities:
    data_of_ability=requests.get(list_of_abilities[ability])
    data_of_ability=data_of_ability.json()
    list_data_pokemon=data_of_ability['pokemon']
    pokemons=[i['pokemon']['name'] for i in list_data_pokemon]
    print_list(pokemons)

#Opción 4: Listar pokemons por habitat. 
# Se deben sugerir opciones a ingresar para interactuar.

print("Opción 4")
print('Ejemplos de habitat: cave, forest, grassland, etc. ')
habitat_in=input("ingrese un habitat: ")
data_habitat=requests.get(f"https://pokeapi.co/api/v2/pokemon-habitat/")
resp_habitat=data_habitat.json()

habitat_pokemon={v['name']:v['url'] for v in resp_habitat['results']}
if habitat_in in habitat_pokemon:
    data_of_habits=requests.get(habitat_pokemon[habitat_in])
    resp_of_habits=data_of_habits.json()
    pokemons_por_habitat=[k['name'] for k in resp_of_habits['pokemon_species']]


#Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar 
# para interactuar.
tipo=input("ingrese un tipo: ")
data_type=requests.get(f"https://pokeapi.co/api/v2/type/")
data_type=data_type.json()

types_pokemon={i['name']:i['url'] for i in data_type['results']}
if tipo in types_pokemon:
    data_of_types=requests.get(types_pokemon[tipo])
    data_of_types=data_of_types.json()
    pokemons=[i['pokemon']['name'] for i in data_of_types['pokemon']]
    print_list(pokemons)
