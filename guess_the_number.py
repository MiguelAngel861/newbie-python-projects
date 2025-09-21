import os, random

def main() -> None:
    while True:
        print("----- Adivina el Numero -----")
        print("En que numero estoy pensando? ")
        number = random.randint(1, 50)
        
        while True:
            guess = get_int("Ingrese un numero entre 1 y 50: ")
            if guess > 50 or guess < 1:
                print("El numero debe estar entre 1 y 50. Intente de nuevo.\n")
                continue

            if check_guess(number, guess):
                break

        if ask_to_continue():
            break

def check_guess(number: int, guess: int) -> bool:
    if guess < number:
        print("El numero es mayor. Intente de nuevo.\n")
        return False
    elif guess > number:
        print("El numero es menor. Intente de nuevo.\n")
        return False
    else:
        print(f"¡Felicidades! Adivinaste el numero {number}.\n")
        return True

def get_int(message: str = "") -> int:
    while True:
        try:
            value: int = int(input(message))
            if value <= 0:
                print("Por favor ingrese un valor mayor que 0.")
                continue
            return value

        except ValueError as e:
            print("\n----- PROGRAM ERROR -----")
            print(f"Entrada inválida. {e}")

def ask_to_continue() -> bool:
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