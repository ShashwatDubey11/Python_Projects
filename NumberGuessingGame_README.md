Number Guessing Game !

 This Jupyter Notebook contains a simple Python script that implements a Number Guessing Game. The game prompts the player to enter a range of numbers, generates a random number within that range, and challenges the player to guess the correct number. The player receives feedback on each guess, and the game continues until the correct number is guessed.

How to Play:

1. Run the Jupyter Notebook:
   - Ensure that you have a Jupyter Notebook environment set up.
   - Open this notebook in your Jupyter environment.
   - Execute the code cells one by one to load and run the Python script.

2. Enter the Number Range:
   - When prompted, enter a range of numbers (two integers separated by a comma).

3. Guess the Number:
   - The script will generate a random number within the specified range.
   - Enter your guesses when prompted. The script will provide feedback on whether your guess is too high or too low.

4. Continue Guessing:
   - Keep guessing until you correctly identify the random number.

Outcome:

- The game will declare whether you won and in how many attempts.
- If you couldn't guess the number within the minimum expected attempts, the correct number will be revealed.

Script Explanation:

Libraries Used:
- The script utilizes the random module for generating random numbers and the math module for mathematical calculations.

User Input:
- Players are prompted to enter a range of numbers at the beginning of the game.

Game Logic:
- The script generates a random number within the specified range.
- Players continue guessing until they correctly identify the random number.
- Feedback is provided for each guess, indicating whether the guess is too high or too low.

Outcome Determination:
- The game determines whether the player won based on the minimum expected attempts calculated using log2(range_size).
- The player is notified of their performance.

Have fun playing the Number Guessing Game!
