first_name = "YOURFIRSTNAME"
last_name = "YOURLASTNAME"

print("Welcome to Palomado's Maze")
print("Instructions: Use up, left, right, down to move through the maze!")

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
    move = input("Enter move (up/left/down/right): ")

    # Movement
    if move == "up":
        globals()[f"{player_var}_y"] += 1
    elif move == "down":
        globals()[f"{player_var}_y"] -= 1
    elif move == "left":
        globals()[f"{player_var}_x"] -= 1
    elif move == "right":
        globals()[f"{player_var}_x"] += 1
    
    print(f"Player position: ({globals()[f'{player_var}_x']}, {globals()[f'{player_var}_y']})")

    # Win condition
    if globals()[f"{player_var}_x"] == treasure_x and globals()[f"{player_var}_y"] == treasure_y:
        print("WIN! You found the treasure!")
        game_running = False

