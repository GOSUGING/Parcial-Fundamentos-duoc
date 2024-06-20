def registrar_pedido(clientes):
    nombre = input("Ingressa el nombre del cliente: ")
    apellido = input("Ingresa el apellido del cliente: ")
    direccion = input("Ingrese direccion del cliente: ")
    sector = input("Ingrese sector del cliente: ")
    if not nombre or not apellido or not direccion:
        print("Error, todos los campos deben ser llenados")
        return
    try:
        pequeno = int(input("Ingrese cantidad de paquetes pequeños que desea enviar: "))
        mediano = int(input("Ingrese cantidad de paquetes mediano que desea enviar: "))
        grande = int(input("Ingrese cantidad de paquetes grande que desea enviar: "))
    except ValueError as error_pedido:
        print("Error: cantidad debe ser un numero entero")

    pedido = {
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "sector": sector,
        "Paq. pequeño": pequeno,
        "Paq. mediano": mediano,
        "Paq. grande": grande
    }

    clientes.append(pedido)

def listar_pedidos(clientes):
    if not clientes:
        print("Error: no hay clientes registrados")
        return
    for pedido in clientes:
        print(f"Nombre {pedido['nombre']}, Apellido: {pedido['apellido']}, Direccion: {pedido['direccion']},Sector: {pedido['sector']}, Paq. pequeño: {pedido['Paq. pequeño']}, Paq. mediano: {pedido['Paq. mediano']}, Paq. grande: {pedido['Paq. grande']}")

def imprimir_hoja_ruta(clientes):
    if not clientes:
        print("Error: no hay clientes registrados")
        return
    ruta_por_sector = []
    for pedido in clientes:
        sector = pedido["sector"]
        if sector not in ruta_por_sector:
            ruta_por_sector[sector]=[]
        ruta_por_sector[sector].append(pedido)
    
    
    with open("hoja_de_ruta.txt", "w") as archivo:
        for sector, pedidos in ruta_por_sector.items():
            archivo.write(f"Sector: {sector}\n")
            for pedido in pedidos:
                archivo.write(f"Nombre {pedido['nombre']}, Apellido: {pedido['apellido']}, Direccion: {pedido['direccion']},Sector: {pedido['sector']}, Paq. pequeño: {pedido['Paq. pequeño']}, Paq. mediano: {pedido['Paq. mediano']}, Paq. grande: {pedido['Paq. grande']}")   
    print("Hoja de ruta generada exitosamnete en 'hoja_de_ruta.txt'.")
def main():
    clientes = []

    while True:
        print("Menu")
        print("1. Registrar pedido")
        print("2. Listar pedidos")
        print("3. Imprimir Hoja de ruta")
        print("4. Salir")
        try:
            opcion = int(input("Ingrese la opcion que desea: "))

            if opcion == 1:
                registrar_pedido(clientes)
            elif opcion == 2:
                listar_pedidos(clientes)
            elif opcion == 3:
                imprimir_hoja_ruta(clientes)
            elif opcion == 4:
                print("Estas saliendo del programa")
                break

        except ValueError as error_opcion_menu:
            print("Ingresar opcion entre 1 y 4.")

if __name__ == "__main__":
    main()                            