import argparse
import random
from game_functions import load_words_from_json, is_valid, initialize_players

def main():
    parser = argparse.ArgumentParser(description="Word Guessing Game")
    parser.add_argument('--json_file', type=str, help='Path to the JSON file containing word categories', default=None)
    parser.add_argument('--num_players', type=int, help='Number of players', default=None)
    
    args = parser.parse_args()

    # Prompt for JSON file path if not provided
    if args.json_file is None:
         args.json_file = input("Please provide the path to the JSON file containing word categories: ")

    # Prompt for number of players if not provided
    if args.num_players is None:
        while True:
            try:
                args.num_players = int(input("Please provide the number of players: "))
                if args.num_players > 0:
                    break
                else:
                    print("The number of players must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
   
    players, players_score = initialize_players(args.num_players)
   

    # Load categories and words from JSON file
    categories = load_words_from_json(args.json_file)
    
    # Allow the player to select a category
    print("Available categories:")
    for category in categories:
        print(category)
    
    selected_category = ""
    while selected_category not in categories:
        selected_category = input("Please select a category from the list above: ").lower()
    
    words_bank = categories[selected_category]


    while words_bank:
        # Pick a random word
        target_word = random.choice(words_bank)
        words_bank.remove(target_word)
        guessed_letters = []
        # Convert the word into "_"
        guess_lst = ["_" for _ in target_word]
        print("Word to guess: " + " ".join(guess_lst))
        
        while "_" in guess_lst:
            for player_idx in range(len(players)):
                player_guess = is_valid(guessed_letters, player_idx, players)
                guessed_letters.append(player_guess)
                if player_guess in target_word:
                    for i in range(len(target_word)):
                        if target_word[i] == player_guess:
                            guess_lst[i] = player_guess
                            players_score[player_idx] += 1
                    print("Current word: " + " ".join(guess_lst))
                    print(f"{players[player_idx]}, your score is: {players_score[player_idx]}")
                else:
                    print(f"Wrong guess, {player_guess} doesn't exist in the word.")
                    print("Current word: " + " ".join(guess_lst))
                            
                if "_" not in guess_lst:
                    break 
        
        if words_bank:
            print(f"Congratulations, {players[player_idx]}! You've completed the word '{target_word}'.")
            print("Let's do another one...")
    print("Game over! All words have been guessed.")

    max_score = max(players_score)
    winners = [players[i] for i, score in enumerate(players_score) if score == max_score]

    print("Final Scores:")
    for player_idx, score in enumerate(players_score):
        print(f"{players[player_idx]}: {score}")

    print(f"Winner(s): {' and '.join(winners)} with a score of {max_score}!")

if __name__ == "__main__":
    main()
