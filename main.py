import requests
import os
import colorama
import sys
import time

from colorama import Fore,init,Style,Back
from readfile import start_read
def menu():
    clear()
    print(logo)
    print(f"(1) Modules")
    print(f"(2) Info\n")
    print(f"(x) Exit")
    option = input(" > ")
    if option == "1":
        modules()
    elif option == "2":
        info()
    elif option in ("x","X"):
        return
    else:
        modules()

def modules():
    clear()
    print(logo)
    if not os.path.exists("configs"):
        os.makedirs("configs")
    
    index_number = 1
    modules_list = ["empty"];modules_enum = enumerate(modules_list)
    
    found_modules = False
    for module in os.listdir("configs"):
        if module.split(".")[-1] == "json":
            found_modules = True
            print("({}) {}".format(index_number,module))
            modules_list.append(module)
            index_number+= 1
    if not found_modules:
        print("No configs found in /configs")
    print("\n(x) Back")
    option = input(" > ")
    try: option = int(option)
    except: 
        if option in ("x","X"): menu()
        else: modules()
    else:
        if option == 0: modules()
        else: 
            if found_modules:
                for index, item in modules_enum:
                    found = False
                    iteration = next(modules_enum)
                    index, item = iteration
                    if option == index:
                        found = True
                        break
                    if found == True:
                        break
                if found != True:
                    modules()
                else:
                    start_read(item)
            else:
                modules()

def info():
    clear()
    print(logo)
    print("This was created and developed by: MickeyYe#0001")
    print("Config files are found with the extention: .op")
    print("Config files should be in: /configs")
    input("Press enter to continue")
    menu()

if __name__ == "__main__":
    init(autoreset=True)
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    logo = Style.DIM+"""
            ________                      __________        
            \_____  \ ______   ____   ____\______   \___.__.
            /   |   \\____ \_/ __ \ /    \|     ___<   |  |
            /    |    \  |_> >  ___/|   |  \    |    \___  |
            \_______  /   __/ \___  >___|  /____|    / ____|
                    \/|__|        \/     \/          \/     
            """
    menu()