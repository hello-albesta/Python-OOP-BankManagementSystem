from datetime import datetime as dt

from abc import ABC, abstractmethod
from tabulate import tabulate

from custom_defined import const_dict as const


class SavingsAccount(ABC):
    def __init__(self,
                 account_number: str,
                 account_holder: str,
                 balance: float,
                 transaction_history):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = transaction_history

    """
    A method to deposit a given amount into the account.

    Parameters:
        export_file_no_error_flag (bool): A flag indicating whether an error occurred during export file creation.
        amount (float): The amount to be deposited into the account.

    Returns:
        None

    ==================================================================================================================

    The explanation of the code snippet:

    This code defines an abstract method called deposit with three parameters:
    self, export_file_no_error_flag, and amount.

    The method does not have any implementation and is meant to be overridden in subclasses.
    """
    @abstractmethod
    def deposit(self, export_file_no_error_flag: bool, amount: float):
        pass

    """
    Withdraws a specified amount from the account.

    Parameters:
        export_file_no_error_flag (bool): A boolean flag indicating whether the withdrawal should be recorded in the export file without any errors.
        amount (float): The amount to withdraw from the account.

    Returns:
        None

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines an abstract method named withdraw that takes three parameters:
    self, export_file_no_error_flag, and amount.

    The withdraw method does not have any implementation and is meant to be overridden by subclasses.
    """
    @abstractmethod
    def withdraw(self, export_file_no_error_flag: bool, amount: float):
        pass

    """
    Calculates the interest for the given account.

    This is an abstract method that needs to be implemented by subclasses.

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet is defining an abstract method called calculate_interest.
    The @abstractmethod decorator indicates that any class that inherits from the class containing this code
    must implement this method.
    """
    @abstractmethod
    def calculate_interest(self):
        pass

    """
    A description of the entire function, its parameters, and its return types.

    :param acc_status: A string representing the account status.
    :param upd_amount: A float representing the updated amount.
    :param total_interest_amt: A float representing the total interest amount.
    :param transaction_time: A string representing the transaction time.

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines an abstract method named acc_transact_history that takes in several parameters
    (acc_status, upd_amount, total_interest_amt, transaction_time).

    The method is marked with the @abstractmethod decorator,
    which means that any class that inherits from the class containing this method must implement it.

    The method itself does not have any implementation and is left empty (pass).
    """
    @abstractmethod
    def acc_transact_history(self, acc_status: str, upd_amount: float, total_interest_amt: float,
                             transaction_time: str):
        pass

    """
    A description of the entire function, its parameters, and its return types.

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines an abstract method called display_account_info that does nothing.
    The @abstractmethod decorator indicates that this method must be implemented by any class that inherits
    from the current class.
    """
    @abstractmethod
    def display_account_info(self):
        pass


