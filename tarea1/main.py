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
                print("{:<8}".format(auto[i]),end="\n")
            else:
                print("{:<8}".format(auto[i]),end=",")

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
    def verify_title_if_exist(self,name):
        for i in self.lista_libros:
            titulo=i.get_titulo()
            if name.lower()==titulo.lower():
                return True
        return False
    def verify_isbn_if_exist(self,name):
        for i in self.lista_libros:
            isbn=i.get_isbn()
            if name.lower()==isbn.lower():
                return True
        return False

    
    def leer_archivo(self):
        while(True):
            print("1.-Cargar archivo csv")
            print("2.-Cargar archivo por defecto")
            opcion=int(input("Ingrese una opci??n: "))
            if opcion==1:
                name=input("Ingrese el nombre archivo csv a cargar: ")
                break
            elif opcion==2:
                name='libro.csv'
                break
            else:
                print("Opci??n v??lida")
                time.sleep(2)
                os.system('cls')
        with open(name) as f:
            x=csv.reader(f)
            next(x)
            for row in x :
                new_val=Libro()
                new_val.set_id(1 if self.lista_libros==[] else int(self.get_id_last_item())+1)
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
                if self.verify_title_if_exist(row[1]) or self.verify_isbn_if_exist(row[3]):
                    print("Dicha informaci??n ya esta registrado")
                    continue
                else:
                    self.lista_libros.append(new_val)
    
    def listar_libros(self):
        print("{:<38} {:<2}".format('','Listado de libros'.upper()))
        print("{:<4} {:<26} {:<15} {:<16} {:<15} {:<12}".format('ID','T??tulo','G??nero','ISBN','Editorial','Autores'))
        for v,a in enumerate(self.lista_libros,start=1):
            id,tit,gen,isb,edi,auto=a.get_attributes()
            print("{:<4} {:<26} {:<15} {:<16} {:<14} ".format(id, tit, gen, isb, edi),end=" ")
            a.mostrar_autores()

    def agregar_libro(self):
        print("Ingrese los siguientes datos del libro: ")
        nm=self.libro
        nm.set_titulo(input("T??tulo del libro: ").title())
        nm.set_genero(input("G??nero del libro: ").lower())
        isbn=input("ISBN: ")
        nm.set_isbn(isbn.upper())
        nm.set_id(1 if self.lista_libros==[] else int(self.get_id_last_item())+1)
        nm.set_editorial(input("Editorial: "))
        nmk=int(input("Ingrese la cantidad de autores: "))
        for vk in range(nmk):
            a=input(f"Ingrese el autor {vk+1}: ")
            nm.set_autor(a)
        if self.verify_isbn_if_exist(isbn):
            print(f"Existe un libro registrado con ISBN: {isbn} ")
            print("El ISBN es el DNI del libro, por lo tanto, no puede haber dos o m??s libros con el mismo ISBN")
            print("Genere el ISBN de su libro.")
        else:
            self.set_list(nm)
            print("Libro agregado a la colecci??n")

    def eliminar_libro(self):
        eliminar=input("Ingrese el t??tulo del libro: ").lower()
        for el in self.lista_libros:
            if el.get_titulo().lower()==eliminar:
                self.lista_libros.remove(el)
                return True
        return False
    def buscar_libro(self):
        busqueda=input("Ingrese ISBN o t??tulo del libro: ").lower()
        print("{:<38} {:<2}".format('','Resultados de la b??squeda'.upper()))
        print("{:<4} {:<26} {:<15} {:<16} {:<15} {:<12}".format('ID','T??tulo','G??nero','ISBN','Editorial','Autores'))
        for k in self.lista_libros:
            if k.get_isbn().lower()==busqueda or k.get_titulo().lower()==busqueda:
                id,titulo,genero,isbn,editoria,_=k.get_attributes()
                print("{:<4} {:<26} {:<15} {:<16} {:<14} ".format(id, titulo, genero, isbn, editoria),end=" ")
                k.mostrar_autores()
    def ordenar_libros(self):
        orden_lista=[]
        print("{:<38} {:<2}".format('','Libros ordenados por t??tulo'.upper()))
        orden_lista=[i.get_titulo().lower() for i in self.lista_libros]
        orden_lista_titulo=sorted(orden_lista)
        print("{:<4} {:<26} {:<15} {:<16} {:<15} {:<12}".format('ID','T??tulo','G??nero','ISBN','Editorial','Autores'))
        for kv2 in orden_lista_titulo:
            for kv1 in self.lista_libros:
                if kv2==kv1.get_titulo().lower():
                    id,titulo,genero,isbn,editoria,_=kv1.get_attributes()
                    print("{:<4} {:<26} {:<15} {:<16} {:<14} ".format(id, titulo, genero, isbn, editoria),end=" ")
                    kv1.mostrar_autores()
    def buscar_libros_autor(self):
        entrada=input("Ingrese el autor del libro: ").lower()
        print("{:<38} {:<2}".format('','Resultados de la b??squeda'.upper()))
        print("{:<4} {:<26} {:<15} {:<16} {:<15} {:<12}".format('ID','T??tulo','G??nero','ISBN','Editorial','Autores'))
        for nk in self.lista_libros:
            for mk in nk.get_autores():
                if mk.lower().lstrip()==entrada:
                    id,titulo,genero,isbn,editoria,_=nk.get_attributes()
                    print("{:<4} {:<26} {:<15} {:<16} {:<14} ".format(id, titulo, genero, isbn, editoria),end=" ")
                    nk.mostrar_autores()

    def buscar_libro_editorial(self):
        entrada=input("Ingrese la editorial del libro: ").lower()
        print("{:<38} {:<2}".format('','Resultados de la b??squeda'.upper()))
        print("{:<4} {:<26} {:<15} {:<16} {:<15} {:<12}".format('ID','T??tulo','G??nero','ISBN','Editorial','Autores'))
        for x in self.lista_libros:
            if x.get_editorial().lower() ==  entrada:
                id,titulo,genero,isbn,editoria,_=x.get_attributes()
                print("{:<4} {:<26} {:<15} {:<16} {:<14} ".format(id, titulo, genero, isbn, editoria),end=" ")
                x.mostrar_autores()
    
    def buscar_libro_genero(self):
        entrada=input("Ingrese el g??nero del libro: ").lower()
        print("{:<38} {:<2}".format('','Resultados de la B??squeda'.upper()))
        print("{:<4} {:<26} {:<15} {:<16} {:<15} {:<12}".format('ID','T??tulo','G??nero','ISBN','Editorial','Autores'))
        for x in self.lista_libros:
            if x.get_genero().lower() ==  entrada:
                id,titulo,genero,isbn,editoria,_=x.get_attributes()
                print("{:<4} {:<26} {:<15} {:<16} {:<14} ".format(id, titulo, genero, isbn, editoria),end=" ")
                x.mostrar_autores()
    
    def buscar_libros_num_autor(self):
        num_autor=int(input("Ingrese la cantidad de autores: "))
        print("{:<38} {:<2}".format('','Resultados de la b??squeda'.upper()))
        print("{:<4} {:<26} {:<15} {:<16} {:<15} {:<12}".format('ID','T??tulo','G??nero','ISBN','Editorial','Autores'))
        for x in self.lista_libros:
            if len(x.get_autores())==num_autor:
                id,titulo,genero,isbn,editorial,_=x.get_attributes()
                print("{:<4} {:<26} {:<15} {:<16} {:<14} ".format(id, titulo, genero, isbn, editorial),end=" ")
                x.mostrar_autores()
    
    def editar_libro(self):
        id_libro=int(input("Ingrese el ID del libro a modificar: "))
        for x in self.lista_libros:
            if int(x.get_id())==id_libro:
                id,titulo,genero,isbn,editorial,autor=x.get_attributes()
                print("{:<38} {:<2}".format('','Atributo cambiado'.upper()))
                print("{:<4} {:<26} {:<15} {:<16} {:<15} {:<12}".format('ID','T??tulo','G??nero','ISBN','Editorial','Autores'))
                print("{:<4} {:<26} {:<15} {:<16} {:<14} ".format(id, titulo, genero, isbn, editorial),end=" ")
                x.mostrar_autores()
                indice=self.lista_libros.index(x)
                self.lista_libros.remove(x)
                print("Las opciones a modificar son: ")
                print("1.- T??tulo\n2.- G??nero\n3.- ISBN\n4.- editorial\n5.- autor(es)\n6.- Atr??s")
                modif=int(input("??Qu?? desea modificar?: "))
                while(modif not in [1,2,3,4,5]):
                    modif=int(input("Opci??n no v??lida, vuelve a intentar: "))
                if modif==1:
                    mod_title=input("Ingrese el nuevo t??tulo: ").title()
                    titulo=mod_title
                    x.set_attributes(id,mod_title,genero,isbn,editorial,autor)
                elif modif==2:
                    mod_genero=input("Ingrese el nuevo g??nero: ")
                    genero=mod_genero
                    x.set_attributes(id,titulo,mod_genero,isbn,editorial,autor)
                elif modif==3:
                    mod_isbn=input("Ingrese el nuevo ISBN: ")
                    isbn=mod_isbn
                    x.set_attributes(id,titulo,genero,mod_isbn,editorial,autor)
                elif modif==4:
                    mod_edi=input("Ingrese la nueva editorial: ")
                    editorial=mod_edi
                    x.set_attributes(id,titulo,genero,isbn,mod_edi,autor)
                elif modif==5:
                    print("1.-Borrar autores del libro y agregar nuevos")
                    print("2.- Modificar un autor")
                    print("3.- Atr??s")
                    opcion=int(input("Ingrese una opci??n: "))
                    while(True):
                        if opcion==1:
                            number=int(input("??Cu??ntos desea agregar?: "))
                            autor=[]
                            for i in range(number):
                                mod_autor=input("Ingrese el autor: ")
                                autor.append(mod_autor)
                            x.set_attributes(id,titulo,genero,isbn,editorial,autor)
                            break
                        elif opcion==2:
                            print("Que autor desea cambiar:")
                            for i,j in enumerate(autor):
                                print(f"{i+1}.- {j}")
                            new_opcion=int(input("Ingrese una opci??n: "))
                            autor[new_opcion-1]=input("Ingrese el autor: ")
                            x.set_attributes(id,titulo,genero,isbn,editorial,autor)
                            break
                        elif opcion==3:
                            break
                        else:
                            print("Ingrese una opci??n v??lida")
                print("{:<38} {:<2}".format('','Atributo cambiado'.upper()))
                print("{:<4} {:<26} {:<15} {:<16} {:<15} {:<12}".format('ID','T??tulo','G??nero','ISBN','Editorial','Autores'))
                id1,titulo1,genero1,isbn1,editorial1,autor1=x.get_attributes()
                print("{:<4} {:<26} {:<15} {:<16} {:<14} ".format(id1, titulo1, genero1, isbn1, editorial1),end=" ")
                x.mostrar_autores()
                self.lista_libros.insert(indice,x)
    # def 
    def guardar_libros(self):
        print("Guardar libros en un archivo .CSV")
        mi_archivo=open('biblioteca.csv','w',newline='')
        with mi_archivo:
            escritura = csv.writer(mi_archivo)
            escritura.writerows([["ID,T??TULO, G??NERO, ISBN, EDITORIAL, AUTORES"]])
            for lib in self.lista_libros:
                id,titulo,genero,isbn,editorial,autor=lib.get_attributes()
                mi_dato=[[id,titulo, genero, isbn, editorial, autor]]
                escritura.writerows(mi_dato)
            print("??Completado!")
