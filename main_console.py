from stegano import lsb
from colorama import *
print(Fore.GREEN+"TikTok:")
print('''
██╗░░░██╗███████╗██████╗░██╗░█████╗░░█████╗░███╗░░██╗███████╗░█████╗░░█████╗░
██║░░░██║██╔════╝██╔══██╗██║██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██╔══██╗
╚██╗░██╔╝█████╗░░██████╔╝██║██║░░╚═╝██║░░██║██╔██╗██║██████╗░██║░░██║╚██████║
░╚████╔╝░██╔══╝░░██╔══██╗██║██║░░██╗██║░░██║██║╚████║╚════██╗██║░░██║░╚═══██║
░░╚██╔╝░░███████╗██║░░██║██║╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚█████╔╝░█████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░░╚════╝░
''')
init()
while True:
    to_do=input("1-Read\n2-Write\n=> ")
    if "1" in to_do:
        path=input("Path to png file\n=> ").split(" ")[0]
        try:
            print(lsb.reveal(path))
        except:
            print("Error")
    if "2" in to_do:
        new_file_name=input("Entry new file name (with words,should end with .png)\n=> ")
        text_to_file=input("Entry text to write to file\n=> ")
        path_to_png=input("Entry path to picture(png)\n=> ")
        try:
            to_create = lsb.hide(path_to_png, text_to_file)
            to_create.save(new_file_name)
        except:
            print("Error")