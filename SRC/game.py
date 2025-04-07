import random

# Create a grid with categories
grid = [["Category " + str(i + j * 10 + 1) for i in range(10)] for j in range(10)]

# Display the grid
def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
    print("\n")

# Sample trivia questions
questions = {
    "Category 1": {"question": "What is the capital of France?", "answer": "Paris"},
    # Add more categories and questions here
}

# Simulate a trivia question
def trivia_battle(category):
    if category in questions:
        q = questions[category]["question"]
        correct_answer = questions[category]["answer"]
        print(f"Trivia Time! {q}")
        player_answer = input("Your Answer: ")
        if player_answer.strip().lower() == correct_answer.lower():
            print("Correct! You win the challenge!")
            return True
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
            return False
    else:
        print("No questions available for this category.")
        return False

# Example gameplay loop
display_grid(grid)

challenger_category = "Category 1"  # Example challenger square
if trivia_battle(challenger_category):
    print("You take control of the square!")
else:
    print("Better luck next time.")