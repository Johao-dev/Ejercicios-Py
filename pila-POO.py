class lista:
    def __init__(self):
        self.__pila = []
    
    def push(self, valor):
        self.__pila.append(valor)

    def pop(self):
        valor = self.__pila[-1]
        del self.__pila[-1]
        return valor
    
class sumar_listas(lista):
    def __init__(self):
        lista.__init__(self)
        self.__sumar = 0

    def enviar_suma(self):
        return self.__sumar

    def push(self, valor):
        self.__sumar += valor
        lista.push(self, valor)

    def pop(self):
        valor = lista.pop(self)
        self.__sumar -= valor
        return valor

objeto_prueba = sumar_listas()

for i in range(4):
    objeto_prueba.push(i)
print(objeto_prueba.enviar_suma())

for i in range(4):
    print(objeto_prueba.pop())