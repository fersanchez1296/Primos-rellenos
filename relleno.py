"""
Practica #1--->Primos rellenos

Fernando Sánchez Plascencia--->219341143   
Luis Davis Olvera Aguilera---->219341178
Juan Carlos Duran Zepeda------>219893731
Luis Alberto Ruelas Batbosa--->215537205

Entrega: Marzo 10 2021

Descripción:
Realiza un programa en Python que, dado un valor inicial y un valor final 
(1<= ini <= fin <= 10,000,000), el programa deberá mostrar en pantalla los 
números primos rellenos que existe entre ini y fin (incluyendolos).


Conclusión: La realización del presente código represento un gran reto, debido que aunque
el planteamiento suena sencillo, la practica es totalmente diferente ya que habia que hacer
modificaciones al algoritmo original para obtener que numeros son primos, y a este algoritmo
agregar como numero primo el numero 1, ya que este, naturalmente no está considerado como
numero primo. Fue un gran reto ya que habia que modificar el algoritmo que hemos conocido por 
mucho tiempo.
Hemos aprendido a pensar de una manera diferente, ya que al parecer un ejercicio facil y al no 
serlo, tuvimos que replantear lo que ya sabiamos, tuvimos que abstraernos de una manera diferente
para adaptarnos a los requerimientos que se nos pedian.
A pesar del gran reto del presente problema, logramos resolverlo de una manera favorable(esperamos),
el trabajo en equipo fue clave para resolver este problema.
El reto mas grande fue fue modificar el algoritmo para los numeros primos para que aceptara
al numero 1 como primo,ya que este, matematicamente no tiene divisores enteros,o divisor alguno
y es por esta razon por lo que no se considera un numero primo, posteriormente solo fue cuestion
de separar el numero en cifras, en decenas, centeas, unidades, etc...
"""



x,y = input().split() #se ingresan los valores 
x=int(x) #casting de la variable x
y=int(y)# casting de la variable y

#declaramos una función, la cual es la encargada de resolver si un numero
#es primo o no lo es, se le pasa un valor como argumento y retorna un valor de tipo bool

"""
En el programa principal se repiten ciertas instrucciones a las cuales solo se les 
hizo la modificación de valores y conforme el numero se va haciendo mas grande
se van extrallendo cifras de la manera n1, n1n2,n1n2n3...etc segun lo requiera cada
numero.
se explicaran dos bloques, ya que como mencioné, el código es el mismo pero con 
ciertas modificaciones que se pueden observar a simple vista y no son de difcil
comprension.
"""

def Primo(a): 
    Divisiones = 0 #variable encargada de almacenar el total de divisores de un numero
    if a==1: #si el argumento "a" es un 1, se le considera primo
        return True
    else: #si el argumento "a" no es 1, se realiza el algoritmo abitual
        for i in range(1,a+1): #se itera en un rango, desde 1 hasta a+1
            if a % i == 0: # se utiliza el modulo para saber el total de divisores
                Divisiones = Divisiones +1 #si un valor de i dividio a "a" se incrementa el contador
                if Divisiones >2:#si se tienen mas de dos divisores, el numero no es primo
                    return False
        if Divisiones < 2: #si se tienen menos de dos divisores, el numero no es primo
            return False
        elif Divisiones ==2:# si se tienen exactamente dos divisores, el numero es primo
            return True

if(x>0 and y<=10000000): #los valores no pueden ser menores o superiores a este rango
    for i in range(x,y+1): #iteramos sobre los valores
        if i>=1 and i<=9: #comparamos entre que valores está i
            resultado=Primo(i) #asignmos una variable y le asignamos el valor devuelto por la funcion
            if resultado!=False: #segun el retorno de la funcion
                print(i)# imprimimos el valor de i que cumple con ser un primo relleno
        elif(i>=10 and i<=99): #repetimos la sentencia anterior pero aumentamos los valores para i
            d=i//10 #obtenemos el primer digito del numero
            resultadod=Primo(d) #llamos a la funcion para el digito extraido
            resultado=Primo(i) #pasamos la cifra completa
            if(resultadod!=False and resultado!=False):#segun el retorno de la funcion
                print(i)# imprimimos el valor de i que cumple con ser un primo relleno
        elif(i>=100 and i<=999):
            c=i//100
            d=i//10
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
        elif(i>=1000 and i<=9999):
            m=i//1000
            c=i//100
            d=i//10
            resultadom=Primo(m)
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadom!=False and resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
        elif(i>=10000 and i<=99999):
            dm=i//1000
            m=i//1000
            c=i//100
            d=i//10
            resultadodm=Primo(dm)
            resultadom=Primo(m)
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadodm!=False and resultadom!=False and resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
        elif(i>=100000 and i<=999999):
            cm=i//10000
            dm=i//1000
            m=i//1000
            c=i//100
            d=i//10
            resultadocm=Primo(cm)
            resultadodm=Primo(dm)
            resultadom=Primo(m)
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadocm!=False and resultadodm!=False and resultadom!=False and resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
        elif(i>=1000000 and i<=10000000):
            M=i//100000
            cm=i//10000
            dm=i//1000
            m=i//1000
            c=i//100
            d=i//10
            resultadoM=Primo(M)
            resultadocm=Primo(cm)
            resultadodm=Primo(dm)
            resultadom=Primo(m)
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadoM!=False and resultadocm!=False and resultadodm!=False and resultadom!=False and resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
else:
    print("Valores Invalidos") # si el rango ingresado sobrepasa los valores delimitados
    #se muestra este mensaje
            
        