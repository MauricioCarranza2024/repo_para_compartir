class pelicula():
    def __init__(self):
        self.director = ""
        self.genero = ""
        self.anio = 0
        self.duracion = 0
        self.actores = []
        self.descripcion = ""

class humor():
    def __init__(self, director, genero, duracion, actores):
        self.pelicula = pelicula()
        self.pelicula.director = director
        self.pelicula.genero = genero
        self.pelicula.duracion = duracion
        self.pelicula.actores = actores
        self.pelicula.descripcion = "Pelicula de humor colombiana."

class Colombiana():
    def __init__(self):
        self.peliculas = []
        