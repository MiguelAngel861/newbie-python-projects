import os
from random import randint

def main() -> None:
    while True:
        print("----- Simulador de Dados -----")
        veces_a_lanzar: int = ingresar_valor_entero("Cuantas veces quieres lanzar los dados? ")

        resultados: list[int] = []
        for _ in range(veces_a_lanzar):
            resultado: int = randint(1, 6)
            resultados.append(resultado)

        print(f"Resultados totales: {resultados}\n")
        print("-------------------------------------------")
        if input("quieres volver a lanzarlos? ('y' o 'n'): ").lower() == "n":
            break
        else:
            resultados = []
            clear_terminal()

def ingresar_valor_entero(mensaje: str) -> int:
    while True:
        try:
            valor: int = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Por favor ingrese un un numero mayor a 0\n")

        except ValueError as e:
            print("\n----- PROGRAM ERROR -----")
            print(f"Entrada inválida. {e}")

def clear_terminal() -> None:
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

if __name__ == "__main__":
    main()