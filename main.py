import random

while True:
 user_action = input("Enter a choice (r, p, s): ").lower()

 possible_actions = ["r", "p", "s"]
 computer_actions = random.choice(possible_actions)

 print(f"\nYou chose {user_action}, computer chose {computer_actions}.\n")

 if user_action == computer_actions:
    print(f"Both players selected {user_action}. It's a tie!")
 elif user_action == "r":
    if computer_actions == "s":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")
 elif user_action == "p":
    if computer_actions == "r":
        print("Paper covers rock! You win!")
    else:
        print("scissor cuts paper! You lose!.")
 elif user_action == "s":
    if computer_actions == "p":
        print("scissor cuts paper! You win!")
    else:
        print("Rock smashes scissor! You lose.")  
    play_again = input("Play again? (Yes/No): ")
    if play_again.lower() != "Yes":
        break                          