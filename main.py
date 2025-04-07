import csv
import os

def leer_transacciones(ruta_archivo):
    # Paso 1: Validar si el archivo existe
    if not os.path.isfile(ruta_archivo):
        print(f"El archivo '{ruta_archivo}' no existe.")
        return None

    # Continuamos creando la estructura donde almacenaremos la data del archivo CSV
    transacciones = []
    # Dentro de un Try-Cath procederemos a controlar cualquier error de lectura, de formato u otro del archivo
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Convertimos el monto a número y agregamos a la lista
                try:
                    fila["monto"] = float(fila["monto"])
                    transacciones.append(fila)
                except ValueError:
                    print(f"Monto inválido en la transacción ID {fila['id']}. Se omitirá.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

    # Validar si hay al menos una transacción
    if len(transacciones) == 0:
        print("No hay transacciones válidas en el archivo.")
        return None

    return transacciones

# Función para calcular el Balance de los datos registrados
def calcular_balance(transacciones):
    balance = 0.0

    for t in transacciones:
        if t["tipo"] == "Crédito":
            balance += t["monto"]
        elif t["tipo"] == "Débito":
            balance -= t["monto"]

    return balance

# Función para encontrar la transaccion mayor de los datos registrados
def encontrar_transaccion_mayor(transacciones):
    mayor_monto = 0.0
    id_mayor = None

    for t in transacciones:
        if t["monto"] > mayor_monto:
            mayor_monto = t["monto"]
            id_mayor = t["id"]

    return id_mayor, mayor_monto

# Función para contar las transacciones según el tipo de los datos registrados
def contar_transacciones_por_tipo(transacciones):
    contador_credito = 0
    contador_debito = 0

    for t in transacciones:
        if t["tipo"] == "Crédito":
            contador_credito += 1
        elif t["tipo"] == "Débito":
            contador_debito += 1

    return contador_credito, contador_debito



# Método main del programa     
if __name__ == "__main__":
    archivo = "data.csv"
    transacciones = leer_transacciones(archivo)

    if transacciones:
        balance = calcular_balance(transacciones)
        id_mayor, monto_mayor = encontrar_transaccion_mayor(transacciones)
        creditos, debitos = contar_transacciones_por_tipo(transacciones)
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance:.2f}")
        print(f"Transacción de Mayor Monto: ID {id_mayor} - {monto_mayor:.2f}")
        print(f"Conteo de Transacciones: Crédito: {creditos} Débito: {debitos}")

