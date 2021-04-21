# create record
# update record
# read record
# delete record

# find user
import os
import validation

user_db_path = "data/user_record/"
auth_session_path = "data/auth_session/"


def create(account_number, firstname, lastname, email, password):
    # create a file
    # name of the file would be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then delete created file
    if does_account_number_exist(account_number):
        return False

    if does_email_exist(email):
        print("An account with this email address already exists.")
        return False

    user_data = firstname + "," + lastname + "," + email + "," + password + "," + str(0) + "," + str(account_number)

    completion_state = False

    try:
        f = open(user_db_path + str(account_number) + ".txt", "x")
    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(account_number) + ".txt")
        if not does_file_contain_data:
            print("Deleting incomplete file.")
            delete(account_number)
    else:
        f.write(str(user_data))
        completion_state = True
    finally:
        f.close()
        return completion_state


def read(account_number):
    # find user with corresponding account number
    # fetch the contents of the file
    is_valid_account_number = validation.account_number_validation(account_number)

    try:
        if is_valid_account_number:
            f = open(user_db_path + str(account_number) + ".txt", "r")
        else:
            f = open(user_db_path + account_number, "r")
    except FileNotFoundError:
        print("Error: User not found")
    except FileExistsError:
        print("Error: User already exists")
    except TypeError:
        print("Error: Invalid format")
    else:
        return f.readline()
    return False


def update(account_number, number):
    print("update user record")
    print(read(account_number))
    user = str.split(read(account_number), ',')

    balance = str(int(user[4]) + int(number))
    print("depositing $" + balance)
    user[4] = balance
    print(user)
    updated_info = ""
    x = 0
    for elem in user:
        if x < len(user) - 1:
            updated_info += elem + ","
            x += 1
        else:
            updated_info += elem
    print(updated_info)
    print("end")
    f = open(user_db_path + str(account_number) + ".txt", "w")
    f.write(updated_info)
    f.close()
    f = open(user_db_path + str(account_number) + ".txt", "r")
    print(f.read)


def pre_deposit(user):
    print("\n***** Make a deposit *****")
    deposit_operation(user[5])


def deposit_operation(account_number):
    read(account_number)
    user = str.split(read(account_number), ',')
    # get and display current balance
    print("Your balance is: $%s" % user[4])
    # get amount to deposit
    deposit_amount = int(input("How much would you like to deposit?\n"))
    deposit(user[5], deposit_amount)


def deposit(account_number, number):
    read(account_number)
    user = str.split(read(account_number), ',')
    balance = str(int(user[4]) + int(number))
    print("Depositing $%s." % number)
    user[4] = balance
    updated_info = ""
    x = 0
    for elem in user:
        if x < len(user) - 1:
            updated_info += elem + ","
            x += 1
        else:
            updated_info += elem
    print("Your new balance is: $%s" % user[4])
    f = open(user_db_path + str(account_number) + ".txt", "w")
    f.write(updated_info)
    f.close()


def pre_withdraw(user):
    print("\n***** Make a withdrawal *****")
    withdraw_operation(user[5])


def withdraw_operation(account_number):
    read(account_number)
    user = str.split(read(account_number), ',')
    # get and display current balance
    print("Your balance is: $%s" % user[4])
    # get amount to withdraw
    withdraw_amount = int(input("How much would you like to withdraw?\n"))
    withdraw(user[5], withdraw_amount)


def withdraw(account_number, number):
    read(str(account_number))
    user = str.split(read(account_number), ',')

    if int(user[4]) > int(number):
        balance = str(int(user[4]) - int(number))
        print("Withdrawing $%s." % number)
        user[4] = balance
        updated_info = ""
        x = 0
        for elem in user:
            if x < len(user) - 1:
                updated_info += elem + ","
                x += 1
            else:
                updated_info += elem
        print("Your new balance is: $%s" % user[4])
        f = open(user_db_path + str(account_number) + ".txt", "w")
        f.write(updated_info)
        f.close()
    else:
        print("Error: Balance too low.")


def delete(user_account_number):
    # find user with corresponding account number
    # delete user record (file)
    # return True
    is_delete_successful = False
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("Error: User not found")
        finally:
            return is_delete_successful


def does_email_exist(email):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    all_mice = os.listdir(user_db_path)
    for mouse in all_mice:
        if mouse == str(account_number) + ".txt":
            return True
    return False


def authed_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ",")
        if password == user[3]:
            return user
    return False


def create_auth_session_file():
    f1 = open(auth_session_path + "login_session.txt", "w")
    f1.write("User is logged in")


def remove_auth_session_file():
    if os.path.exists(auth_session_path + "login_session.txt"):
        os.remove(auth_session_path + "login_session.txt")
    else:
        print("Error: login_session.txt does not exist.")
