def main() -> None:
    print("----- Conversor de Unidades Metricas -----")
    print("A que unidad desea convertir?")
    print("01 - milimetros a centimetros")
    print("02 - centimetros a metros")
    print("03 - metros a kilometros")
    opcion_menu: int = ingresar_opcion(1, 4)

    print("\n----- Valor a Convertir -----")
    valor_convertir: float = ingresar_valor_flotante("Ingrese el valor a convertir: ")

    if opcion_menu == 1:
        resultado: float = valor_convertir / 100
        print("\n----- Resultado de la Convercion -----")
        print(f"El valor de la conversion de {valor_convertir:.2f}mm a centimetros es igual a: {resultado:.2f}cm")
    
    if opcion_menu == 2:
        resultado: float = valor_convertir / 100
        print("\n----- Resultado de la Convercion -----")
        print(f"El valor de la conversion de {valor_convertir:.2f}cm a centimetros es igual a: {resultado:.2f}m")

    if opcion_menu == 3:
        resultado: float = valor_convertir / 1000
        print("\n----- Resultado de la Convercion -----")
        print(f"El valor de la conversion de {valor_convertir:.2f}m a centimetros es igual a: {resultado:.3f}km")


def ingresar_valor_flotante(mensaje: str = "") -> float:
    while True:
        try:
            valor: float = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("\n----- PROGRAM ERROR -----")
                print("Por favor ingrese un un numero mayor a 0\n")

        except ValueError as e:
            print("\n----- PROGRAM ERROR -----")
            print(f"Entrada inválida. {e}")

def ingresar_opcion(valor_minimo: int, valor_maximo: int) -> int:
    while True:
        try:
            opcion: int = int(input("Opcion numero: "))
            if opcion < valor_minimo or opcion > valor_maximo:
                print("\n----- PROGRAM ERROR -----")
                print(f"Por favor ingrese un número entre {valor_minimo} y {valor_maximo}.")
            else:
                return opcion

        except ValueError as e:
            print("\n----- PROGRAM ERROR -----")
            print(f"Entrada inválida. {e}")

        print("\nA que unidad desea convertir?")

if __name__ == "__main__":
    main()
