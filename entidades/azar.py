import random

"""En este modulo trate de hacer una clase y una función donde
el sistema trataria de adivinar tu numero ingresado por usted,
esto usando la libreria random y usando variables para
utilizar ' randint ' con un rango del 1 al 10"""

""" ' randint ' significa la libreria random e 'int ' de numero entero
osea que manejaremos numeros enteros a random"""

"""El codigo funciona en base la clase creada
haciendo un constructor init cuyos parametros
son self number, despues con una función adivinar
que recibe self sera el numero a adivinar"""

"""Tu tienes que ingresar el numero y ver
si adivinas el valor que el sistema eligio
con randint"""

class Adivinar:
    def __init__(self, number):
        self.number = number
    
    def adivinar(self):
        #el número aleatorio a adivinar
        secreto = random.randint(1, 10)
        
        #la entrada del usuario
        intento = int(input("¿Cual sería el numero? "))
        
        
        if intento == secreto:
            print("Correcto")
        else:
            print(f"Incorrecto, era {secreto}")




