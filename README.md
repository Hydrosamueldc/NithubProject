# NithubProject.py
 

 # ELEMENTAL CLASH TEXT-BASE GAME

## INTRODUCTION

The Elemental Clash game is a text-based two-player game where the players compete by choosing elements (fire, water, earth, or air) to clash against each other. Each player starts with 5 life points, and the goal is to reduce the opponent's life points to zero. The game follows specific rules for element matchups, and the player who remains with life points at the end of the game is declared the winner.

### GAME RULES

Each player starts with 5 life points.
Players take turns choosing one of the four elements: fire (F), water (W), earth (E), or air (A).
Element matchups:
Fire beats earth
Water beats fire
Earth beats water
Air beats earth

If both players choose the same element, it results in a tie for that round.
If fire and air or water and air are matched up, it results in a tie, and no damage is dealt to either player.
After each round, the player who wins the clash deals damage to the opponent equal to the difference in life points.
The game continues until one player's life points reach zero.
At the end of the game, the player with remaining life points is declared the winner.

Game Implementation
The game is implemented in Python and is text-based, allowing players to enter their choices through the console. The code is structured into a single function play_game() that encapsulates the entire gameplay.

### Function: play_game():

The play_game() function serves as the entry point of the game and contains the main game loop. It begins by prompting the user to enter their name and then displays the game's rules.

The function uses a while loop to keep the game running until one player's life points reach zero or the user decides to quit. Inside the loop, the computer's choice of element is generated randomly using the random.choice() function.

The user is prompted to enter their choice of element, and the game then determines the winner based on the element matchups. The life points of the players are adjusted accordingly after each round, and the scores are updated.

The game continues until one player wins or the user decides to quit by entering 'q' or 'quit'.

### ELEMENTS DICTONARY

The game uses a dictionary named elements to map the full element names to their abbreviated representations (e.g., "fire" to "F"). This dictionary is used to display the user's and computer's choices in a more readable format.

### HANDLING INVALID INPUT AND USER ELEMENT CHOICES

To ensure that the user enters a valid element choice, the code includes error handling and validation. This code block is responsible for checking if the user's input is valid and converting it to the corresponding element.

Checking for Invalid Input:
The elif condition checks if the user's input is neither a valid element key nor a valid element value (in lowercase) from the elements dictionary. If the condition is true, it means the user entered an invalid input that doesn't match any of the valid elements. In such a case, the code prints "INVALID INPUT" to notify the user.

### DETERMINING THE USER ELEMENT CHOICE

If the user's input is valid, the code proceeds to determine the user's chosen element. The variable user_element is initially set to an empty string.

If the user's input exactly matches one of the valid element keys (e.g., 'fire'), the code sets user_element to that input directly.
If the user's input matches one of the valid element values in lowercase (e.g., 'f' for fire), the code uses a loop to find the corresponding key from the elements dictionary. It iterates over each key-value pair and compares the user's input with the lowercase value of each element. When a match is found, the corresponding key is assigned to user_element, and the loop is terminated using break.

### DISPLAYING UPDATED SCORE

String Formatting using f-strings:
The updated_score variable is a formatted string that uses f-strings (formatted strings) to include dynamic content. The content inside curly braces {} is replaced with the corresponding values at runtime. Let's break down each part of the updated_score string:

{elements[computer]}: This part displays the element chosen by the computer for the current round. It uses the computer variable (which holds the randomly chosen computer element) to access the corresponding abbreviation from the elements dictionary (e.g., 'F' for fire).

{elements[user_element]}: This part displays the element chosen by the user for the current round. It uses the user_element variable, which holds the user's chosen element after handling input validation, to access the corresponding abbreviation from the elements dictionary (e.g., 'W' for water).

{computer_points}: This part displays the current score (life points) of the computer after the current round. The computer_points variable holds the computer's remaining life points.

{user_live_points}: This part displays the current score (life points) of the user after the current round. The user_live_points variable holds the user's remaining life points.

Printing the Updated Scores:
After constructing the updated_score string with the relevant values, the code uses the print function to display the updated scores on the console. The user can see the elements chosen by both the computer and themselves, along with the respective scores for both players.

This mechanism of displaying the updated scores after each round allows players to keep track of their progress and make informed decisions for the next rounds. It enhances the interactive nature of the game and provides immediate feedback on the outcomes of each gameplay interaction.

### ERROR HANDLING  AND INPUT  VALIDATION

Invalid Element Input:
If the user enters an invalid element, the code will display "INVALID INPUT" and prompt the user to enter a valid element. The game will not progress to the next round until a valid input is provided.

