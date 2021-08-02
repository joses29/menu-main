from calculadora import *
from operacionnumeros import *
from listas import *
from cadenas import *
import os
class Menu:
    def __init__(self, titulo='', opciones=[]):
        self.titulo = titulo
        self.opciones = opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input('Elija opcion [1...{}]: '.format(len(self.opciones)))
        return opc

opc = ''
while opc != '5':
    #os.system("cls")
    menu = Menu('MENU PRINCIPAL', ['1) Calculadora', '2) Operacion numeros', '3) Tratamiento de listas', '4) Operacion de cadenas', '5) Salir'])
    opc = menu.menu()
    if opc == '1':
        opc1 = ''
        while opc1 != '10':
            os.system("cls")
            menu1 = Menu('//--MENU CALCULADORA--//', ['1) Suma', '2) Resta', '3) Multiplicacion', '4) Division', '5) Exponente', '6) valor absoluto', '7) circunferencia', '8) area circulo','9) Area cuadrado', '10) Salir'])
            opc1 = menu1.menu()
            if opc1 == '1':
                os.system("cls")
                print('Suma')
                n1=float(input("Ingrese el primer numero: "))
                n2=float(input("Ingrese el segundo numero: "))
                obj1=calCientifica(n1,n2)
                print(("{} + {} = {}").format(n1,n2,obj1.suma()))
                input("Presione una tecla para continuar...")

            if opc1 == '2':
                os.system("cls")
                print('Resta')
                n1=float(input("Ingrese el primer numero: "))
                n2=float(input("Ingrese el segundo numero: "))
                obj1=calCientifica(n1,n2)
                print(("{} - {} = {}").format(n1,n2,obj1.resta()))
                input("Presione una tecla para continuar...")

            if opc1 == '3':
                os.system("cls")
                print('Multiplicacion')
                n1=float(input("Ingrese el primer numero: "))
                n2=float(input("Ingrese el segundo numero: "))
                obj1=calCientifica(n1,n2)
                print(("{} * {} = {}").format(n1,n2,obj1.multiplicacion()))
                input("Presione una tecla para continuar...")

            if opc1 == '4':
                os.system("cls")
                print('Division')
                n1=float(input("Ingrese el primer numero: "))
                n2=float(input("Ingrese el segundo numero: "))
                obj1=calCientifica(n1,n2)
                print(("{} / {} = {}").format(n1,n2,obj1.division()))
                input("Presione una tecla para continuar...")
            
            if opc1 == '5':
                os.system("cls")
                print('Exponente')
                n1=float(input("Ingrese el primer numero: "))
                n2=float(input("Ingrese el segundo numero: "))
                obj1=calEstandar(n1,n2)
                print(("{} ** {} = {}").format(n1,n2,obj1.exponente()))
                input("Presione una tecla para continuar...")

            if opc1 == '6':
                os.system("cls")
                print('Valor Absoluto')
                n=float(input("Ingrese un numero: "))
                obj1=calEstandar()
                print(("el numero es :{} , en valor absoluto: {}").format(n,obj1.valorAbsoluto(n)))
                input("Presione una tecla para continuar...")

            if opc1 == '7':
                os.system("cls")
                print('Circunferencia')
                rad = float(input("Ingrese el radio: "))
                obj1=calCientifica(radio=rad)
                print(("la cinfunferencia es : {}").format(round(obj1.circunferencia(),2)))
                input("Presione una tecla para continuar...")

            if opc1 == '8':
                os.system("cls")
                print('Area del circulo')
                rad = float(input("Ingrese el radio: "))
                obj1=calCientifica(radio=rad)
                print(("el area del circulo es : {}").format(round(obj1.areaCirculo(),2)))
                input("Presione una tecla para continuar...")
            
            if opc1 == '9':
                os.system("cls")
                print('Area Cuadrado')
                lado = float(input("Ingrese un lado del cuadrado: "))
                obj1=calCientifica()
                print(("el area del cuadrado es : {}").format(obj1.areaCuadrado(lado)))
                input("Presione una tecla para continuar...")

    elif opc == '2':
        opc1 = ''
        while opc1 != '11':
            os.system("cls")
            menu1 = Menu('//--OPERACION NUMEROS--//', ['1) Presentar los números de 1 a n', '2) Sumar los números de 1 a n', '3) Múltiplo de cualquier numero', '4) Presentar los divisores de un numero', '5) Numero Primo', '6) Factorial de cualquier numero', '7) Fibonacci de una serie de n números', '8) Numero Perfecto','9) Primos gemelos', '10) Números amigos','11) Salir'])
            opc1 = menu1.menu()
            if opc1 == '1':
                os.system("cls")
                print('PRESENTAR NUMEROS DE 1 HASTA N')
                n=int(input("Ingrese hasta que numero desea presentar en pantalla :"))
                obj = Basico(n)
                obj.numerosN()
                input("Presione una tecla para continuar...")

            if opc1 == '2':
                os.system("cls")
                print('SUMA DE NUMEROS DE 1 HASTA N')
                n=int(input("Ingrese el numero hasta el que desea sumar :"))
                obj = Basico(n)
                print('La suma de 1 hasta {} es : {} '.format(n,obj.sumaN()))
                input("Presione una tecla para continuar...")

            if opc1 == '3':
                os.system("cls")
                print('MULTIPLOS')
                n=int(input("Ingrese el numero que desea saber sus multiplos :"))
                obj = Basico(n)
                print('Los primeros 10 multiplos de {} son:'.format(n))
                obj.multiplo()
                input("Presione una tecla para continuar...")   

            if opc1 == '4':
                os.system("cls")
                print('DIVISORES DE UN NUMERO')
                n=int(input("Ingrese un numero :"))
                obj = Basico(n)
                print('Los divisores de {} son:'.format(n))
                obj.DivisoresNumero()
                input("Presione una tecla para continuar...")

            if opc1 == '5':
                os.system("cls")
                print('NUMERO PRIMO')
                n=int(input("Ingrese un numero para comprobar si es primo (hasta 100):"))
                obj = Basico()
                obj.primo(n)
                input("Presione una tecla para continuar...")
            
            if opc1 == '6':
                os.system("cls")
                print('FACTORIAL')
                n=int(input("Ingrese el numero para calcular su factorial :"))
                obj= Intermedio()
                print("El factorial de {} es : {}".format(n,obj.factorial(n)))
                input("Presione una tecla para continuar...")

            if opc1 == '7':
                os.system("cls")
                print("FIBONACCI")
                sel = True
                preg ="y"
                while sel:
                    if preg.lower() == "y":
                        n = int(input("Ingrese un numero : "))
                        obj=Intermedio()
                        obj.fibonacci(n) 
                        print()
                        print()
                        preg = input ("Desea continuar ? digite (y) para seguir: ")
                    else:
                        sel = False

            if opc1 == '8':
                os.system("cls")
                print('NUMERO PERFECTO')
                n=int(input("Ingrese un numero para comprobar si es perfecto :"))
                obj= Basico(n)
                obj.perfecto()
                input("Presione una tecla para continuar...")   

            if opc1 == '9':
                os.system("cls")
                print('PRIMOS GEMELOS')
                n1=int(input("Ingrese el primer numero :"))
                n2=int(input("Ingrese el segundo numero :"))
                obj= Intermedio()
                obj.primosgemelos(n1,n2)
                input("Presione una tecla para continuar...")  

            if opc1 == '10':
                os.system("cls")
                print('NUMEROS AMIGOS')
                n1=int(input("Ingrese el primer numero :"))
                n2=int(input("Ingrese el segundo numero :"))
                obj= Intermedio()
                obj.numerosamigos(n1,n2)
                input("Presione una tecla para continuar...")
    elif opc == '3':
        
        print('Operacion con listas')
        menu = Lista("Menu Principal",["1) Recorrer y presentar los datos de una lista","2) Buscar un valor en una lista","3) Retornar una lista con factoriales",
                              "4) Retornar una lista numeros primos","5) Recorrer una lista de diccionario con notas de alumnos ","6) Insertar un dato en una Lista dada lo Posición",
                              "7) Eliminar todas las ocurrencias en una Lista","8) Retornar cualquier valor de una lista eliminándolo ","9)	Copiar cada elemento de una tupla en una lista",
                              "10) Dar el vuelto a varios clientes","11) Salir"])
        op = menu.menu()
        if op == '1':
            menu.presentarLista()
        if op == '2':
            menu.buscarLista('')
        if op == '3':
            menu.listaFactorial()
        if op == '4':
            menu.listaPrimo()
        if op == '5':
            dic = [{}]
            menu.listaNotas()
        if op == '6':
            menu.insertarLista('',0)
        if op == '7':
            menu.eliminarLista('0')
        if op == '8':
            menu.retornaValorLista(0)
        if op == '9':
            tupla = ()
            menu.copiarTuplaLista(tupla)
        if op == '10':
            menu.vueltoLista()
        if op == '11':
            exit()
    elif opc == '4':
        cad = Cadena("Menu Principal",["1) Recorrer y presentar los datos de una cadena","2) Buscar un carácter en una cadena","3)Retornar una lista con las posiciones dado un carácter de la cadena",
                              "4) Retornar una lista con todas las palabras de una cadena","5) Retornar una cadena a partir de una lista ","6) Insertar un dato en una cadena dada lo Posición",
                              "7) Eliminar todas las ocurrencias en una cadena","8) Retornar cualquier valor de una cadena eliminándolo  ","9) Concatenar cadenas","11) Salir"])
        op = cad.menu()
        if op == '1':
            cadena = input("Ingrese una palabra: " )
            cad.recorrerCadena(cadena)
        if op == '2':
            cadena = input("Ingrese una palabra: " )
            buscador = input("Ingrese el caracter a buscar: " )
            cad.BuscarCaracter(cadena,buscador)
        if op == '3':
            cadena = input("Ingrese una palabra: " )
            caracter= input("ingrese El caracter a buscar en lista: ")
            cad.listaPosiciones(cadena,caracter)
        if op == '4':
            Palabras= str("ingrese sus palabras, al finalizar use el punto\n")
            cad.listaPalabras()
        if op == '5':
            Palabras=str(input("Ingrese una palabra, al finaizar use el punto\n"))
            cad.ListaPalabras(Palabras)
        if op == '6':
            cad.InsertarDato('',0)
        if op == '7':
            cad.eliminarOcurrencia('')
        if op == '8':
            cad.retornarValor(0)
        if op == '9':
            cad.concatenarCadena('')
        if op == '10':
            exit()
    elif opc == '5':
        exit()                  



