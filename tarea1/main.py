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

    #Funciones Set
    def set_id(self,i):
        self.__id=i
        
    def set_titulo(self,tittle):
        self.__titulo=tittle
    def set_genero(self,x):
        self.__genero=x
    def set_isbn(self,code):
        self.__id_ISBN=code
    def set_editorial(self,ed):
        self.__editorial=ed
    def set_autor(self,autor):
        self.__autores.append(autor)
    def set_attributes(self,id,titulo,genero,isbn,editorial,autores):
        self.__id=id
        self.__titulo=titulo
        self.__genero=genero
        self.__id_ISBN=isbn
        self.__editorial=editorial
        self.__autores=autores
    #Funciones Get
    def get_attributes(self):
        return self.__id,self.__titulo,self.__genero,self.__id_ISBN,self.__editorial,self.__autores
    
    def get_titulo(self):
        return self.__titulo
    def get_autores(self):
        return self.__autores
    def get_editorial(self):
        return self.__editorial
    def get_archivo(self):
        return self.__archivo
    def get_genero(self):
        return self.__genero
    def get_id(self):
        return self.__id
    def get_isbn(self):
        return self.__id_ISBN
    
    #Funciones
    def mostrar_autores(self):
        auto=self.__autores
        for i in range(len(auto)):
            if(i==len(auto)-1):
                print(f"{auto[i]}",end="\n")
            else:
                print(f"{auto[i]}",end=" ")

class Sistema_libros:
    def __init__(self,lista=[]):
        self.__archivo=""
        self.libro=Libro()
        self.lista_libros=lista
    #Funciones SET
    def set_list(self,libro):
        self.lista_libros.append(libro)
    
    def set_archivo(self,y):
        self.__archivo=y
    #Funciones GET
    def get_archivo(self):
        return self.__archivo
    def get_id_last_item(self):
        a=self.lista_libros[-1]
        id,_,_,_,_,_=a.get_attributes()
        return id
    #Funciones
    
    def leer_archivo(self):
        name=input("Ingrese el nombre archivo csv a cargar: ")
        with open(name) as f:
            x=csv.reader(f)
            next(x)
            for row in x :
                new_val=Libro()
                new_val.set_id(row[0])
                new_val.set_titulo(row[1])
                new_val.set_genero(row[2])
                new_val.set_isbn(row[3])
                new_val.set_editorial(row[4])
                lista=[]
                for l in str(row[5]):
                    if l.isalpha() or l==' ' or l==',':
                        lista.append(l)
                    new_row_5="".join(lista)
                                     
                val_autor=new_row_5.split(',')

                for k in val_autor:
                    new_val.set_autor(k)

                self.lista_libros.append(new_val)
    
    def listar_libros(self):
        print("Listado de libros")
        for v,a in enumerate(lista_libros):
            print(f"{v} -> {a.get_titulo()}, {a.get_genero()}, {a.get_isbn()}, {a.get_editorial()}",end=" ")
            a.mostrar_autores()

    def agregar_libro(self):
        print("Ingrese los siguientes datos del libro: ")
        nm=self.libro
        nm.set_titulo(input("Título del libro: ").title())
        nm.set_genero(input("Género del libro: ").lower())
        nm.set_isbn(input("ID o ISBN: ").upper())
        nm.set_id(int(self.get_id_last_item())+1)
        nm.set_editorial(input("Editorial: "))
        nmk=int(input("Ingrese la cantidad de autores: "))
        autor=[]
        for vk in range(nmk):
            a=input(f"Ingrese el autor {vk+1}: ")
            nm.set_autor(a)
        
        self.set_list(nm)
        print("Libro agregado a la coleccion")

    def eliminar_libro(self):
        eliminar=input("Ingrese el título del libro: ").lower()
        for el in self.lista_libros:
            if el.get_titulo().lower()==eliminar:
                self.lista_libros.remove(el)
                return True
        return False
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
def menu():
    recorrido=True
    while recorrido:
        print(" ")
        print("Menu\n")
        print("1.- Leer archivo (.CSV o .txt)")
        print("2.- Listar libros")
        print("3.- Agregar libro")
        print("4.- Eliminar libro")
        print("5.- Buscar libro por ISBN o por título")
        print("6.- Ordenar libros por título")
        print("7.- Buscar libros por autor, editorial o género")
        print("8.- Buscar libros por número de autores")
        print("9.- Editar o actualizar datos de un libro")
        print("10.-Guardar libros (.CSV o .txt)")
        print("11.-Salir")
        print(" ")
        try:
            opcion=int(input('Ingrese una opción: '))
            if opcion==1:
                leer_archivo()
            elif opcion==2:
                listar_libros()
            elif opcion==3:
                agregar_libro()
            elif opcion==4:
                eliminar_libro()
            elif opcion==5:
                buscar_libro()
            elif opcion==6:
                ordenar_libros()
            elif opcion==7:
                buscar_libros_autor_eg()
            elif opcion==8:
                buscar_libros_num_autor()
            elif opcion==9:
                editar_libros()
            elif opcion==10:
                guardar_libros()
            elif opcion==11:
                recorrido=False
            else:
                print("Ingrese una opción de 1 a 11")
        except Exception as ex:
            print(f"¡Ocurrió un Error!, {ex}")
menu()

