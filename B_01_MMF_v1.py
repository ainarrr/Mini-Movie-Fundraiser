import pandas


# Functions go here
def make_statement(statement, decoration):
    """"Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the first letter of a word from the list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose ab option from {valid_answers}")


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
    
For each ticket holder enter ...
- Their name
-Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the 
ticket cost ( and the profit)
          
Once you have either sp;d a;; of the tickets or entered the exit code ('xxx'),
the program will display the ticket sales information and write the data to a text file)

It will also choose one lucky ticket holder who wins the draw ( their ticket is free))

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def int_check(question):
    """Checks users enter integer )"""

    error = "Oops - please enter an integer more than zero"

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == "exit_code":
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(response)

            if response > 0:
                return response

            else:
                print(error)
        except ValueError:
            print(error)


def currency(x):
    return "${:.2f}".format(x)


# Main Routine goes here

# Initialise ticket numberss
MAX_TICKETS = 5
tickets_sold = 0
# initialise variables / non-default option
payment_ans = ('cash', 'credit')
# Ticket Price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge
CREDIT_SURCHARGE = 0.05

# lists to hold ticket details
all_names = []
all_tickets_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_tickets_costs,
    'Surcharge': all_surcharges
}

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

while tickets_sold < MAX_TICKETS:
    # ask use for their name ( and check it's not blank)
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break
    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 120:
        print("You are too old")
        continue
    else:
        pass

    # ask user for payment method ( cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ({pay_method})")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You sold all the tickets ( ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold}/{MAX_TICKETS} tickets.")
