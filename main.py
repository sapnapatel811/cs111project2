# Dictionaries
main_menu = {
    "A": "(A)bout the game.",
    "P": "(P)lay Chicago Explorers!",
    "D": "(D)isplay game stats.",
    "Q": "(Q)uit."
}
# a dictionary that defines the relationships/connections between locations
locations_map = {
    'shedd aquarium': ['field museum', 'mccormick place'], 
    'mccormick place': ['shedd aquarium', 'museum of science and industry'], 
    'museum of science and industry': ['mccormick place'], 
    'uic': ['field museum'],
    'field museum': ['uic', 'shedd aquarium', 'art institute'],
    'art institute': ['millennium park', 'willis tower', 'river walk', 'field museum'],
    'willis tower': ['art institute'],
    'millennium park': ['art institute'],
    'navy pier': ['river walk'],
    'river walk': ['art institute', 'navy pier']
}
# dictionary of inspirations - maps location -> message that should be printed
inspirations = {
    'museum of science and industry': 'Surrounded by the inventions of others, you begin to draft new displays of innovation to inspire others', 
    'art institute': 'The sculptures within the Art Institute remind you of the intricate stonework in Chicago, you wonder about how you can incorporate this into your project.', 
    'willis tower': 'The towering might of this iconic skyscraper has given you new ideas on how to create a new, soaring masterpiece to add to the Chicago skyline.'
}

# String variables that contain output text you print at various points (so you don't have to guess)
welcome_msg = '--- WELCOME TO CHICAGO EXPLORERS ---\n'
about_msg =  'ABOUT THE GAME:\nYou and your party have been asked to come up with Chicago\'s next great landmark!\nTo begin your creative journey, you have all decided to visit the city to find inspiration.\nTravel the city until all the insprirations have been found then get back to UIC as fast as possible.'
line = ("----------------------------------\n")
last_inpiration_msg = "YOU FOUND THE LAST INSPIRATION!!!\nNow get back to UIC!"
win_msg = line +"|   Congrats - You Won the Game.    |\n|   (Checkout your game stats)      |\n"+line

# Lists for logging locations and inspirations
found_inspirations = []         # keep a list of inspiration locations visited
location_log = []               # keep a log of all locations visited

# Variable setup - suggested variables for holding game state -- you will need to make more as part of the project
menu_choice = ""                # string to hold current main menu choice
current_loc = 'uic'             # string to hold the current location (game starts at uic)

# Your code starts below
#This is the app Chicago Explorers coded by Sapna Patel for CS111 @UIC on 10/13/24
#This app allows user to navigate toursit landmarks in the city of Chicago. The game has a main menu that shows the options to learn about the game, play the game, quit, or view the statistics of the game. Gameplay involves traveling to locations and finding specific inspirations. Once all inspirations are found, then the player will return to the starting location to end the game and win. 
#Begin the main game loop (milestone 1)
print(welcome_msg)
continue_main_loop = True

while continue_main_loop:
    #Print the main menu options
    for value in main_menu.values():
        print("-", value)

    print("What is your choice? ", end="")
    user_choice = input()

    #validate user input
    while user_choice not in main_menu:
        user_choice = input("Invalid input. Please try again: ")

    print(f"\nYour choice: {main_menu[user_choice]}")
    print()

    #Quit option (milestone 1)
    if user_choice == "Q":
        continue_main_loop = False
        print("Goodbye!")
    
    #About game option (milestone 1)
    elif user_choice == "A":
        print(welcome_msg)
        print(about_msg)

    #Gameplay option (basic funtionality) (milestone 2)
    elif user_choice == "P":
        gameplay = True
        
        while gameplay: 
            location_log.append(current_loc) #Add current location to log
            print(line)
            print(f"You are currently at {current_loc}.")

            #checks current location if inspiration found (milestone 3)
            if current_loc in inspirations and current_loc not in found_inspirations: #m3 task 1
                print()
                print(line)
                print("Congrats! You found an inspiration!")
                print(inspirations[current_loc])
                found_inspirations.append(current_loc) #add inspiration to end of inspiration log (m3 task 2)
                print()
                if len(found_inspirations) == len(inspirations): #check if 3 inspirations found (m3 task 4)
                    print(last_inpiration_msg) #m3 task 3
                print("----------------------------------")

            #print locations to move on to
            print("\nWhere would you like to go next?\n")
            for location in locations_map[current_loc]:
                print("-", location)
            print("- (return) to main menu)")
 
            next_loc = input("Enter next location (or 'return'): ")

            #validate input for next location
            while next_loc != "return" and next_loc not in locations_map[current_loc]:
                print("Try again: ",end="")
                next_loc = input()
            
            #check if user won game after finding all inspirations if returned to uic 
            if(len(found_inspirations) == len(inspirations) and next_loc == 'uic'):
                print(win_msg)
                current_loc = next_loc
                break
            elif next_loc == "return":
                break
            else:
                current_loc = next_loc

    #Display game stats option (milestone 4)
    elif user_choice == "D":
        print(line)
        print("GAME STATS:\n")
        print(f"Location visit log: {len(location_log)} total hops")
        print(f"Locations: {location_log}\n")
        print(f"Unique Locations Visited: {len(set(location_log))}")
        print(f"Locations: {set(location_log)}\n")
        print(f"Inspirations found: {len(found_inspirations)}")
        for i in found_inspirations:
            print("-", i)
        print(line)
    #THE END :)))