import requests

class Pokemon:
    def __init__(self):
        self.__nombre=""
        self.__habilidades=""
        self.__number=""
    #SET
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_habilidades(self,habilidades):
        self.__habilidades=habilidades
    def set_number(self,n):
        self.__number=n
    #GET    
    def get_atributos(self):
        return self.__nombre, self.__habilidades,self.__url
    def get_nombre(self):
        return self.__nombre
    def get_habilidades(self):
        return self.__habilidades
    def get_number(self):
        return self.__number
    #Funciones
    def print_nombre_habilidad_url(self):
        dato_pokemon=extract_json(f'https://pokeapi.co/api/v2/pokemon/{self.__nombre}')
        if dato_pokemon==404:
            dato_pokemon=extract_json(f'https://pokeapi.co/api/v2/pokemon/{self.__number}')
        self.__habilidades = extract_habilidades(dato_pokemon)
        url_imagen= dato_pokemon['sprites']['other']
        self.__url=url_imagen['official-artwork']['front_default']
        print('---------------------------------------------------------------'*2)
        print(f'Nombre del Pokémon: {self.__nombre}')
        print(f'Habilidades de {self.__nombre}: ',', '.join(self.__habilidades))
        print(f'URL de la imagen: ',self.__url)
        print('---------------------------------------------------------------'*2)

class Sistema:
    def listar_generacion(self):
        poke=Pokemon()
        generation=int(input("Ingrese la generación de Pokémones a mostrar (1,2,..,8): "))
        data=extract_json(f"https://pokeapi.co/api/v2/generation/{generation}")
        pokemons_in_generation=[i['name'] for i in data['pokemon_species']]
        pokemon_number_data=[i['url'].split('/')[-2] for i in data['pokemon_species']]
        for v,[k_pokemon,u_pokemon] in enumerate(zip(pokemons_in_generation,pokemon_number_data), start=1):
            poke.set_nombre(k_pokemon)
            poke.set_number(u_pokemon)
            print(f'\nPOKÉMON N° {v}')
            poke.print_nombre_habilidad_url()
        
    def listar_forma(self):
        poke=Pokemon()
        print("Sugerencias: unown-a, unown-z, cherrim-overcast, shellos-west, ... ")
        forma_in=input("Ingrese una forma: ")
        data_form=extract_json(f"https://pokeapi.co/api/v2/pokemon-form/?offset=0&limit=1320")

        form_pokemon={v['name']:v['url'] for v in data_form['results']}
        if forma_in in form_pokemon:
            data_of_forms=extract_json(form_pokemon[forma_in])
            poke.set_nombre(data_of_forms['pokemon']['name'])
            print('\nRESULTADO: ')  
            poke.print_nombre_habilidad_url()
        else:
            print("No se encontró ningún Pokémon con esta forma")
    
    def listar_habilidad(self):
        poke=Pokemon()
        print("Sugerencias: stench, drizzle, sturdy, ...")
        ability=input("Ingrese una habilidad: ")

        data_ability=extract_json(f"https://pokeapi.co/api/v2/ability/?offset=0&limit=330")
        val_abilities=data_ability['results']
        list_of_abilities={i['name']:i['url'] for i in val_abilities}
        if ability in list_of_abilities:
            data_of_ability=extract_json(list_of_abilities[ability])
            list_data_pokemon=data_of_ability['pokemon']
            pokemons=[i['pokemon']['name'] for i in list_data_pokemon]
            # print_list(pokemons)
            for v,k_pokemon in enumerate(pokemons, start=1):
                poke.set_nombre(k_pokemon)
                print(f'\nPOKÉMON N° {v}')
                poke.print_nombre_habilidad_url()
        else:
            print("No se encontró ningún Pokémon con esa habilidad")
    def listar_habitat(self):
        poke=Pokemon()
        pokemons_por_habitat=[]
        print('Sugerencias: cave, forest, grassland, etc. ')
        habitat_in=input("ingrese un hábitat: ")
        data_habitat=extract_json(f"https://pokeapi.co/api/v2/pokemon-habitat/")


        habitat_pokemon={v['name']:v['url'] for v in data_habitat['results']}
        if habitat_in in habitat_pokemon:
            data_of_habits=extract_json(habitat_pokemon[habitat_in])
            pokemons_por_habitat=[k['name'] for k in data_of_habits['pokemon_species']]
            for v,k_pokemon in enumerate(pokemons_por_habitat, start=1):
                poke.set_nombre(k_pokemon)
                print(f'\nPOKÉMON N° {v}')
                poke.print_nombre_habilidad_url()
        else:
            print("No se encontró ningún Pokémon con esa habitat")
    def listar_tipo(self):
        poke=Pokemon()

        print("Sugerencias: normal, fighting, flying, ... ")
        tipo=input("Ingrese un tipo: ")
        data_type=extract_json(f"https://pokeapi.co/api/v2/type/")

        types_pokemon={i['name']:i['url'] for i in data_type['results']}
        if tipo in types_pokemon:
            data_of_types=extract_json(types_pokemon[tipo])
            pokemons=[i['pokemon']['name'] for i in data_of_types['pokemon']]

            for v,k_pokemon in enumerate(pokemons, start=1):
                poke.set_nombre(k_pokemon)
                print(f'\nPOKÉMON N° {v}')
                poke.print_nombre_habilidad_url()
        else:
            print("No se encontró ningún Pokémon de este tipo")
        
#Funciones auxiliares
def extract_json(url):
    datos=requests.get(url,stream=True)
    if datos.status_code==404:
        return 404
    datos=datos.json()
    return datos
def extract_habilidades(datos):
    return [elem['ability']['name'] for elem in datos['abilities']]




def menu():
    sistema_poke=Sistema()
    opciones=True
    while opciones:
        print("==========================================\n")
        print("_________________ MENÚ ___________________\n")
        print("Opción 1: Listar pokemons por generación")
        print("Opción 2: Listar pokemons por forma")
        print("Opción 3: Listar pokemons por habilidad")
        print("Opción 4: Listar pokemons por hábitat")
        print("Opción 5: Listar pokemons por tipo")
        print("Opción 6: Salir")
        print("==========================================\n")
        try:
            opcion=int(input("Digite una opción (número): "))
            if opcion==1:
                sistema_poke.listar_generacion()
            elif opcion==2:
                sistema_poke.listar_forma()
            elif opcion==3:
                sistema_poke.listar_habilidad()
            elif opcion==4:
                sistema_poke.listar_habitat()
            elif opcion==5:
                sistema_poke.listar_tipo()
            elif opcion==6:
                opciones=False
            else:
                print("Ingrese de 1 a 6")
        except Exception as ex:
            print("¡Ocurrió un error! -> ", ex)
menu()