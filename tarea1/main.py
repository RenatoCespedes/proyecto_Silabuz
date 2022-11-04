import csv
import os
import time
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
    def buscar_libro(self):
        busqueda=input("Ingrese ISBN o título del libro: ").lower()
        for k in self.lista_libros:
            if k.get_isbn().lower()==busqueda or k.get_titulo().lower()==busqueda:
                id,titulo,genero,isbn,editoria,_=k.get_attributes()
                print(f"{id} ,{titulo}, {genero}, {isbn}, {editoria}, ",end="")
                k.mostrar_autores()
    def ordenar_libros(self):
        orden_lista=[]
        orden_lista=[i.get_titulo().lower() for i in self.lista_libros]
        orden_lista_titulo=sorted(orden_lista)
        for kv2 in orden_lista_titulo:
            for kv1 in self.lista_libros:
                if kv2==kv1.get_titulo().lower():
                    id,titulo,genero,isbn,editoria,_=kv1.get_attributes()
                    print(f"{titulo}, {genero}, {isbn}, {editoria}, ",end="")
                    kv1.mostrar_autores()
    def buscar_libros_autor_eg(self):
        print("Buscar libros por autor, editorial o género")
        print("Buscar libro por autor")
        entrada=input("Ingrese el autor del libro: ").lower()
        for nk in self.lista_libros:
            for mk in nk.get_autores():
                if mk.lower()==entrada:
                    id,titulo,genero,isbn,editoria,_=nk.get_attributes()
                    nk.mostrar_autores()
                    print(f"{titulo}, {genero}, {isbn}, {editoria} ")

    def buscar_libro_editorial(self):
        entrada=input("Ingrese la editorial del libro: ").lower()
        for x in self.lista_libros:
            if x.get_editorial().lower() ==  entrada:
                print("Se encontro una coincidencia")
                id,titulo,genero,isbn,editoria,_=x.get_attributes()
                print(f"{id}, {titulo}, {genero}, {isbn}, ",end="")
                x.mostrar_autores()
    
    def buscar_libro_genero(self):
        entrada=input("Ingrese el genero del libro: ").lower()
        for x in self.lista_libros:
            if x.get_genero().lower() ==  entrada:
                print("Se encontro una coincidencia")
                id,titulo,genero,isbn,editoria,_=x.get_attributes()
                print(f"{id}, {titulo}, {isbn}, {editoria}, ",end="")
                x.mostrar_autores()
    
    def buscar_libros_num_autor(self):
        num_autor=int(input("Ingrese la cantidad de autores: "))
        for x in self.lista_libros:
            if len(x.get_autores())==num_autor:
                id,titulo,genero,isbn,editorial,_=x.get_attributes()
                print(f"{id}, {titulo}, {genero}, {isbn}, {editorial}, ",end="")
                x.mostrar_autores()
    
    def editar_libro(self):
        id_libro=int(input("Ingrese el id del libro a modificar: "))
        for x in self.lista_libros:
            # print(type(x.get_id()))
            if int(x.get_id())==id_libro:
                id,titulo,genero,isbn,editorial,autor=x.get_attributes()
                print(f"{id}, {titulo}, {genero}, {isbn}, {editorial}, ",end="")
                x.mostrar_autores()
                indice=self.lista_libros.index(x)
                self.lista_libros.remove(x)
                print("Las opciones a modificar son: ")
                print("1.- Titulo\n2.- Genero\n3.- Isbn\n4.- editorial\n5.- autor(es)")
                modif=int(input("Que desea modificar?: "))
                while(modif not in [1,2,3,4,5]):
                    modif=input("Opcion no valida, vuelve a intentar: ")
                if modif==1:
                    mod_title=input("Ingrese el nuevo titulo: ").title()
                    titulo=mod_title
                    x.set_attributes(id,mod_title,genero,isbn,editorial,autor)
                elif modif==2:
                    mod_genero=input("Ingrese el nuevo genero: ")
                    genero=mod_genero
                    x.set_attributes(id,titulo,mod_genero,isbn,editorial,autor)
                elif modif==3:
                    mod_isbn=input("Ingrese el nuevo isbn: ")
                    isbn=mod_isbn
                    x.set_attributes(id,titulo,genero,mod_isbn,editorial,autor)
                elif modif==4:
                    mod_edi=input("Ingrese la nueva editorial: ")
                    editorial=mod_edi
                    x.set_attributes(id,titulo,genero,isbn,mod_edi,autor)
                elif modif==5:
                    number=int(input("Cuantos desea agregar: "))
                    autor=[]
                    for i in range(number):
                        mod_autor=input("Ingrese el autor: ")
                        autor.append(mod_autor)
                    x.set_attributes(id,titulo,genero,isbn,editorial,autor)
                print("Atributos cambiados....")
                id1,titulo1,genero1,isbn1,editorial1,autor1=x.get_attributes()
                print(f"{id1}, {titulo1}, {genero1}, {isbn1}, {editorial1}, ",end="")
                x.mostrar_autores()
                self.lista_libros.insert(indice,x)
    def guardar_libros(self):
        print("Guardar libros en un archivo .CSV")
        mi_archivo=open('biblioteca.csv','w',newline='')
        with mi_archivo:
            escritura = csv.writer(mi_archivo)
            escritura.writerows([["ID,TITULO, GENERO, ISBN, EDITORIAL, AUTORES"]])
            for lib in self.lista_libros:
                id,titulo,genero,isbn,editorial,autor=lib.get_attributes()
                mi_dato=[[id,titulo, genero, isbn, editorial, autor]]
                escritura.writerows(mi_dato)
            print("¡Completado!")
