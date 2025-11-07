first_name = "YOURFIRSTNAME"
last_name = "YOURLASTNAME"

# Example: If first_name = "JANICE" → janice_x, janice_y
player_var = first_name.lower()
globals()[f"{player_var}_x"] = 0
globals()[f"{player_var}_y"] = 0

# Example: Dela Cruz → last letter = Z → 26
last_letter = last_name[-1].lower()
treasure_x = ord(last_letter) - 96   # a=1, b=2, ..., z=26

# treasure_y stays the same
treasure_y = 3

game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
print(f"Your player variable name is: {player_var}_x and {player_var}_y")

while game_running:
    move = input("Enter move (w/a/s/d or q to quit): ")

    # Movement
    if move == "w":
        globals()[f"{player_var}_y"] += 1
    elif move == "s":
        globals()[f"{player_var}_y"] -= 1
    elif move == "a":
        globals()[f"{player_var}_x"] -= 1
    elif move == "d":
        globals()[f"{player_var}_x"] += 1
    
    # Quit game
    elif move == "q":
        print("Game exited.")
        game_running = False
        continue

    print(f"Player position: ({globals()[f'{player_var}_x']}, {globals()[f'{player_var}_y']})")

    # Win condition
    if globals()[f"{player_var}_x"] == treasure_x and globals()[f"{player_var}_y"] == treasure_y:
        print("WIN! You found the treasure!")
        game_running = False
