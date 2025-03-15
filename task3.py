import sys
from pathlib import Path
from colorama import Fore, Style, init 

init(autoreset=True)

def visualize_directory(directory: Path, indent = 0):
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + Style.BRIGHT + f"Path: '{directory}' doesn't exist.")
        return
    

    if indent == 0:
        print(Fore.GREEN + Style.BRIGHT  + f"📦 {directory.name}/")

    for item in directory.iterdir():

        if item.is_dir():
            print(" " * (indent + 2) + Fore.BLUE + Style.BRIGHT + f"📁 {item.name}/")
            visualize_directory(item, indent + 2)
        else:
            print(" " * (indent + 2) + Fore.CYAN + Style.BRIGHT + f"📜 {item.name}")
 
def main():
    if len(sys.argv) != 2:
        print(Fore.RED + Style.BRIGHT + "Please provide directory path")
        sys.exit(1)

    directory_path = sys.argv[1]
    directory = Path(directory_path)

    visualize_directory(directory)

if __name__ == "__main__":
    main()




