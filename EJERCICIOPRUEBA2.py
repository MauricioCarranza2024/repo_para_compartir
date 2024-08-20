# Clase Libro
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def leer(self):
        print(f"Estás leyendo {self.titulo} de {self.autor}.")

# Clase Novela, que hereda de Libro
class Novela(Libro):
    def __init__(self, titulo, autor, paginas, genero):
        super().__init__(titulo, autor, paginas)
        self.genero = genero
    
    def describir(self):
        print(f"{self.titulo} es una novela de género {self.genero}.")

# Clase Romántica, que hereda de Novela
class Romantica(Novela):
    def __init__(self, titulo, autor, paginas, genero, protagonista):
        super().__init__(titulo, autor, paginas, genero)
        self.protagonista = protagonista
    
    def mostrar_protagonista(self):
        print(f"El protagonista de {self.titulo} es {self.protagonista}.")

# Ejemplo de uso
mi_libro = Romantica(titulo="Orgullo y Prejuicio", autor="Jane Austen", paginas=432, genero="Romántico", protagonista="Elizabeth Bennet")
mi_libro.leer()               
mi_libro.describir()          
mi_libro.mostrar_protagonista()  
