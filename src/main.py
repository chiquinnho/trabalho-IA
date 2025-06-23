from ui.gui import NPuzzleGUI
from ui.cli import NPuzzleCLI

def main():
    # Initialize the user interface
    choice = input("Choose interface (1 for GUI, 2 for CLI): ")
    
    if choice == '1':
        app = NPuzzleGUI()
        app.run()
    elif choice == '2':
        cli = NPuzzleCLI()
        cli.run()
    else:
        print("Invalid choice. Please select 1 for GUI or 2 for CLI.")

if __name__ == "__main__":
    main()