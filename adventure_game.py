print("Welcome to The Adventure")
character = input("What is your character's name ")
print(f'{character} is on a quest to find gold and secrets.')
difficulty = int(input(f"What difficulty level should {character} play? (1-10) "))
gold_value = 100
health_drop = 1

health_drop = health_drop * difficulty
print(f'Your health will drop by {health_drop} points each turn.')

gold_value = gold_value / difficulty
print(f'The gold you find will be worth {gold_value} points.')

ask_action = input("Choose an action (explore,talk, rest, or quit)")
if ask_action == "explore":
    health_drop = health_drop * difficulty
    gold_value = gold_value / difficulty
    print(f"You gain the gold {gold_value} and lose the health {health_drop}")

elif ask_action == "talk":
    health_drop = health_drop / difficulty
    gold_value = gold_value / difficulty
    print(f"You lose gold {gold_value} and health {health_drop}")

elif ask_action == "rest":
    health_drop = health_drop * difficulty
    
    print(f"You gain the health {health_drop}")

elif ask_action == "quit":
    print("You left the game")

else:
    print("An unrecognised command")
