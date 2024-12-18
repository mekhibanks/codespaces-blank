# Discuss the anatomy of a function

# A function definition tells the computer
# the instructions on what we want to do with data

# data = just means data types

# curly brackets = passing in data
# the function definition: this is formally
# called a parameter

# parameter = placeholder

def modifyMyName(name):
    print('Your new modified name is the great '+ name)

# when we pass data into a function call it is called an
# arguement
# arguement = evidence, facts, real data.
# modifyMyname('Mekhi')





# Lesson on Conditional Statements

# conditional statements use the 'If' and 'ELSE'
# keywords to filter and create specific outcomes
# based on data.

def verifyAge(age):
    if age > 17:
        print('Congrats! You can buy GTA VI')
    elif age >28:
        print('Sorry, you're too old for this game.')
    else:
        print('Sorry, you need an adult to buy this game.') 

verifyAge(40)



