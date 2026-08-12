from api import get_crypto

def showMenu():
    while True:
        menu = input("Welcome to CWP Cryptocurrency Tracker! To search press S , to exit or Quit Press E")
    while (

    )
    if menu == "S":
        response = input("Please type in the crptoId")
        print(get_crypto(response))
    
    elif menu == "E":
        print("Goodbye dear client")
    else:
        print("Invalid choice")

    


showMenu()
    