class Producto():
    def __init__(self, nombre, precio, categoria, iva=21):
        self.__nombre=nombre
        self.__precio=precio
        self.__categoria=categoria
        self.__iva=iva
        

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre=valor
    
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio=valor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        self.__categoria=valor

    @property
    def iva(self):
        return self.__iva

    @iva.setter
    def iva(self, valor):
        self.__iva=valor
    
    def aumento(self, incremento):
        self.precio=self.precio+self.precio*incremento/100

    def vf(self):
        return self.precio+self.precio*self.iva/100

    def __str__(self): #Me permite definir una conversión a string del objeto
        return f"Producto: {self.nombre} - Categoría: {self.categoria} - Precio: {self.precio} - IVA: {self.iva}"


class Bebida(Producto):
    def __init__(self, nombre, precio, capacidad=1): #Sobreescribo un método de mi clase padre
        super().__init__(nombre, precio, "bebidas")
        self.__capacidad=capacidad
        

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):
        self.__capacidad=valor
    
    def valorPorLitro(self):
        return self.precio/self.capacidad

    def __str__(self): #Sobreescribo la clase de mi padre
        return super().__str__()+f" - Capacidad: {self.capacidad}"

class Electronico(Producto):
    def __init__(self, nombre, precio, iva=10.5):
        super().__init__(nombre, precio, "electronicos", iva)
    
