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
print('\n Cargando datos opción 2 ...')
a_form={}
test_form=True
limite=400 # maximo->limite=906
for n_form in range(200,limite):#posibles valores a encontrar
    pokemon_form=f'https://pokeapi.co/api/v2/pokemon-form/{n_form}/'
    resp_form = requests.get(pokemon_form)
    dato_form=resp_form.json()
    if dato_form['form_name'] != '':
        name_poke=dato_form['pokemon']['name']
        a={dato_form['form_name']:name_poke}
        a_form.update(a)
print(f"Ejemplo de formas: {a_form.keys()}")
form_in=input("Ingrese una forma: ")
print("Pokemon: ", a_form[form_in])

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
opcion=True
habitat_pokemon={}
nm=1
while opcion:
    pokemon_habitat=f'https://pokeapi.co/api/v2/pokemon-habitat/{nm}/'
    resp_hab = requests.get(pokemon_habitat)
    nm+=1
    if f'{resp_hab}'=='<Response [200]>':
        dato_hab=resp_hab.json()
        a_hab={dato_hab['name']:[k['name'] for k in dato_hab["pokemon_species"]]}
        habitat_pokemon.update(a_hab)
    else:
      opcion=False
print('Ejemplos de habitat: cave, forest, grassland, etc. ')
habitat_in=input('Ingrese un habitat: ')
print('Los pokemons son: ', ', '.join(habitat_pokemon[f'{habitat_in}']))



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
