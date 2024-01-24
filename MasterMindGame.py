import random

def get_valid_input(prompt, input_type):
    """
    Function to get valid input of a specified type
    """
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def display_response(correct_digits):
    """
    Function to display response to the player
    """
    response_str = ''.join(correct_digits)
    print(f"Not quite the number. But you did get these digits correct!: {response_str}")

def play_mastermind():
    """
    Main function to play the Mastermind game
    """
    # Generate a random 4-digit number
    secret_number = str(random.randint(1000, 9999))

    try:
        # Get the number of players
        num_players = get_valid_input("Input number of players: ", int)
    except ValueError:
        print("Please enter a valid number of players.")
        return

    attempts_per_player = []

    for player_num in range(1, num_players + 1):
        print(f"\n=== Player {player_num} ===")
        attempts = 0

        # Get the player's guess
        player_guess = get_valid_input("Guess the 4-digit number: ", str)

        while player_guess != secret_number:
            correct_digits = [c if c == secret_number[i] else 'X' for i, c in enumerate(player_guess)]
            display_response(correct_digits)

            attempts += 1

            # Get the player's guess again
            player_guess = get_valid_input("Guess the number again: ", str)

        print("Congratulations! You guessed it right.")
        attempts_per_player.append(attempts)

    # Determine the winner
    min_attempts = min(attempts_per_player)
    winner_index = attempts_per_player.index(min_attempts) + 1
    print(f"\nWinner is Player {winner_index}. They guessed in the minimum number of attempts ({min_attempts} times).")

if __name__ == "__main__":
    play_mastermind()