class ConventionalSavings(SavingsAccount):
    def __init__(self,
                 account_number: str,
                 account_holder: str,
                 balance: float,
                 transaction_history):
        SavingsAccount.__init__(self,
                                account_number=account_number,
                                account_holder=account_holder,
                                balance=balance,
                                transaction_history=transaction_history)
        self.balance = balance
        self.saving_type = const.ACC_CONVENTIONAL_SAVING_TYPE
        self.min_balance = const.LIMIT_MIN_ACC_AMT_BALANCE
        self.interest_rate = const.CONVENTIONAL_SAVING_TYPE_INTEREST_RATE

    """
    Check if the account balance is below the minimum balance required to avoid a penalty.

    Returns:
        bool: True if the balance is below the minimum, False otherwise.

    ==================================================================================================================

    The explanation of the code snippet:

    This code defines a method called acc_penalty_cond that checks
    if the balance of an account is less than a minimum balance.

    If the balance is less than the minimum balance, it returns True, otherwise it returns False.
    """
    def acc_penalty_cond(self):
        if self.balance < self.min_balance:
            return True

        else:
            return False

    """
    Deposits the specified amount into the account.

    Args:
        export_file_no_error_flag (bool): A flag indicating whether there was an error in the export file.
        amount (float): The amount to be deposited.

    Returns:
        None

    ==================================================================================================================

    The explanation of the code snippet:

    This code defines a deposit method that takes in three arguments: export_file_no_error_flag,
    a boolean indicating if there was an error in exporting a file, amount, the amount to be deposited.

    If export_file_no_error_flag is True, the method increases the balance by amount, calculates the interest,
    records the transaction in the account transaction history, and prints a success message.

    If export_file_no_error_flag is False, the method decreases the balance by amount,
    removes the last transaction from the transaction history (if it exists), and prints a warning message.
    """
    def deposit(self, export_file_no_error_flag: bool, amount: float):
        if export_file_no_error_flag is True:
            self.balance += amount
            interest_amt = self.calculate_interest()

            transaction_time = dt.now().strftime(const.DATETIME_FORMAT)
            acc_status = const.ACC_DEPOSIT_STAT

            self.acc_transact_history(acc_status=acc_status,
                                      upd_amount=amount,
                                      total_interest_amt=interest_amt,
                                      transaction_time=transaction_time)

            print(f"{const.SUCCESS_TEXT_1}${amount} HAS BEEN DEPOSITED IN YOUR ACCOUNT.{const.SUCCESS_TEXT_2}")

        else:
            self.balance -= amount

            if len(self.transaction_history) > 0:
                self.transaction_history.pop()

            print(f"{const.WARNING_TEXT_1}TRANSACTION OF DEPOSIT ${amount} HAS BEEN CANCELLED IN YOUR ACCOUNT."
                  f"{const.WARNING_TEXT_2}")

    """
    Withdraws a specified amount from the account balance.

    Parameters:
        export_file_no_error_flag (bool): A flag indicating if there are any errors in the export file.
        amount (float): The amount to be withdrawn from the account balance.

    Returns:
        bool: True if the withdrawal is successful, False otherwise.

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet is a method called withdraw that belongs to a class.

    It takes three parameters:
    export_file_no_error_flag, which is a boolean indicating whether there was an error in exporting a file,
    amount, which is a float representing the amount to be withdrawn, and
    self, which refers to the instance of the class itself.

    The code checks if export_file_no_error_flag is True.
    If so, it checks if a penalty condition is not met (self.acc_penalty_cond() is False),
    and if the balance is greater than or equal to the specified amount.

    If these conditions are met, it deducts the amount from the balance, calculates interest, 
    records the transaction in the account updates the transaction history, and prints a success message.
    It then returns True.

    If any of the conditions are not met,
    it prints a warning message depending on the specific condition that failed and returns False.

    If export_file_no_error_flag is False, it adds the amount to the balance,
    removes the last transaction from the history (if any), prints a cancellation message, and returns False.
    """
    def withdraw(self, export_file_no_error_flag: bool, amount: float):
        if export_file_no_error_flag is True:
            if self.acc_penalty_cond() is False:
                if self.balance >= amount:
                    self.balance -= amount

                    interest_amt = self.calculate_interest()
                    transaction_time = dt.now().strftime(const.DATETIME_FORMAT)
                    acc_status = const.ACC_WITHDRAW_STAT

                    self.acc_transact_history(acc_status=acc_status,
                                              upd_amount=amount,
                                              total_interest_amt=interest_amt,
                                              transaction_time=transaction_time)

                    print(f"{const.SUCCESS_TEXT_1}${amount} HAS BEEN WITHDRAWN FROM YOUR ACCOUNT."
                          f"{const.SUCCESS_TEXT_2}")

                    return True

                else:
                    print(const.WARNING_TEXT_1 + const.INSUFFICIENT_AMT_BALANCE_WARN + const.WARNING_TEXT_2)

                    return False

            else:
                print(const.WARNING_TEXT_1 + const.ACC_AMT_BALANCE_PENALTY_WARN + const.WARNING_TEXT_2)

                return False

        else:
            self.balance += amount

            if len(self.transaction_history) > 0:
                self.transaction_history.pop()

            print(f"{const.WARNING_TEXT_1}TRANSACTION OF WITHDRAW ${amount} HAS BEEN CANCELLED IN YOUR ACCOUNT."
                  f"{const.WARNING_TEXT_2}")

            return False

    """
    Calculates the simple interest earned based on the current balance and interest rate.

    Returns:
        float: The simple interest earned.

    ==================================================================================================================

    The explanation of the code snippet:

    This code defines a method called calculate_interest that calculates the simple interest earned
    based on the balance and interest rate of an account. It then prints the result and returns it.
    """
    def calculate_interest(self):
        simple_interest = self.balance * (self.interest_rate / 100)

        print(f"SIMPLE INTEREST EARNED IS {const.SUCCESS_TEXT_1}${simple_interest}{const.SUCCESS_TEXT_2}.")

        return simple_interest

    """
    Updates the account transaction history with the provided details.

    Args:
        acc_status (str): The status of the account transaction.
        upd_amount (float): The amount of the transaction.
        total_interest_amt (float): The total interest amount.
        transaction_time (str): The time of the transaction.

    Returns:
        None

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a method acc_transact_history that takes in several parameters representing
    the status of an account, the amount to be updated, the total interest amount, and the transaction time.

    Inside the method, the code checks the account status and updates the balance and status amount accordingly.
    It then creates a dictionary acc_track_hist that represents the transaction history with keys such as
    account status, balance before, balance, updated status amount, total interest rate, and transaction time.

    Finally, the method assigns the transaction history dictionary to the transaction_history attribute of the object.
    """
    def acc_transact_history(self, acc_status: str, upd_amount: float, total_interest_amt: float,
                             transaction_time: str):
        balance_before = 0
        upd_stat_amount = ''

        if acc_status == const.ACC_DEPOSIT_STAT:
            balance_before = (self.balance - upd_amount)
            upd_stat_amount = const.ACC_AMT_BALANCE_INCREMENT

        elif acc_status == const.ACC_WITHDRAW_STAT:
            balance_before = (self.balance + upd_amount)
            upd_stat_amount = const.ACC_AMT_BALANCE_DECREMENT

        acc_track_hist = {
            const.ACC_STATUS_KEY: acc_status,
            const.ACC_BALANCE_BEFORE_KEY: balance_before,
            const.ACC_BALANCE_KEY: self.balance,
            upd_stat_amount: upd_amount,
            const.ACC_INTEREST_RATE_KEY: total_interest_amt,
            const.ACC_TIME_KEY: transaction_time,
        }

        self.transaction_history = [acc_track_hist]

    """
    Display the account information of the user.

    This function retrieves the user's account information, such as the saving type, account number, account holder, and balance. It then prints the account information in a tabular format.

    Parameters:
        self (object): The object instance of the class.

    Returns:
        None

    ==================================================================================================================

    The explanation of the code snippet:

    This code defines a method called display_account_info that prints a table of user account information.
    It creates a dictionary account_info with keys representing different attributes of the account
    (such as saving type, account number, account holder, and balance).

    Then, it uses the tabulate function to format and print the table using the account_info dictionary.
    """
    def display_account_info(self):
        account_info = {
            const.ACC_SAVING_TYPE_KEY: self.saving_type,
            const.ACC_NUMBER_KEY: self.account_number,
            const.ACC_NAME_KEY: self.account_holder,
            const.ACC_BALANCE_KEY: self.balance
        }

        print("<< USER ACCOUNT INFORMATION TABLE >>")
        print(tabulate(tabular_data=[account_info],
                       headers='keys',
                       tablefmt='fancy_grid',
                       showindex=False,
                       stralign="center",
                       numalign="right"))


