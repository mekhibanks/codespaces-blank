# Number 1

def checkNumber(num):
    if num > 0:
        return "this is a positive number"
    elif num < 0:
        return "this is a negative number"
    else:
        return "this is zero "
   

# Number 2

def movieTicketPrice(age):
    if age <= 10:
        return "$5.00"
    elif 16 <= age < 20:
        return "10.00"
    elif age >= 65:
        return "5.00"
    else:
        return "15.00"
   
   

# Number 3


def discountFunction(membership, itemPrice):
    # Define the discount rates for each membership
    if membership == "superShopper":
        print(' You are getting 10 percent off.')
        discount= itemPrice * .1
        total= itemPrice -discount
        print(total)
    elif membership == "megaShopper":
        print(' You are getting 15 percent off.')
    elif membership == "ultraShopper":
        print(' You are getting 20 percent off.')
    else:
        print(' Error: Sorry, that membership type doesnt exist.')
   
discountFunction('superShopper', 150)