Case-Insensitive Input:
The code converts all user inputs to lowercase using .lower() when comparing them with the valid element keys. This ensures that the game can handle inputs like 'Fire', 'FIRE', 'FiRe', etc., and still recognize them as valid elements.

Quitting the Game:
If the user enters 'q' or 'quit', the game will end with a "Thanks for playing! The end." message, and the loop will break, terminating the game.

Handling User Element Choices:
The code ensures that user input for element choices is matched with the corresponding element in the elements dictionary. If the user enters the full element name (e.g., 'fire'), the code directly uses it. If the user enters the abbreviated form (e.g., 'f'), the code looks up the corresponding element and uses it.

Handling Ties and Matchups:
In case of a tie, the code will display "It's a tie." and no damage is dealt to either player. For specific matchups (e.g., 'fire' vs. 'water' or 'water' vs. 'earth'), the code will correctly adjust the life points based on the game rules.

By handling these cases and validating user inputs, the code ensures that the game progresses smoothly and prevents any unexpected errors or invalid inputs from disrupting the gameplay.

### ENDING THE GAME

This code block is responsible for determining when the game should end and displaying the final outcome to the player.

Checking for Game End:
The if statement checks whether either the user's (user_live_points) or the computer's (computer_points) life points have reached zero or less. If this condition evaluates to True, it means that one of the players has lost all their life points, indicating the end of the game.

Ending the Game:
If the condition is true and the game has ended, the code executes the following actions:

It prints "Thanks for playing! The end." to inform the player that the game is over.
The loop within the play_game function will break, and the game will terminate.
Final Outcome:
Before the game ends, the code block doesn't explicitly declare the winner. Instead, it leaves this task for later within the play_game function. The final outcome will be displayed once the game loop ends. The winner will be determined based on the comparison of remaining life points for both the user and the computer.

Game End and Winner Declaration:
The game loop checks if either player's life points reach zero. If that happens, the game ends, and the final scores are displayed. In case of a tie, the code will display "It's a tie." If the user wins, the code will declare "CONGRATULATION YOU WIN!" Otherwise, if the user loses, the code will display "YOU LOSE Better luck next time!".

### play_game() Function Call:

Lastly, the play_game() function is called outside the code block. This function call starts the game and initiates the game loop, allowing the player to make choices and interact with the computer until one player's life points reach zero, leading to the end of the game.

By including this code block, the game can handle the termination condition properly and provide a clear message to the player when the game ends. It also sets the stage for determining and displaying the final outcome of the game.

### HOW TO PLAY

Run the script or execute the code.
Enter your player name when prompted.
Read the game rules and follow the instructions on how to play.
On your turn, enter your choice of element by typing 'Fire/f', 'Water/w', 'Earth/e', 'Air/a', 'Q/q', or 'QUIT/quit' to end the game.
Observe the results of the round and the updated scores.
Continue playing until one player wins or you decide to quit.
At the end of the game, the final scores will be displayed, and the winner (if there is one) will be declared.

### EXPECTED OUTPUT

Enter player name: John
John, welcome to the text-based game Elemental_Clash!

THE RULE OF GAME

The game is played by two players, you and the computer.
Each player starts with a certain number of life points: 5.
On each turn, the players choose one of the four elements: fire/f, water/w, earth/e, air/a.
The element matchups follow the rule: fire beats earth, water beats fire, earth beats water, and air beats earth.
If both players choose the same element, it results in a tie for that round.
If fire and air or water and air are matched up, it results in a tie, and no damage is dealt to either player.
After each round, the winner deals damage to the opponent equal to the difference in life points.
The game continues until one player's life points reach zero.
At the end of the game, the player with remaining life points is declared the winner.

Enter any one of these: 'Fire/f', 'Water/w', 'Earth/e', 'Air/a', or 'Q/q' or 'QUIT/quit' to end the game: fire

You lose.
computer: E
user: F
computer score = 6
your score = 4

Enter any one of these: 'Fire/f', 'Water/w', 'Earth/e', 'Air/a', or 'Q/q' or 'QUIT/quit' to end the game: water

You win.
computer: F
user: W
computer score = 5
your score = 5

Enter any one of these: 'Fire/f', 'Water/w', 'Earth/e', 'Air/a', or 'Q/q' or 'QUIT/quit' to end the game: q

Thanks for playing! The end.
CONGRATULATION YOU WIN!

John final score is: 5
Computer final score: 5
