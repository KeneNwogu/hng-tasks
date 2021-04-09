from random import randint
from datetime import datetime

allowed_names = ['Seyi', 'Mike', 'Love']
user_accounts = [400, 500, 800]
user_account_numbers = [10000, 10001, 10002]
allowed_passwords = ['passwordSeyi', 'passwordMike', 'passwordLove']

def register():
    """
    Registers a user with their name and password.
    If username is available
    """
    name = input("Enter your name: ")
    if name not in allowed_names:
        allowed_names.append(name)
    else:
        print("Name already taken.")
        return register()
    password = input("Enter your password: ")
    allowed_passwords.append(password)
    user_accounts.append(0)
    if create_account_number():
        today = datetime.now() 
        dt_string = today.strftime("%d/%m/%Y %H:%M:%S")    
        print(f"Account Succesfully created at {dt_string}")
        print("You'll be redirected to log-in shortly...")
    return True

def login():
    """
    Logs a user in. 
    no params needed.

    Asks user for and checks if the name is in the list of registered names.
    If user is in allowed is in allowed_names, it asks for the user's password.
    If password is valid with the user, he will be logged in, else an error message will be prompted to the user.

    Returns user's id and True if user logged in properly.
    Returns None and false if user did not log in.
    """
    name = input("Enter your name: ")
    if name in allowed_names:
        user_id = allowed_names.index(name)
    else:
        print('Invalid username. Please try again.') 
        return None, False
    password = input('Enter your password to log in: \n')

    # check if password is valid with the username
    if password == allowed_passwords[user_id]:
        today = datetime.now() 
        dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Welcome {name}!")
        print(f"Account Number: {user_account_numbers[user_id]}")
        print(f"Account Balance: {user_accounts[user_id]}")
        print(f"You logged in at {dt_string} \n")
        print("0. Transfer")
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Complaint')
        print("4. Quit ")

        # returns the user_id and True if user logs in.
        return user_id, True
    else:
        print('Invalid Password, please try again.')
        return None, False

def create_account_number():
    """
    Creates an account number from random digits.
    Checks if account number already exists.
    
    Returns the account number if it created and is not registered.
    Creates another account number if its registered.
    """
    account_number = randint(10000, 90000)
    if account_number not in user_account_numbers:
        user_account_numbers.append(account_number)
        return account_number
    else:
        return create_account_number()

def get_user_requests():
    """
    Queries user for his request option.
    Returns the option the user selected. 
    """
    selectedOption = int(input('Please select an option: \n'))
    return selectedOption

def respond_to_user_request(user_id: int, request: int):
    """
    Responds the request of a logged in user.
    Takes the user's id and requested option as parameters

    request: 0, handles transfer from one account to another,
    request: 1, handles withdrawal from user account to user,
    request: 2, handles deposit from user to user's account,
    request: 3, handles complaints from a user.
    request: 4, exits the user from system.

    For request values of range 0-3, it returns start_another_operation.
    Request value of 4 returns False.
    """
    if request == 0:
        transfer_amount = int(input('Enter amount to transfer: \n'))
        receipient = input("Enter name of user you want to transfer to: \n")
        account_balance = user_accounts[user_id]
        if transfer_amount > account_balance:
            print('Unable to transfer this amount. Insuffient funds')
            return start_another_operation()
        else:
            try:
                receipient_id = allowed_names.index(receipient)
            except ValueError:
                print("Invalid User.")
                return start_another_operation()
            else:
                user_accounts[receipient_id] += transfer_amount
                account_balance -= transfer_amount
                user_accounts[user_id] = account_balance

            print(f'Transfer successful. Your account balance is now: {account_balance}')
            print('Thanks for working with us.')
            return start_another_operation()

    if request == 1:
        withdrawal_amount = int(input('Enter amount to withdraw: \n'))
        account_balance = user_accounts[user_id]
        if withdrawal_amount > account_balance:
            print('Unable to withdraw this amount.')
            return start_another_operation()
        else:
            account_balance -= withdrawal_amount
            user_accounts[user_id] = account_balance
            print(f'Withdrawal successful. Your account balance is now: {account_balance}')
            print('Thanks for working with us.')
            return start_another_operation()
                
    elif request == 2:
        deposit_amount = int(input('Enter amount to deposit: \n'))
        account_balance = user_accounts[user_id]
        account_balance += deposit_amount
        user_accounts[user_id] = account_balance
        print(f'Deposit successful. Your account balance is now: {account_balance}')
        print('Thanks for working with us.')
        return start_another_operation()
            
    elif request == 3:
        get_user_complaint()
        print('Thank you for contacting us.')
        return start_another_operation()

    elif request == 4:
        print("Thanks for working with us. Come again soon.")
        return False

def start_another_operation():
    """
    Asks a user if he wants to start another operation.
    Returns True for values of 1.
    Returns False for values of 2.
    """
    print("Would you like to start another operation? ")
    print("1. Yes")
    print("2. No")
    response = int(input("please select 1 or 2. \n"))
    if response == 1:
        return True
    else:
        print("Thanks for working with us. Come again soon.")
        return False

def get_user_complaint():
    """
    Get user complaint and returns it.
    """
    complaint = input('What issue will you like to report? \n')
    return complaint
        
user_break = False  # breaks out of loop 

while not user_break:
    print("Welcome to Bank. What do you want to do today?")
    print("1. Register ")
    print("2. Login ")
    service = int(input("please select 1 or 2. \n"))
    if service == 1:
        registered = register()
        if registered:
            id, logged = login()
            if logged:
                request = get_user_requests()
                if request == 4:
                    user_break = True
                    print("Thanks for working with us. Come again soon.")
                else:
                    start_again = respond_to_user_request(id, request)
                    while start_again:
                        print("0. Transfer")
                        print('1. Withdrawal')
                        print('2. Deposit')
                        print('3. Complaint')
                        print("4. Quit ")
                        request = get_user_requests()
                        start_again = respond_to_user_request(id, request)
                    if not start_again:
                        user_break = True
                
    elif service == 2:
        id, logged = login()
        if logged:
            request = get_user_requests()
            if request == 4:
                user_break = True
                print("Thanks for working with us. Come again soon.")
            else:
                start_again = respond_to_user_request(id, request)
                while start_again:
                    print('1. Withdrawal')
                    print('2. Deposit')
                    print('3. Complaint')
                    print("4. Quit ")
                    request = get_user_requests()
                    start_again = respond_to_user_request(id, request)
                if not start_again:
                    user_break = True
        