def menu():
    recorrido=True
    print("---------------- Bienvenido al Sistema ----------------\n")
    while recorrido:
        print("*******Menu Biblioteca*******\n")
        print("1.- Leer archivo .CSV")
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
        libro=Sistema_libros()
        try:
            opcion=int(input('Ingrese una opción: '))
            if opcion==1:
                # entrada=input("Ingrese el archivo a leer: ")
                libro.leer_archivo()
                time.sleep(1)
                input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')
            elif opcion==2:
                libro.listar_libros()
                time.sleep(1)
                input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')
            elif opcion==3:
                libro.agregar_libro()
                time.sleep(1)
                input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')
            elif opcion==4:
                verificar=libro.eliminar_libro()
                if verificar:
                    print("Libro Eliminado")
                else:
                    print("No se encontro ningun libro con ese titulo")
                time.sleep(1)
                input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')
            elif opcion==5:
                libro.buscar_libro()
                time.sleep(1)
                input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')
            elif opcion==6:
                libro.ordenar_libros()
                time.sleep(1)
                input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')
            elif opcion==7:
                
                while(True):
                    print("1.- Buscar libro por autor")
                    print("2.- Buscar libro por editorial")
                    print("3.- Buscar libro por genero")
                    print("4.- Atras")
                    op=int(input("Ingrese una Opcion: "))
                    if op==1:
                        verify=libro.buscar_libros_autor()
                        # time.sleep(1)
                        input("Presiona enter para regresar al menu ........")
                        os.system('cls')
                    elif op==2:
                        libro.buscar_libro_editorial()
                        # time.sleep(1)
                        input("Presiona enter para regresar al menu ........")
                        os.system('cls')
                    elif op==3:
                        verify=libro.buscar_libro_genero()
                        # time.sleep(1)
                        input("Presiona enter para regresar al menu ........")
                        os.system('cls')
                    elif op==4:
                        break
                # time.sleep(1)
                # input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')    

            elif opcion==8:
                print("Buscar libros por el número de autores")
                libro.buscar_libros_num_autor()
                time.sleep(1)
                input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')
            elif opcion==9:
                # print("9.- Editar o actualizar datos de un libro")
                libro.editar_libro()
                time.sleep(1)
                input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')
            elif opcion==10:
                print("10.- Guardar Libro")
                libro.guardar_libros()
                time.sleep(1)
                input("Presiona enter para regresar al menu ........")
                # time.sleep(1)
                os.system('cls')
            elif opcion==11:
                print("Gracias por usar el sistema")
                recorrido=False
            else:
                print("Ingrese una opción de 1 a 11")
        except Exception as ex:
            print(f"¡Ocurrió un Error!, {ex}")              
                    
menu()

