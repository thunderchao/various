import os, datetime, webbrowser
import colorama
from colorama import Fore, Style

os.system("mode con cols=81 lines=60")

colorama.init()

header = """
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
            Supreme Python Library Organizer Deluxe Edition (SPLODE)\n
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"""

def libload():
    if os.path.exists(".booklib.txt"):
        with open(".booklib.txt", "r") as bf:
            booklib = [line.strip() for line in bf]
            booklib.sort()
            global booklib
    else:
        booklib = []
        global booklib
    if os.path.exists(".movielib.txt"):
        with open(".movielib.txt", "r") as mf:
            movielib = [line.strip() for line in mf]
            movielib.sort()
            global movielib
    else:
        movielib = []
        global movielib
        
def startup():
    libload()
    os.system("cls")
    print(Fore.GREEN + Style.BRIGHT + header)
    topmenu = "\t1. View Contents\n\t2. Add an Item\n\t3. Exit"
    print("Select an option\n" + topmenu)
    select = input("\n\t# ")
    if select == "1":
        viewlib()
    elif select == "2":
        addstart()
    elif select == "3":
        print(Style.RESET_ALL)
        os.system("mode con cols=80 lines=25")
        quit
    else:
        input("\nTry again. Hit enter.")
        startup()

def viewlib():
    os.system("cls")
    print(header + "\nView the Library\n")
    date = datetime.datetime.now()
    stamp = date.strftime("%Y%m%d-%H%M")
    fname = "Library-" + stamp + ".txt"
    f = open(fname, 'w')
    f.write("Books:\n")
    for item in booklib:
        f.write("%s\n" % item)
    f.write("\nMovies:\n")
    for item in movielib:
        f.write("%s\n" % item)
    f.close()
    print("File " + Fore.CYAN + Style.BRIGHT + fname + Fore.GREEN + Style.BRIGHT + " created.")
    webbrowser.open(fname)
    input("Press enter to return.")
    startup()

def addstart():
    os.system("cls")
    print(header + "\nAdd an Item\n\t1. Book\n\t2. Movie\n")
    addsel = input("\t# ")
    if addsel == "1":
        addbook()
    elif addsel == "2":
        addmovie()
    else:
        startup()
    
def addbook():
    os.system("cls")
    print(header + "\nAdd a Book\n")
    bauthor = input("Author's Name (Last, First):\n\t")
    btitle = input("Book Title:\n\t")
    byear = input("Year Published:\n\t")
    addb = [bauthor, btitle, byear]
    booklib.append(addb)
    with open(".booklib.txt", "w") as ab:
        for item in booklib:
            ab.write("%s\n" % item)
    print("\nAdded \"" + Fore.CYAN + Style.BRIGHT + btitle + Fore.GREEN + Style.BRIGHT + "\" to the library")
    input("Press enter to go back")
    startup()

def addmovie():
    os.system("cls")
    print(header + "\nAdd a Movie\n")
    mtitle = input("Movie Title:\n\t")
    myear = input("Year Released:\n\t")
    addm = [mtitle, myear]
    movielib.append(addm)
    with open(".movielib.txt", "w") as am:
        for item in movielib:
            am.write("%s\n" % item)
    print("\nAdded \"" + Fore.CYAN + Style.BRIGHT + mtitle + Fore.GREEN + Style.BRIGHT + "\" to the library")
    input("Press enter to go back")
    startup()

startup()
