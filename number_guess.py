# Number Guessing Game

# Task:

# Computer generates a random number (1-100) user keeps guessing until correct. 
# Tell them "Too High" or "Too Low"



# computer_guess = random.randint(1, 101)

# user_guess = int(input("Enter a number of your choice? ")) 

print("Welcome to number guess game!")
print("I'm thinking of a number between 1 and 100") 

import random 

num = random.randint(1, 101)
user_guess = int(input("Enter any number of your choice? ")) 
score = 0
turns = 0
print(num)

guess = True
turns = True
def game(): 
    """Check whether user have the same guess with computer."""
    while turns: 
        def num_guess(guess, answer): 
            
            # user_guess = int(input("Enter any number of your choice? "))
            # computer_guess = random.randint(1, 101)
            
            if guess > answer:
                print("Too high")
            elif guess < answer:
                print("Too low")
            else:
                print(f"You get {answer} correct")
                turns =  False
        guess = num_guess(guess=user_guess, answer=num) 
        
    while guess:
        if guess != num:
            print("You are running out of time")
        else:
            print("Guess again.")
game()


#     while num != guess: 
#         if user_guess == num:
#             print("You're run out of guesses, you lose.")
#         elif user_guess != num:
#             print("Guess again")
            
            
# game()  

# Task 1: A program that calculates exchange rates between 3 African currencies using variables and operators 

# Example:

# Task 2: A program using if/elif/else that categories African countries by GDP per capital into 'Low', 'Middle', 'High' income 

# Task 3: A program using a for loop that processes a list of African city populations and finds the top 3 largest. 

# Task 4: A program using a dictionary that stores 10 African countries with their capitals and lets a user look up any country. 

# Task 5: A program using a function that takes a list of student scores and returns the average, highest and lowest using tuple unpacking. 