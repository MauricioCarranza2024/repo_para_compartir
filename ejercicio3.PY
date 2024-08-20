# Clase  Película
class Pelicula:
    def __init__(self, titulo, director, duracion):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion
    
    def reproducir(self):
        print(f"Reproduciendo la película {self.titulo} dirigida por {self.director}.")

# Clase intermedia Humor, que hereda de Película
class Humor(Pelicula):
    def __init__(self, titulo, director, duracion, tipo_humor):
        super().__init__(titulo, director, duracion)
        self.tipo_humor = tipo_humor
    
    def describir_humor(self):
        print(f"{self.titulo} es una película de humor {self.tipo_humor}.")

# Clase derivada Colombiana, que hereda de Humor
class Colombiana(Humor):
    def __init__(self, titulo, director, duracion, tipo_humor, ambientacion):
        super().__init__(titulo, director, duracion, tipo_humor)
        self.ambientacion = ambientacion
    
    def describir_ambientacion(self):
        print(f"{self.titulo} está ambientada en {self.ambientacion} en Colombia.")

# Ejemplo de uso
mi_pelicula = Colombiana(titulo="El Paseo", director="Harold Trompetero", duracion="90 minutos", tipo_humor="familiar", ambientacion="vacaciones en la costa")
mi_pelicula.reproducir()             
mi_pelicula.describir_humor()        
mi_pelicula.describir_ambientacion() 
