def main() -> None:
    print("----- Calculadora -----")
    print("Elija una de las siguientes de las opciones a ejecutar.")
    print("1 - Suma de Valores")
    print("2 - Resta de Valores")
    print("3 - Multiplicacion de Valores")
    print("4 - Division de Valores")
    opcion_menu: int = ingresar_opcion(1, 4)

    print("\n----- Valores a Utilizar -----")
    primer_numero: float = ingresar_valor_flotante("Ahora Ingrese el primer numero de la operacion a ejecutar: ")
    segundo_numero: float = ingresar_valor_flotante("Ahora Ingrese el segundo numero de la operacion a ejecutar: ")

    if opcion_menu == 1:
        print("\n----- Resultado de la Operacion -----")
        resultado: float = primer_numero + segundo_numero
        print(f"El valor de la operacion: {primer_numero:.2f} + {segundo_numero:.2f} = {resultado:.2f}")

    elif opcion_menu == 2:
        print("\n----- Resultado de la Operacion -----")
        resultado: float = primer_numero - segundo_numero
        print(f"El valor de la operacion: {primer_numero:.2f} - {segundo_numero:.2f} = {resultado:.2f}")

    elif opcion_menu == 3:
        print("\n----- Resultado de la Operacion -----")
        resultado: float = primer_numero * segundo_numero
        print(f"El valor de la operacion: {primer_numero:.2f} * {segundo_numero:.2f} = {resultado:.2f}")

    elif opcion_menu == 4:
        print("\n----- Resultado de la Operacion -----")
        resultado: float = primer_numero / segundo_numero
        print(f"El valor de la operacion: {primer_numero:.2f} ÷ {segundo_numero:.2f} = {resultado:.2f}")

def ingresar_opcion(valor_minimo: int, valor_maximo: int) -> int:
    while True:
        try:
            opcion: int = int(input("Opcion numero: "))
            if opcion < valor_minimo or opcion > valor_maximo:
                print(f"\nPor favor ingrese un número entre {valor_minimo} y {valor_maximo}.")
            else:
                return opcion

        except ValueError as e:
            print("\n----- PROGRAM ERROR -----")
            print(f"Entrada inválida. {e}")

def ingresar_valor_flotante(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))

        except ValueError as e:
            print("\n----- PROGRAM ERROR -----")
            print(f"Entrada inválida. {e}")

if __name__ == "__main__":
    while(True):
        main()
        print("\n-----------------------------------------------")
        respuesta = input("quieres seguir utilizando la aplicacion? ('y' o 'n'): ")
        if respuesta.lower() == 'n':
            break
        print()