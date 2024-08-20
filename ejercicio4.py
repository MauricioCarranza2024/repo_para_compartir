# Clase Instrumento
class Instrumento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def tocar(self):
        print(f"Estás tocando el {self.nombre}.")

# Clase intermedia Cuerda, que hereda de Instrumento
class Cuerda(Instrumento):
    def __init__(self, nombre, numero_cuerdas):
        super().__init__(nombre, tipo="cuerda")
        self.numero_cuerdas = numero_cuerdas
    
    def afinar(self):
        print(f"Afinando el {self.nombre} con {self.numero_cuerdas} cuerdas.")

# Clase derivada Guitarra, que hereda de Cuerda
class Guitarra(Cuerda):
    def __init__(self, nombre, numero_cuerdas, tipo_guitarra):
        super().__init__(nombre, numero_cuerdas)
        self.tipo_guitarra = tipo_guitarra
    
    def tocar_acorde(self, acorde):
        print(f"Tocando el acorde {acorde} en la guitarra {self.tipo_guitarra}.")

# Ejemplo de uso
mi_guitarra = Guitarra(nombre="Guitarra Acústica", numero_cuerdas=6, tipo_guitarra="acústica")
mi_guitarra.tocar()           
mi_guitarra.afinar()          
mi_guitarra.tocar_acorde("Do Mayor")  
