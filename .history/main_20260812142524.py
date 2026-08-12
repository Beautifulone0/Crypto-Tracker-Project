from api import get_crypto


def showMenu():
    while True:
        menu = input(
            "Welcome to CWP Cryptocurrency Tracker! "
            "To search press S, to exit or Quit press E: "
        )

        if menu == "S":
            response = input("Please type in the crypto ID: ")
            print(get_crypto(response))

        elif menu == "E":
            print("Goodbye dear client")
            break

        else:
            print("Invalid choice")


showMenu()