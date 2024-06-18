import csv, sys

def welcome_screen():
    print("""******************************************
****** WELCOME TO OUT ADOPTION SITE ******
******************************************

Please select one of the following options:
1. Cats
2. Dogs
""")
    user_input = input("Type your animal type here: ")

    querying_db(user_input)

def querying_db(user_input):
    try:
        with open(f'data/{user_input}.csv', newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"{row['name']} is a{row[' age']} year old{row[' breed']}")
    except Exception:
        print(f"Sorry, we don't have any {user_input} here")

welcome_screen()