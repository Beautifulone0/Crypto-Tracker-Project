from api import get_crypto


def display_crypto(crypto):
    """Display cryptocurrency information in a readable format."""
    if crypto is None:
        print("\nCryptocurrency not found. Please check the crypto ID and try again.")
        return

    print("\n========== Cryptocurrency Information ==========")
    print(f"Name: {crypto['name']}")
    print(f"Symbol: {crypto['symbol'].upper()}")
    print(f"Current Price: ${crypto['price']}")
    print(f"Market Cap: ${crypto['market Cap']}")
    print(f"24h Change: {crypto['24h change']}%")
    print("===============================================\n")


def search_crypto():
    """Ask the user for a cryptocurrency ID and display its information."""
    crypto_id = input("Please enter the cryptocurrency ID: ").strip().lower()

    if not crypto_id:
        print("Crypto ID cannot be empty.")
        return

    crypto = get_crypto(crypto_id)
    display_crypto(crypto)


def show_menu():
    """Display the main menu and handle user interaction."""
    while True:
        print("\n======================================")
        print("     CWP Cryptocurrency Tracker")
        print("======================================")
        print("S - Search cryptocurrency")
        print("E - Exit")

        menu = input("Please choose an option: ").strip().upper()

        if menu == "S":
            search_crypto()

        elif menu == "E":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter S to search or E to exit.")


show_menu()