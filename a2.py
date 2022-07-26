import random
#Create a function for rolling the dice
def roll_function():
    #Ask the user how many times they want to roll the dice and store it
    roll_amount = int(input("How many times would you like to roll the dice?\n"))

    #Randomly choose a number between 1 and 6 (random.randint) and calculate it for the number of rolls the user has indicated (roll_amount)
    roll = [random.randint(1,6) for i in range(roll_amount)]

    #Calculate the average of the stored dice rolls
    #Define a function for calculating average
    def Average(l): 
        avg = sum(l) / len(l) 
        return avg 
    average = Average(roll)

    #Calculate the total
    total = sum(roll)

   
    #Print the numbers rolled, the average, and the total
    print("Here's what you rolled: ", str(roll))
    print("Here's the average: ", str(average))
    print("Here's the total: ", str(total) )
    
    #Ask the user if they'd like to roll again. If yes, go to roll_function. Otherwise, exit.
    question = input("Would you like to roll again [y/n]?\n")
    while question != 'n':
        if question == 'y': 
            roll_function()
        else:
            print("Invalid resonse. Please type 'y' or 'n'.")
            question = input("Would you like to roll again [y/n]?\n")
    print("Goodbye!")
    exit()

roll_function()