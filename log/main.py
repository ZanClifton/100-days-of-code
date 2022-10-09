import os
import psycopg2
from dotenv import load_dotenv

from database import add_entry, create_table, get_entries
from art import logo

menu = """What do you want to do today?

1) Add a new entry
2) View all entries
3) View entries on a specific day
4) View entries on a specific date
5) Exit

Enter a number: """

welcome = "Welcome to your 100 Days Log!"

read_only_mode = """
Writing new entries has been disabled for now. 

If this is your log, please add a new entry via your local copy, or temporarily enable this functionality.

If you are not the owner of the log, please enjoy your 'read only' access. 

Thank you.

"""


def prompt_new_entry(connection):
    """Prompts new entry and passes details to add_entry function"""
    day = input("Which 100 Days day is this? ")
    date = input("Enter the date (dd-mm-yyyy): ")
    activity = input("What did you do today? ")
    thoughts = input(
        "What are your thoughts about that? What did you learn? How can you apply this in future? "
    )
    github = input("Please link to the GitHub repo or PR: ")
    demo = input("If you have a working demo please link it here: ")
    add_entry(connection=connection,
              entry_activity=activity,
              entry_thoughts=thoughts,
              entry_date=date,
              entry_day=day,
              entry_github=github,
              entry_demo=demo)


def view_entries(entries):
    """Prints entries from array received as argument"""
    for entry in entries:
        print(f"""
    Day: {entry[3]}/100
    Date: {entry[2]}
    Activity: {entry[0]}
    Thoughts: {entry[1]}
    GitHub Link: {entry[4]}
    Demo Link: {entry[5]}

    +++++++++++++++++
        """)


load_dotenv()
database_uri = os.environ["DATABASE_URI"]
connection = psycopg2.connect(database_uri)

print(logo)
print(welcome)
create_table(connection)

while (user_choice := int(input(menu))) != 5:
    if user_choice == 1:
        prompt_new_entry(connection)
        # print(read_only_mode)

    elif user_choice == 2:
        view_entries(entries=get_entries(connection))

    elif user_choice == 3:
        day = int(input("Which day/100 would you like to see entries for? "))
        view_entries(entries=get_entries(connection, day, None))

    elif user_choice == 4:
        date = input("Enter the date (dd-mm-yyyy): ")
        view_entries(entries=get_entries(connection, None, date))

    else:
        print("Invalid option! Try again.")
