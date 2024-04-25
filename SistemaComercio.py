import Productos as pr

lista=[]
lista.append(pr.Producto("tomate", 24.3, "almacén"))
lista.append(pr.Producto("manzana", 90, "frutas"))
lista.append(pr.Producto("pritty", 56, "bebidas"))

lista.append(pr.Bebida("teem", 33, 2))

# for pro in lista:
#     print(pro)

print(lista[3].categoria)
print(lista[3].capacidad) #Sabe algo más, sabe hacer algo más. Bebida es un Producto pero con algunos atributos y métodos adicionales
print(lista[3].valorPorLitro())
print(lista[3].iva)
# print(lista[2].capacidad)
# print(lista[2].valorPorLitro())

lista.append(pr.Electronico("monitor", 56000))
print(lista[4].vf())

print("Ahora viene la lista con productos de subclases")
for pro in lista:
    print(pro)

