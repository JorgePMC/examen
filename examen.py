def mostrar_stock(stock):
    for x, y in stock.items():
        print(x, y)

def stock_marca(mar):
    mar=(input("Que marca desea consultar?: "))

def val_marca(x):
    while True:
        for x in productos.items():
            if x == ['HP'] or ['lenovo'] or ['Asus'] or ['Dell']:
                return

def limite_precio(articulo):
    while True:
        pre_minimo=int(input("Ingrese el precio minimo para la busqueda"))
        pre_maximo=int(input("Ingrese el precio maximo para la busqueda"))
        for articulo in stock.items():
            if articulo >= pre_minimo and articulo <= pre_maximo:
                print("estos son los articulos que estan en el los parametros solicitados")
                print()
            else:
                print("No hay notebooks en ese rango de precio")
def dispo_stock(articulo):
    while True:
        g

def actualizar_precio(stock):
    while True:
        y=str(input("Ingrese modelo a actualizar: "))
        for x in stock.items():
            if y == stock[any]:
                new=int(print("Ingrese el nuevo precio: "))
                stock[x][0]=new
                print("Precio actualizado!!!")

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
mostrar_stock(stock)
while True:
    try:
        print("""
*** MENU PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Actualizar precio.
4. Salir.
              """)
        op=int(input())
        match op:
            case 1:
                stock_marca(productos)
            case 2:
                a
            case 3:
                actualizar_precio(stock)
            case 4:
                break
            case _:
                print("Escoja solo las opciones disponibles!")
    except Exception as errol:
        print("El error es:", errol)