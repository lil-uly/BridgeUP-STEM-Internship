# This function asks the user for a number with the input() function
# then checks to see if a number is less than 10 or 50 
# and prints out an appropriate message
def number_game():
    # input() returns a string so we need to use the float() function
    num = float(input("Let's play the number game! Type a number and press return: "))  
    if num < 10:
        print("That's a small number!")
    elif num < 50:
        print("That number isn't too small or too big")
    else:
        print("That's a big number!")
    
    # Ask if the user wants to play again
    response = input("Do you want to play again? (enter yes or no): ")
    return response

# Run the number_game function and store the result in "y_n"
response = number_game()

# This while loop calls the number_game() function as long as response is yes
# and prints "Good bye!" as soon as the response is not "yes"
while response == "yes":
    response = number_game() # This stores the new response
else:
    print("Good bye!")