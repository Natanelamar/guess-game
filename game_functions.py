import json

def load_words_from_json(file_path):
    """Load words from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def is_valid(guessed_letters, player_idx, players):
    """Validate the player's guess."""
    while True:
        user_guess = input(f"{players[player_idx]}, it's your turn to guess a letter: ").lower()
        if len(user_guess) > 1:
            print("Please enter only one letter.")
        elif not user_guess.isalpha():
            print("Sorry, only letters are allowed.")
        elif user_guess in guessed_letters:
            print("This letter has already been guessed. Try another one.")
        else:
            return user_guess

def initialize_players(num_players):
    """Initialize players and their scores."""
    players = []
    players_score = []
    for player in range(num_players):
        players.append(input(f"Player number {player+1}, please type in your name: ").capitalize())
        players_score.append(0)
    return players, players_score
