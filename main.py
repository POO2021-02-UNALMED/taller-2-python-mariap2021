class Asiento:
    def __init__(self, color,precio,registro):
        self.color= color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color=="amarillo" or color=="negro" or color=="blanco" or color=="verde" or color=="rojo":
            self.color=color 


class Motor:
    def __init__(self, numeroCilindros,tipo,registro):
        self.numeroCilindros= numeroCilindros
        self.tipo= tipo
        self.registro= registro


    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo=="gasolina" or tipo=="electrico":
            self.tipo=tipo  


class Auto:

    CantidadCreados=0

    def __init__(self, modelo,precio,asientos,marca,motor,registro):
        self.modelo= modelo
        self.precio= precio
        self.asientos= asientos
        self.marca= marca
        self.registro= registro
        self.motor=motor

    def cantidadAsientos(self):
        numero= 0
        for i in self.asientos:
            if type(i) == Asiento:
                numero +=1
        return numero        
    
    def verificarIntegridad(self):
        


        for i in self.asientos:
            if type(i)== Asiento:
                if(i.registro==self.registro and self.registro==self.motor.registro and i.registro== self.motor.registro):
                    return "Auto original"
            else:
                return "Las piezas no son originales"          
            return "Las piezas no son originales"


               
             