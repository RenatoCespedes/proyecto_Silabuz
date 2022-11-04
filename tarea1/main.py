import csv
lista_libros=[]
class Libro:
    def __init__(self):
        
        self.__id=0
        self.__titulo=""
        self.__genero=""
        self.__id_ISBN=""
        self.__editorial=""
        self.__autores=[]
def leer_archivo():
    print("Leer archivos CSV o txt")
def listar_libros():
    print("Listado de libros")
    for v,a in enumerate(lista_libros):
        print(f"{v} -> {a.titulo}, {a.genero}, {a.id_ISBN}, {a.editorial}, {a.autores}")
def agregar_libro():
    print("Agregar libro")
    print("Ingrese los siguientes datos del libro: ")
    nm=Libro()
    nm.titulo=input("Título del libro: ")
    nm.genero=input("Género del libro: ")
    nm.id_ISBN=input("ID o ISBN: ")
    nm.editorial=input("Editorial: ")
    nmk=int(input("Ingrese la cantidad de autores: "))
    autor=[]
    for vk in range(nmk):
        a=input(f"Ingrese el autor {vk+1}: ")
        autor.append(a)
    nm.autores=autor
    lista_libros.append(nm)
def eliminar_libro():
    print("Eliminar libro")
    eliminar=input("Ingrese el título del libro: ")
    for el in lista_libros:
        if el.titulo==eliminar:
            lista_libros.remove(el)
        else:
            print("¡No se encontró el libro!")
def buscar_libro():
    print("Buscar libro por ISBN o por título")
    busqueda=input("Ingrese ISBN o título del libro: ")
    for k in lista_libros:
        if k.id_ISBN==busqueda or k.titulo==busqueda:
            print(f"{k.titulo}, {k.genero}, {k.id_ISBN}, {k.editorial}, {k.autores}")
def ordenar_libros():
    print("Ordenar libros por título")
    orden_lista=[]
    for kv in lista_libros:
        orden_lista.append(kv.titulo)
    orden_lista_titulo=sorted(orden_lista)
    lista_libros_nuevo=[]
    for kv2 in orden_lista_titulo:
        for kv1 in lista_libros:
            if kv2==kv1.titulo:
                lista_libros_nuevo.append(kv1)
                print(f"{kv1.titulo}, {kv1.genero}, {kv1.id_ISBN}, {kv1.editorial}, {kv1.autores}")
def buscar_libros_autor_eg():
    print("Buscar libros por autor, editorial o género")
    print("Buscar libro por autor")
    autor=input("Ingrese el autor del libro: ").lower()
    for nk in lista_libros:
        for mk in nk.autores:
            if mk.lower()==autor:
                print(f"{nk.titulo}, {nk.genero}, {nk.id_ISBN}, {nk.editorial}, {nk.autores}")
            else:
                print("¡No hay resultados!")
def buscar_libros_num_autor():
    print("Buscar libros por el número de autores")
    num_autor=int(input("Ingrese la cantidad de autores: "))
    for numk in lista_libros:
        if len(numk.autores)==num_autor:
            print(f"{numk.titulo}, {numk.genero}, {numk.id_ISBN}, {numk.editorial}, {numk.autores}")
        else:
            print("¡No hay resultados!")
def editar_libros():
    print("Editar o actualizar datos de un libro")
def guardar_libros():
    print("Guardar libros (.CSV o .txt)")
    mi_archivo=open('biblioteca.csv','w',newline='')
    with mi_archivo:
        escritura = csv.writer(mi_archivo)
        escritura.writerows([["Título del libro, Género, ID_ISBN, Editorial, Autores"]])
        for lib in lista_libros:
            mi_dato=[[lib.titulo, lib.genero, lib.id_ISBN, lib.editorial, lib.autores]]
            escritura.writerows(mi_dato)
        print("¡Completado!")