#Funcion limpiar
def pause_clear_console():
    while(True):
        if input("Presione enter para continuar....")!="":
            pass
        else:
            os.system('cls')
            break

def menu():
    recorrido=True
    print("=========== BIENVENIDO AL SISTEMA ================\n")
    while recorrido:
        print("*************** MEN?? BIBLIOTECA ******************\n")
        print("1.- Leer archivo .CSV")
        print("2.- Listar libros")
        print("3.- Agregar libro")
        print("4.- Eliminar libro")
        print("5.- Buscar libro por ISBN o por t??tulo")
        print("6.- Ordenar libros por t??tulo")
        print("7.- Buscar libros por autor, editorial o g??nero")
        print("8.- Buscar libros por n??mero de autores")
        print("9.- Editar o actualizar datos de un libro")
        print("10.-Guardar libros .CSV")
        print("11.-Salir")
        print(" ")
        print("**************************************************\n")
        libro=Sistema_libros()
        try:
            opcion=int(input('Ingrese una opci??n: '))
            if opcion==1:
                try:
                    libro.leer_archivo()
                except:
                    print("No se encontro archivo")
                    print("La estructura del Archivo es: ")
                    print("id,titulo,genero,isbn,editorial,autores")
                    print("Ejemplo:")
                    print("2,'La hora feliz','ficcion','99292929','vallejo','Luiz Ramos, Julia Valero'")
                pause_clear_console()
            elif opcion==2:
                libro.listar_libros()
                pause_clear_console()
            elif opcion==3:
                libro.agregar_libro()
                pause_clear_console()
            elif opcion==4:
                verificar=libro.eliminar_libro()
                if verificar:
                    print("Libro Eliminado")
                else:
                    print("No se encontr?? ning??n libro con ese t??tulo")
                pause_clear_console()
            elif opcion==5:
                print("Sugerencias de titulos: la ciuda y los perros, la ciudad de los tisicos, antiheroes")
                print("Sugerencias de ISBN: 9789972404375, 9786124262708, 9788416858378")
                libro.buscar_libro()
                pause_clear_console()
            elif opcion==6:
                libro.ordenar_libros()
                pause_clear_console()
            elif opcion==7:
                
                while(True):
                    print("1.- Buscar libro por autor")
                    print("2.- Buscar libro por editorial")
                    print("3.- Buscar libro por g??nero")
                    print("4.- Atr??s")
                    op=int(input("Ingrese una opci??n: "))
                    if op==1:
                        libro.buscar_libros_autor()
                        pause_clear_console()
                    elif op==2:
                        libro.buscar_libro_editorial()
                        pause_clear_console()
                    elif op==3:
                        verify=libro.buscar_libro_genero()
                        pause_clear_console()
                    elif op==4:
                        break
                pause_clear_console()    

            elif opcion==8:
                print("Buscar libros por el n??mero de autores")
                libro.buscar_libros_num_autor()
                pause_clear_console()
            elif opcion==9:
                libro.editar_libro()
                pause_clear_console()
            elif opcion==10:
                print("Guardar Libro")
                libro.guardar_libros()
                pause_clear_console()
            elif opcion==11:
                print("Gracias por usar el sistema")
                recorrido=False
            else:
                print("Ingrese una opci??n de 1 a 11")
        except Exception as ex:
            print(f"??Ocurri?? un Error!, {ex}")              
                    
menu()