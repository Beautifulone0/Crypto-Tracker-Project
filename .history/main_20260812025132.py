from api import get_crypto

def showMenu():
    menu = input("Welcome to CWP Cryptocurrency Tracker! To search press S , to exit or Quit Press E")
    if menu == "S":
        response = input("Please type in the crptoId")
        print(response)
    elif menu == "E":
        print
    else:
        print("Please exit")

    


showMenu()
    