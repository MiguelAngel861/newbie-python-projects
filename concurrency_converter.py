import os

currencies: dict[str, float] = {
    "USD": 1,
    "NIO": 36.81
}

def main() -> None:
    while True:
        print("----- Convertidor de Moneda -----")
        print(f"Monedas disponibles: {', '.join(key for key in currencies.keys())}")

        print("\n----- Seleccion de Moneda -----")
        from_currency: str = ingresar_opcion("Ingrese la moneda a convertir: ")
        to_currency: str = ingresar_opcion("Ingrese la moneda a la que sera convertida: ")
        amount: float = ingresar_valor_flotante("Cual es la cantidad de dinero que desea convertir? ")
        converted_amount = convertir_moneda(from_currency, to_currency, amount)

        print("\n----- Resultado de Conversion -----")
        print(f"{amount:.2f} {from_currency}  =  {converted_amount:.2f} {to_currency}")

        if detener_app():
            break

def ingresar_opcion(message: str = "") -> str:
    while True:
            option: str = input(message).strip().upper()
            if option not in currencies:
                print(f"\nPor favor ingrese una opcion valida.")
                continue
            return option

def ingresar_valor_flotante(message: str = "") -> float:
    while True:
        try:
            value: float = float(input(message))
            if value <= 0:
                print("Por favor ingrese un valor mayor que 0.")
                continue
            return value

        except ValueError as e:
            print("\n----- PROGRAM ERROR -----")
            print(f"Entrada inválida. {e}")

def convertir_moneda(from_currency: str, to_currency: str, amount: float) -> float:
    if from_currency == to_currency:
        return amount
    usd_amount = amount / currencies[from_currency]

    return usd_amount * currencies[to_currency]

def detener_app() -> bool:
    while True:
        response = input("quieres seguir utilizando la aplicacion? ('y' o 'n'): ").strip().lower()
        if response.lower() == 'n':
            return True
        elif response.lower() == 'y':
            clear_terminal()
            return False
        else:
            print("Por favor ingrese 'y' o 'n'.\n")

def clear_terminal() -> None:
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()