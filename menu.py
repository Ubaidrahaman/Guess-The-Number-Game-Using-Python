#Imports
import os

#Variables
game_running = True

#function
def clear_screen(): os.system("cls" if os.name == "nt" else "clear")
def show_menu():
            print("""               ==============================
                        Wellcome to Geuss the number
                        Press 1 to start the game
                        Press 2 for Help
                        Press 3 to quit                       
                        ==============================""")
            

#Menu display
show_menu()
while game_running == True:
    user_choice = input()
    if user_choice == "1":
            print("Sure Let's Play")
        

    elif user_choice == "2":
            clear_screen()
            print("HELP".title())
            print("""In this game I will think a number and you have to guess it correctly
                You will have 5 attempts to guess the Number 
                Enjoy """)
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("Press enter to Go Back.")
            input()
            clear_screen()
            show_menu()
    elif user_choice == "3":
            print("Thanks for playing")
            game_running = False

