# heads or tails game
print('Welcome to our heads or tails game!')

# Get user selection
user_selection = \
input('please press 1 for heads or 2 for tails and then press enter')

if str(1) == user_selection:
    print('you selected heads')
elif str(2) == user_selection:
    print('you selected tails')
else:
    print("you didn't follow instructions...")
    user_selection = \
    input('please press 1 for heads or 2 for tails and then press enter')

# get flip result

# Trimming down import statement to omit the choice option
#from random import choice, random
from random import random

#Using random.choice()
# Ignore this option to focus on the random using the if statement
#coin_flip_with_choice = choice(["Heads","Tails"])

#Using random.random()
coin_flip_with_random = "Heads" if random() > 0.5 else "Tails"
random_number = random()
# comment out a no longer used example
#year = 2016
#event = 'Referendum'
#print(f'Results of the {year} {event}')
#'Results of the 2016 Referendum'
print(f'our random_number was {random_number:.3f}.')
flip_result = "Heads" if random() > 0.5 else "Tails"

# Ignore this option to focus on the random using the if statement
#print(coin_flip_with_choice)
print(coin_flip_with_random)
print(flip_result)

#Output:
#Tails
#Heads


# if user selection matches flip result, user wins

# else users does not win
