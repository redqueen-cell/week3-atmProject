import datetime
import numpy

now = datetime.datetime.now()

allowedUsers = ["Soph", "Mike", "Love"]
allowedPassword = ["pwSoph", "pwMike", "pwLove"]
numbers = numpy.array([100, 200, 300])
currentBalance = numbers


def main():
    name = input("What's your name? \n")
    if name in allowedUsers:
        password = input("Password? \n")
        userID = allowedUsers.index(name)

        if password == allowedPassword[userID]:
            print("Hello")

            def menu():
                print("Welcome %s." % name)
                print("The date and time is:")
                print(now.strftime("%y-%m-%d %H:%M:%S"))
                print("Your current balance is: %s." % currentBalance[userID])
                print("These are your available options:")
                print("1. Withdrawal")
                print("2. Cash Deposit")
                print("3. Complaint")
                selectedOption = int(input("Please select an option:"))

                if selectedOption == 1:
                    print("You selected %s" % selectedOption)
                    withdrawAmount = int(input("How much would you like to withdraw?"))
                    currentBalance[userID] = currentBalance[userID] - withdrawAmount
                    print("Your current balance is now: %d cash" % currentBalance[userID])
                    print("Take your %s cash" % withdrawAmount)
                    return_menu = input("Return to menu? y/n")
                    if return_menu == "y":
                        menu()
                    else:
                        print("Goodbye")
                        exit()
                elif selectedOption == 2:
                    print("You selected %s" % selectedOption)
                    depositAmount = int(input("How much would you like to deposit?"))
                    currentBalance[userID] = currentBalance[userID] + depositAmount
                    print("Your current balance is now: %d cash" % currentBalance[userID])
                    return_menu = input("Return to menu? y/n")
                    if return_menu == "y":
                        menu()
                    else:
                        print("Goodbye")
                        exit()
                elif selectedOption == 3:
                    print("You selected %s" % selectedOption)
                    complaint = input("What issue would you like to report?")
                    print("Thank you for contacting us about %s." % complaint)
                    return_menu = input("Return to menu? y/n")
                    if return_menu == "y":
                        menu()
                    else:
                        print("Goodbye")
                        exit()

                else:
                    print("Invalid option selected, please try again.")
                    return_menu = input("Return to menu? y/n")
                    if return_menu == "y":
                        menu()
                    else:
                        print("Goodbye")
                        exit()

            menu()
        else:
            print("Password incorrect, please try again.")
    else:
        print("Name not found, please try again.")
        return_login = input("Return to sign in screen? y/n")
        if return_login == "y":
            main()
        else:
            print("Goodbye")
            exit()


main()
