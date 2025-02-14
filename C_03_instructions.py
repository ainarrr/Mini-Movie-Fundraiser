# Functions go here
def make_statement(statement, decoration):
    """Creates heading (3 lines), subheading (2lines) and
    emphasised text / mini-headings (1 line). Only use emoji for
    single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


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


# Main Routine goes here

make_statment("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("Program continues...")