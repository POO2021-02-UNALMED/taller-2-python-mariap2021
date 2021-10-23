class Asiento:
    def __init__(self, color,precio,registro):
        self.color= color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color=="amarillo" or color=="negro" or color=="blanco" or color=="verde" or color=="rojo":
            self.color=color 





class Auto:

    CantidadCreados=0

    def __init__(self, modelo,precio,asientos,marca,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.registro=registro

    def cantidadAsientos(self): 
        n= 0
        for i in self.asientos:
            if i != None:
                n += 1
        return n       

	

    def verificarIntegridad(self): 
        for i in self.asientos:
            if i != None:
                 if i.registro!=self.registro or self.registro!=self.motor.registro or i.registro!= self.motor.registro:
                     return "Las piezas no son originales"
                     break
                
        return "Auto original"          

    

        

class Motor:
    def __init__(self, numeroCilindros,tipo,registro):
        self.numeroCilindros= numeroCilindros
        self.tipo= tipo
        self.registro= registro


    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if(tipo=="gasolina" or tipo=="electrico"):
            self.tipo=tipo  