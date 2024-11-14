import random

# Dictionary of fun facts about numbers
fun_facts = {
    0: "Zero is the only number that cannot be represented in Roman numerals.",
    1: "1 is the only number that is neither prime nor composite.",
    2: "2 is the smallest and the only even prime number.",
    3: "A triangle has 3 sides. It's the first number that forms a shape.",
    4: "There are 4 seasons in a year: Spring, Summer, Fall, and Winter.",
    5: "There are 5 senses in the human body: sight, hearing, taste, smell, and touch.",
    6: "A hexagon has 6 sides.",
    7: "Seven is often considered a lucky number and appears in many cultures.",
    8: "A stop sign has 8 sides.",
    9: "A cat is said to have 9 lives!",
    10: "Humans have 10 fingers and toes.",
}

def get_fun_fact(number):
    # If the number exists in our fun_facts dictionary, return its fact
    if number in fun_facts:
        return fun_facts[number]
    # Otherwise, generate a random fact
    else:
        random_fact = f"{number} is a pretty cool number, but we don't have a specific fact for it!"
        return random_fact

def play_game():
    print("Welcome to the Fun Fact Game!")
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Thanks for playing!")
            break
        if user_input.isdigit():
            number = int(user_input)
            fact = get_fun_fact(number)
            print(f"Fun fact about {number}: {fact}")
        else:
            print("Please enter a valid number.")

# Start the game
if __name__ == "__main__":
    play_game()