class ShariaSavings(SavingsAccount):
    def __init__(self,
                 account_number: str,
                 account_holder: str,
                 balance: float,
                 transaction_history):
        SavingsAccount.__init__(self,
                                account_number=account_number,
                                account_holder=account_holder,
                                balance=balance,
                                transaction_history=transaction_history)
        self.balance = balance
        self.saving_type = const.ACC_SHARIA_SAVING_TYPE
        self.interest_rate = const.SHARIA_SAVING_TYPE_INTEREST_RATE

    """
    Deposit an amount into the account.

    Parameters:
        export_file_no_error_flag (bool): A flag indicating if the export file has any error.
        amount (float): The amount to be deposited.

    Returns:
        None

    ==================================================================================================================

    The explanation of the code snippet:

    This code defines a deposit method that takes three arguments: export_file_no_error_flag, amount, and self.

    If export_file_no_error_flag is True, it performs the following actions:

    It adds the amount to the balance attribute of the object.
    It calculates the interest amount using the calculate_interest method.
    It sets the transaction_time variable to the current date and time.
    It sets the acc_status variable to a constant value.
    It calls the acc_transact_history method with several arguments.
    It prints a success message.
    If export_file_no_error_flag is not True, it performs the following actions:

    It subtracts the amount from the balance attribute of the object.
    If the transaction_history list is not empty, it removes the last item.
    It prints a warning message.

    Overall, this code snippet represents a method that handles deposit transactions for an account,
    updating the balance and transaction history accordingly.
    """
    def deposit(self, export_file_no_error_flag: bool, amount: float):
        if export_file_no_error_flag is True:
            self.balance += amount
            interest_amt = self.calculate_interest()

            transaction_time = dt.now().strftime(const.DATETIME_FORMAT)
            acc_status = const.ACC_DEPOSIT_STAT

            self.acc_transact_history(acc_status=acc_status,
                                      upd_amount=amount,
                                      total_interest_amt=interest_amt,
                                      transaction_time=transaction_time)

            print(f"{const.SUCCESS_TEXT_1}${amount} HAS BEEN DEPOSITED IN YOUR ACCOUNT.{const.SUCCESS_TEXT_2}")

        else:
            self.balance -= amount

            if len(self.transaction_history) > 0:
                self.transaction_history.pop()

            print(f"{const.WARNING_TEXT_1}TRANSACTION OF DEPOSIT ${amount} HAS BEEN CANCELLED IN YOUR ACCOUNT."
                  f"{const.WARNING_TEXT_2}")

    """
    Withdraws a specified amount from the account balance.

    Parameters:
        export_file_no_error_flag (bool): A flag indicating if there was no error in exporting the file.
        amount (float): The amount to be withdrawn from the account balance.

    Returns:
        bool: True if the withdrawal is successful, False otherwise.

    ==================================================================================================================

    The explanation of the code snippet:

    This code defines a withdraw method that takes three parameters: self, export_file_no_error_flag, and amount.

    If export_file_no_error_flag is True, it checks if the account balance is greater than or equal
    to the withdrawal amount.

    If so, it subtracts the amount from the balance, calculates the interest, updates the transaction history,
    and returns True. If the balance is insufficient, it prints a warning message and returns False.

    If export_file_no_error_flag is not True, it adds the amount to the balance,
    removes the last transaction from the history (if any), prints a cancellation message, and returns False.
    """
    def withdraw(self, export_file_no_error_flag: bool, amount: float):
        if export_file_no_error_flag is True:
            if self.balance >= amount:
                self.balance -= amount
                interest_amt = self.calculate_interest()

                transaction_time = dt.now().strftime(const.DATETIME_FORMAT)
                acc_status = const.ACC_WITHDRAW_STAT

                self.acc_transact_history(acc_status=acc_status,
                                          upd_amount=amount,
                                          total_interest_amt=interest_amt,
                                          transaction_time=transaction_time)

                print(f"{const.SUCCESS_TEXT_1}${amount} HAS BEEN WITHDRAWN FROM YOUR ACCOUNT.{const.SUCCESS_TEXT_2}")

                return True

            else:
                print(const.WARNING_TEXT_1 + const.INSUFFICIENT_AMT_BALANCE_WARN + const.WARNING_TEXT_2)

                return False

        else:
            self.balance += amount

            if len(self.transaction_history) > 0:
                self.transaction_history.pop()

            print(f"{const.WARNING_TEXT_1}TRANSACTION OF WITHDRAW ${amount} HAS BEEN CANCELLED IN YOUR ACCOUNT."
                  f"{const.WARNING_TEXT_2}")

            return False

    """
    Calculate the interest earned based on the current balance and interest rate.

    :return: The simple interest earned.

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a method called calculate_interest that calculates the simple interest earned
    based on the balance and interest rate of an account.

    It then prints the result and returns the simple interest earned.
    """
    def calculate_interest(self):
        simple_interest = self.balance * (self.interest_rate / 100)

        print(f"SIMPLE INTEREST EARNED IS {const.SUCCESS_TEXT_1}${simple_interest}{const.SUCCESS_TEXT_2}.")

        return simple_interest

    """
    Updates the transaction history of the account.

    Parameters:
        acc_status (str): The status of the account transaction.
        upd_amount (float): The amount to be updated in the account.
        total_interest_amt (float): The total interest amount in the account.
        transaction_time (str): The time of the transaction.

    Returns:
        None

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a method called acc_transact_history that takes in several parameters
    related to a financial transaction.

    Depending on the value of the acc_status parameter, the code calculates the balance_before value and
    assigns a corresponding value to upd_stat_amount.

    Then, a dictionary called acc_track_hist is created to store the transaction details.

    Finally, the transaction_history attribute of the object is updated with the acc_track_hist dictionary.
    """
    def acc_transact_history(self, acc_status: str, upd_amount: float, total_interest_amt: float,
                             transaction_time: str):
        balance_before = 0
        upd_stat_amount = ''

        if acc_status == const.ACC_DEPOSIT_STAT:
            balance_before = (self.balance - upd_amount)
            upd_stat_amount = const.ACC_AMT_BALANCE_INCREMENT

        elif acc_status == const.ACC_WITHDRAW_STAT:
            balance_before = (self.balance + upd_amount)
            upd_stat_amount = const.ACC_AMT_BALANCE_DECREMENT

        acc_track_hist = {
            const.ACC_STATUS_KEY: acc_status,
            const.ACC_BALANCE_BEFORE_KEY: balance_before,
            const.ACC_BALANCE_KEY: self.balance,
            upd_stat_amount: upd_amount,
            const.ACC_INTEREST_RATE_KEY: total_interest_amt,
            const.ACC_TIME_KEY: transaction_time,
        }

        self.transaction_history = [acc_track_hist]

    """
    Display the account information in a tabulated format.

    Parameters:
        None

    Returns:
        None

    ==================================================================================================================

    The explanation of the code snippet:

    This code defines a method called display_account_info that creates a dictionary containing information
    about an account.

    It then uses the tabulate function to print the account information in a formatted table.
    """
    def display_account_info(self):
        account_info = {
            const.ACC_SAVING_TYPE_KEY: self.saving_type,
            const.ACC_NUMBER_KEY: self.account_number,
            const.ACC_NAME_KEY: self.account_holder,
            const.ACC_BALANCE_KEY: self.balance
        }

        print("<< USER ACCOUNT INFORMATION TABLE >>")
        print(tabulate(tabular_data=[account_info],
                       headers='keys',
                       tablefmt='fancy_grid',
                       showindex=False,
                       stralign="center",
                       numalign="right"))
