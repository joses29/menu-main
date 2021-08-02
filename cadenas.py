class Cadena():
    def __init__(self,titulo="",opciones=[]):
        self.titulo = titulo
        self.opciones = opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc
    def recorrerCadena(self,cadena):
        len(cadena)
        print("La cadena es:"+ cadena+" y cuenta con: " +  str(len(cadena)) + " Caracteres")
        for i, c in enumerate(cadena):
            print('Caracter: %s' % (c))
    #Punto2
    def BuscarCaracter(self,cadena,buscador):
        acu = 0
        for i in range (len(cadena)):
            if (cadena[i]== buscador):
                acu+=1 
                print("Existe :" + str(acu))
                print("En el caracter: "+ str(i))
            else:
                print("No hay Coincidencia")
    ##Punto 3
    def listaPosiciones(self,cadena,caracter):
        for i, c in enumerate(cadena):
                print('Caracter: %s - Puesto: %i' % (c,i))
                if (cadena[i]== caracter):
                    print('El Caracter : %s - Se encuentra en el Puesto: %i' % (c,i))
    ##Punto 4
    def listaPalabras(self):
        frase=input("Ingrese la Oracion\n")
        Palabras = frase.split()
        print(Palabras)
        print(len(Palabras))
    ##Punto5
    def ListaPalabras(self,Palabras):
        Lista=[]
        ##Palabras=str(input("Ingrese una palabra, al finaizar use el punto\n"))
        while Palabras!=".":
            Lista.append(Palabras)
            Palabras=str(input("Ingrese una palabra, al finaizar use el punto\n"))
        print("La Lista seria\n"+ str(Lista))
        Cad=" ".join(Lista)
        print("La Cadena seria\n"+ str(Cad))
    #def InsertarDato(self,buscado,posicion):
    def InsertarDato(self,buscado:str,posicion):
        cadena = input('Ingresa una cadena: ')
        d = cadena.split()
        d.insert(posicion,buscado)
        print(d)
    def eliminarOcurrencia(self,buscado:str):
        cadena = input('Ingresa una cadena: ')
        d = cadena.split(buscado)
        lista = ''.join(d)
        print(lista)
    def retornarValor(self,posicion):
        cadena = input('Ingresa una cadena: ')
        d = cadena.split()
        valor = d[posicion]
        d.pop(posicion)
        return valor
    def concatenarCadena(self,dato):
        cadena = input('Ingresa una cadena: ')
        print(cadena + dato)

