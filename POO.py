class Animal:
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"
    

mi_perro = Perro("Bethoven", 4)
print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.patas} patas. Los perros hacen {mi_perro.hacer_sonido()}")