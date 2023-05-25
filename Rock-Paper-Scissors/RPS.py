# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play, opponent_history=[], sequences={}, history_length=3):
    # Initialize a list to keep track of the opponent's previous moves
    # and a dictionary to keep track of move sequences
    # and a variable to keep track of the length of the move history
    # (with a default value of 3)

    # The three possible moves that the player can make: rock ("R"), paper ("P"), or scissors ("S").
    possible_moves = ["R", "P", "S"]


    # If `prev_play` is not an empty string ("") then it appends the move to `opponent_history`.
    if prev_play != '':
        opponent_history.append(prev_play)
    
      # If there are not enough previous moves in `opponent_history` (less than `history_length`), then it returns a random move from `possible_moves`. This is because there is not enough information to make a prediction at this point.
    if len(opponent_history) < history_length:
        return possible_moves[0]
    
    # If the length of `opponent_history` is greater than `history_length + 1`, it removes the oldest move from `opponent_history`. This ensures that the length of the history is never greater than `history_length + 1`.
    if len(opponent_history) > history_length + 1:
        opponent_history.pop(0)
    
    # Convert the move history list to a string
    current_sequence = "".join(opponent_history)
    
    # Checking if `current_sequence` is in the `sequences` dictionary. If it is, it increments the count for that key-value pair by 1. If it is not, it adds a new key-value pair to `sequences` with `current_sequence` as the key and 1 as the value. This updates the frequency of each sequential combination of moves played. 
    if current_sequence in sequences:
        sequences[current_sequence] += 1
    else:
        sequences[current_sequence] = 1
    
    # Calculate the opponent's most common move based on the move history. Create a new string `current_sequence` by joining the last `history_length` items from `opponent_history`, and then create a list `possible_next_moves` by concatenating `current_sequence` with each possible move from `possible_moves`. It then selects the most common move from `possible_next_moves` using the `max()` function with a `key` function to look up the value from the `sequences` dictionary. The most common move is the last character of the selected sequence, which is accessed with `[-1]`.

    current_sequence =  "".join(opponent_history[-history_length:])
    possible_next_moves = [current_sequence + move for move in possible_moves]
    most_common_move = max(possible_next_moves, key=lambda key: sequences.get(key, 0))[-1]

    predicted_move = {"R": "P", "P": "S", "S": "R"}[most_common_move]

    return predicted_move
    
    







