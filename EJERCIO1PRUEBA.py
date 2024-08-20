# Clase Mamífero
class Mamifero:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mover(self):
        print(f"{self.nombre} está moviéndose.")

    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Clase Doméstico, que hereda de Mamífero
class Domestico(Mamifero):
    def __init__(self, nombre, edad, dueño):
        super().__init__(nombre, edad)
        self.dueño = dueño
    
    def mostrar_dueño(self):
        print(f"El dueño de {self.nombre} es {self.dueño}.")

# Clase Perro, que hereda de Doméstico
class Perro(Domestico):
    def __init__(self, nombre, edad, dueño, raza):
        super().__init__(nombre, edad, dueño)
        self.raza = raza
    
    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

# Ejemplo de uso
mi_perro = Perro(nombre="Rex", edad=5, dueño="Juan", raza="Labrador")
mi_perro.mover()            
mi_perro.comer()            
mi_perro.mostrar_dueño()     
mi_perro.ladrar()           
