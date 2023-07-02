from random import choice

def play_game():
    user_name = input("Enter player name: ")
    print(f"{user_name}, welcome to the text-based game Elemental_Clash!")
    print(f"""
    THE RULE OF GAME 
    
  The game is played by two players, you and computer.
  Each player starts with a certain number of life points  5.
  On each turn, the players choose one of the four elements: fire/f, water/w, earth/e, air/a.
  The element matchups follow the rule: fire beats earth, water beats fire , earth beats water, and air beats earth.
  If both players choose the same element, it results in a tie for that round.
  If fire  and air  or water and air  are matchup , it results in a tie, and no damage is dealt to either player.
  After each round, the CONGRATULATION YOU WIN deals damage to the opponent equal to the difference in life points.
  The game continues until one player's life points reach zero.
  At the end of the game, the player with remaining life points is declared the CONGRATULATION YOU WIN.
    
    """)
    
    user_live_points = 5
    computer_points = 5
    elements = {"fire": "F", "water": "W", "earth": "E", "air": "A"}
    
    while True:
        computer = choice(list(elements.keys()))
        user = input("\nEnter any one of these: 'Fire/f', 'Water/w', 'Earth/e', 'Air/a', or 'Q/q' or 'QUIT/quit' to end the game: ").lower()
        
        if user in ["q", "quit"]:
            print("Thanks for playing! The end.")
            break

        elif user not in elements.keys() and user not in [value.lower() for value in elements.values()]:
            print("INVALID INPUT")

        else:
            user_element = ""
            if user in elements.keys():
                user_element = user
            else:
                for key, value in elements.items():
                    if user == value.lower():
                        user_element = key
                        break

            if user_element == computer:
                print("It's a tie.")
            elif (user_element == "fire" and computer == "water") or (user_element == "water" and computer == "earth") or (user_element == "earth" and computer == "fire"):
                print("You lose.")
                user_live_points -= 1
                computer_points += 1
            elif (user_element == "fire" and computer == "earth") or (user_element == "water" and computer == "fire") or (user_element == "earth" and computer == "water") or (user_element == "air" and computer == "earth"):
                print("You win.")
                user_live_points += 1
                computer_points -= 1

            elif user_element == "air" and (computer == "fire" or computer == "water"):
                print("It's a tie.")

            updated_score = f"computer: {elements[computer]}\nuser: {elements[user_element]}\ncomputer score = {computer_points}\nyour score = {user_live_points}"
            print(updated_score)

        if user_live_points <= 0 or computer_points <= 0:
            print("Thanks for playing! The end.")
            if user_live_points == computer_points:
                print(f"It's a tie.\n{user_name} final score is: {user_live_points}\ncomputer final score: {computer_points}")
            elif user_live_points > computer_points:
                print(f"\nCONGRATULATION YOU WIN!\n\n{user_name} final score is: {user_live_points}\ncomputer final score: {computer_points}")
            else:
                print(f"\nYOU LOSE Better luck next time!\n\n{user_name} final score is: {user_live_points}\ncomputer final score: {computer_points}")

play_game()



