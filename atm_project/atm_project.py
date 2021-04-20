# Last updated April 19, 2021
# IMPORTS
import random
import datetime
import validation
import database
from getpass import getpass


# DATABASE
# user_database = {1111111111: ['Soph', 'Velasquez', 'soph@email.com', 'pwSoph', 1000],
#                  2222222222: ["Jazz", "Jazz", "jazz@email.com", "pwJazz", 1500],
#                  3333333333: ["Jo", "Jo", "jojo@email.com", "pwJojo", 2000]}


# INITIALIZING THE SYSTEM // DEFINING FUNCTIONS

def init():
    print("\n*****ʕ·͡ᴥ·ʔ Welcome to bank Sophos. ʕ·͡ᴥ·ʔ*****")
    have_account = int(input('Do you have an account with us? \n 1 (Yes) \n 2 (No)\n'))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print('Invalid option selected.')
        init()


def register():
    print("\n***** Register *****")

    email = input("What is your email address?\n")
    firstname = input("What is your first name?\n")
    lastname = input("What is your last name?\n")
    password = getpass("Create a password for yourself:\n")

    try:
        account_number = generate_account_number()
    except:
        print("An unexpected error occurred. Please try again later.")
        init()

    # user_database[account_number] = [email, firstname, lastname, password, 0]
    # prepared_user_details = firstname + "," + lastname + "," + email + "," + password + "," + str(0)
    is_user_created = database.create(account_number, firstname, lastname, email, password)

    if is_user_created:
        print(
            "Account created.\nYour account number is: %d.\nPlease log in using your new credentials." % account_number)
    else:
        print("Something went wrong. Please try again.")

    init()


def login():
    print("\n***** Log In *****")

    attempted_account_number = input("What is your account number?\n")
    is_valid_account_number = validation.account_number_validation(attempted_account_number)
    if is_valid_account_number:
        attempted_password = getpass("What is your password?\n")
        user = database.authed_user(attempted_account_number, attempted_password)
        if user:
            print("\n***** Login successful! *****")
            bank_operation(user)
        print("Invalid account or password.")
        try_again = int(input("Try again?\n(1) Yes\n(2) No\n"))
        if try_again == 1:
            login()
        else:
            print("Exiting.\n")
            exit()
    else:
        print("Invalid account number. Check that you only have 10 digits and only integers.")
        login()


def bank_operation(user):
    now = datetime.datetime.now()

    print("Welcome %s %s." % (user[0], user[1]))
    print("The time is:")
    print(now.strftime("%m-%d-%y, %H:%M:%S"))
    selected_option = int(
        input("What would you like to do?\n(1) Deposit\n(2) Withdrawal\n(3) Report an issue\n(4) Log out\n(5) Exit\n"))

    if selected_option == 1:
        deposit_operation(user)
        make_another_trans = int(input("Make another transaction?\n(1) Yes\n(2) No\n"))
        if make_another_trans == 1:
            bank_operation(user)
        elif make_another_trans == 2:
            print("Have a nice day!")
            exit()
        else:
            print("Invalid option selected.")
            bank_operation(user)

    elif selected_option == 2:
        withdrawal_operation(user)
        make_another_trans = int(input("Make another transaction?\n(1) Yes\n(2) No\n"))
        if make_another_trans == 1:
            bank_operation(user)
        elif make_another_trans == 2:
            print("Have a nice day!")
            exit()
        else:
            print("Invalid option selected.")
            bank_operation(user)

    elif selected_option == 3:
        complaint_operation()
        return_to_menu = int(input("Return to menu?\n(1) Yes\n(2) No\n"))
        if return_to_menu == 1:
            bank_operation(user)
        elif return_to_menu == 2:
            print("Have a nice day!")
            exit()
        else:
            print("Invalid option selected.")
            bank_operation(user)

    elif selected_option == 4:
        print('Logging Out...')
        print('You are now logged out. Redirecting to home page.')
        init()

    elif selected_option == 5:
        print("Have a nice day!")
        exit()

    else:
        print("Invalid option selected.")
        bank_operation(user)


def deposit_operation(user):
    print("\n***** Make a deposit *****")
    # Convert string to integer
    current_balance = int((user[4]))
    # get and display current balance
    print("Your current balance is: $%f" % current_balance)
    # get amount to deposit
    deposit_amount = int(input("How much would you like to deposit?\n"))
    database.deposit(user, deposit_amount)
    print("Your current balance is now: $%f" % current_balance)


def withdrawal_operation(user):
    print("\n***** Make a withdrawal *****")
    # Convert string to integer
    current_balance = int((user[4]))
    # get and display current balance
    print("Your current balance is: $%f" % current_balance)
    # get amount to withdraw
    withdraw_amount = int(input("How much would you like to withdraw?\n"))
    # subtract withdraw amount from current balance.
    database.withdraw(user, withdraw_amount)


def complaint_operation():
    print("\n***** Report an issue *****")
    input("What issue would you like to report?\n")
    print("Thank you for contacting us.")


def generate_account_number():
    return random.randrange(1000000000, 9999999999)


def get_user_balance(user_details):
    return user_details[4]


def set_user_balance(user_details, balance):
    user_details[4] = balance


# ACTUAL BANKING SYSTEM
init()
