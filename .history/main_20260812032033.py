from api import get_crypto

def showMenu():
    menu = input("Welcome to CWP Cryptocurrency Tracker! To search press S ,R to retrieve market information,  to exit or Quit Press E")
    if menu == "S":
        response = input("Please type in the crptoId")
        print(get_crypto(response))
    elif menu == "R"
    elif menu == "E":
        print("Goodbye dear client")
    else:
        print("Invalid choice")

    


showMenu()
    