import string
from random import shuffle, choice

# Declaracion de Carecteres a Usar
numbers: list[str] = list(string.digits)
punctuation: list[str] = list(string.punctuation)
low_case: list[str] = list(string.ascii_lowercase)
up_case: list[str] = list(string.ascii_uppercase)

# Las Listas de Caracteres a usar se desordenaran
shuffle(numbers)
shuffle(punctuation)
shuffle(low_case)
shuffle(up_case)

def main() -> None:
    print("----- Generador de Contrasenas -----")
    pass_lenght: int = ingresar_largo_contrasena("Ingrese cual sera el tamano de su contrasena: ")
    
    raw_password: list[str] = []
    # Creacion de Contrasena
    for i in range(round(pass_lenght * (30 / 100))):
        raw_password.append(choice(numbers))
        raw_password.append(choice(punctuation))
        shuffle(raw_password)

    for i in range(round(pass_lenght * (20 / 100))):
        raw_password.append(choice(low_case))
        raw_password.append(choice(up_case))
        shuffle(raw_password)

    if len(raw_password) > pass_lenght:
        raw_password.pop()

    password: str = "".join(raw_password)

    print("\n----- Contrasena Exitosamente Generada -----")
    print(password)
def ingresar_largo_contrasena(texto: str) -> int:
    while True:
        try:
            valor: int = int(input(texto))
            if valor <= 8:
                print("\n----- PROGRAM ERROR -----")
                print(f"El tamano de su contrasena debe de ser mayor de 8 caracteres.\n")
            else:
                return valor

        except ValueError as e:
            print("\n----- PROGRAM ERROR -----")
            print(f"Entrada inválida. {e}\n")

if __name__ == "__main__":
    main()