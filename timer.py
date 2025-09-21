import os
from time import sleep

def main() -> None:
    while True:
        print("----- Temporizador -----")
        seconds: int = get_int_number("Ingrese el tiempo a esperar: ")

        for i in range(seconds , 0, -1):
            print(i)
            sleep(1)
    
        print("\n¡Tiempo terminado!\n")

        if stop_app():
            break

def get_int_number(message: str = '') -> int:
    while True:
        try:
            value: int = int(input(message))
            if value <= 0:
                print("Ingrese un numero mayor a 0\n")
                continue
            return value

        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

def stop_app() -> bool:
    while True:
        print("\n--------------------------------------------------------")
        response = input("quieres seguir utilizando la aplicacion? ('y' o 'n'): ").strip().lower()
        if response == 'n':
            return True
        elif response == 'y':
            clear_terminal()
            return False
        else:
            print("Por favor ingrese 'y' o 'n'.\n")

def clear_terminal() -> None:
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
print("hello world")