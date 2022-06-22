# Clases desarrolladas

class Tienda:
    '''
    Clase con los compionenetes de una tienda de electrodomésticos
    Atributos:
        tipo = 'Electrodomésticos' -> String
        abierto = True -> Bool
    '''
    tipo = 'Electrodomésticos'
    abierto = True

    def __init__(self, nombre:str, direccion:str, n_empleados:int, ventas_3m:list):
        '''
        Atributos particulares de una tienda
        Input:
            nombre: string
            direccion: string
            n_empleados: string
            ventas_3m: list
        '''
        self.nombre = nombre
        self.direccion = direccion
        self.n_empleados = n_empleados
        self.ventas_3m = ventas_3m
        # self.show_class()

    def ventas_totales(self):
        '''
        Método que suma todas las ventas de la tienda
        Output:
            Valor total de ventas -> float/int
        '''
        return sum(self.ventas_3m)

    def media_ventas_emp(self):
        '''
        Método que calcula las ventas por empleados de los últimos 3 meses
        Output:
            Media de ventas por empleado -> float/int
        '''
        return self.ventas_totales()/self.n_empleados

    def nombre_direc(self):
        '''
        Método que devuelve el nombre y dirección de la tienda
        Output:
            Nombre y dirección -> string
        '''
        return self.nombre + ' ' + self.direccion

    def ult_ventas(self):
        '''
        Método que devuelve las ventas del últimos mes
        Output:
            Ventas último mes -> float/int
        '''
        return self.ventas_3m[-1]

    def prox_ventas(self, inversion_mark):
        '''
        Método que devuelve la proyección de las ventas en función a la inversión en marketing
        Input:
            inversion_mark -> float/int
        Output:
            Proyección de ventas -> list
        '''
        for i in range(len(self.ventas_3m)):
            if inversion_mark < 1000:
                self.ventas_3m[i] = self.ventas_3m[i] * 1.2
            else:
                self.ventas_3m[i] = self.ventas_3m[i] * 1.5
        return self.ventas_3m
    
    def show_class(self):
        '''
        Método que muestra por pantalla los atributos y métodos de la clase
        '''
        print(self.tipo)
        print(self.abierto)
        print(self.nombre)
        print(self.direccion)
        print(self.n_empleados)
        print(self.ventas_3m)
        print(self.ventas_totales())
        print(self.media_ventas_emp())
        print(self.nombre_direc())
        print(self.ult_ventas())
        print(self.prox_ventas(1200))


class Perro():
    '''
    Clase de perro ejemplo
    Atributos generales:
        patas = 4 -> int
        orejas = 2 -> int
        ojos = 2 -> int
        velocidad = 0 -> float/int
    '''
    
    patas = 4
    orejas = 2
    ojos = 2
    velocidad = 0

    def __init__(self, raza:str, color="Marron", duenio=False):
        '''
        Los perros se diferencian unos de otros por los siguientes atributos particulares
        Inputs:
            raza -> String
            color -> String ("Marron" por defecto)
            duenio -> Bool (False por defecto)
        '''
        self.raza = raza
        self.color = color
        self.duenio = duenio

    def andar(self,aumento_velocidad):
        '''
        Método que aumenta el atributo de velocidad
        Input:
            aumento_velocidad -> float/int
        '''
        self.velocidad = self.velocidad + aumento_velocidad
    
    def parar(self):
        '''
        Método que detiene la velocidad y la actualiza a 0
        '''
        self.velocidad = 0

    def ladrar(self, mensaje):
        '''
        Método que devuelve un mensaje de perro
        Input:
            mensaje -> String
        Output:
            mensaje de perro -> String
        '''
        return "GUAU! " + str(mensaje)