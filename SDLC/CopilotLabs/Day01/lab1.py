
# test inline variable suggestions
user_name = input("Please enter your name: ")

# Test Multi-line Function Suggestion
def greet_user(name, email, location):
    print(f"Hello, {name}!")
    print(f"Your email is: {email}")
    print(f"You are located in: {location}")

# Use Comment-Based Code Generation
""" Create a function that takes a list of numbers and returns the sum of all even numbers in the list. """
def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Analyze Multiple Suggestions“

# create a function that takes a list of strings and returns a new list containing only the strings that have more than 5 characters.
def filter_long_strings(strings):
    return [s for s in strings if len(s) > 5]


# Aceept word by word suggestions
def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

# Use Inline Chat (Ctrl + I)

def analyze_scores(score1, score2, score3, score4, score5):
    scores = [score1, score2, score3, score4, score5]
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")


# Using Copilot chat window to generate a function that takes user details and scores as input and displays the total, average, highest, and lowest scores along with the user's name, email, and location.


def display_user_details(name, email, location, score1, score2, score3, score4, score5):
    scores = [score1, score2, score3, score4, score5]
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Location: {location}")
    print(f"Total Score: {total}")
    print(f"Average Score: {average}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")



