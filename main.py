import os
import time as system_time
from datetime import datetime as dt

import pandas as pd
from abc import ABC, abstractmethod

from banks import Bank
from savings import ConventionalSavings as Conventional, ShariaSavings as Sharia
from custom_defined import const_dict as const


class BaseMenu(ABC):
    """
    A description of the `display_menu` function, its parameters, and its return types.

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines an abstract method called display_menu inside a class.
    The @abstractmethod decorator indicates that this method must be implemented by any subclass of the class
    that contains it.

    Class BaseMenu is an abstract class that has an abstract method called display_menu with no arguments.
    """
    @abstractmethod
    def display_menu(self):
        pass


class BankApplicationMenu(BaseMenu):
    def __init__(self, accounts):
        self.accounts = accounts

    """
    Display the core menu for the user.

    Parameters:
        user_menu_type (str): The type of menu to display.
        user_main_menu_input (str): The input from the user.
        user_account_bank_obj (object): The bank account object for the user.
        user_saving_type_obj (object): The saving type object for the user.

    Returns:
        None

    ===================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a method called display_core_menu that takes several parameters.
    Within the method, there is a switch statement that checks the value of res_user_main_menu_input and
    performs different actions based on the value.

    In the first case, it prompts the user to input a deposit amount, validates the input, and
    performs a series of operations related to depositing money into an account.

    In the second case, it prompts the user to input a withdrawal amount, validates the input,
    and performs a series of operations related to withdrawing money from an account.

    In the third case, it displays a quit menu and waits for 2 seconds before returning to the main menu.

    At the end of each case, it calls self.display_menu() to display the main menu again.
    """
    def display_core_menu(self, user_menu_type, user_main_menu_input, user_account_bank_obj, user_saving_type_obj):
        res_user_main_menu_input = int(user_main_menu_input)

        if user_menu_type == const.LIST_OF_MENU_TYPE[1] and res_user_main_menu_input == 2:
            res_user_main_menu_input += 1

        match res_user_main_menu_input:
            case 1:
                temp_user_account_deposit_amt = 0
                check_data_input_is_valid = False

                while check_data_input_is_valid is False:
                    check_data_input_is_valid = True

                    print(const.LOGO_MENU_PAGE)
                    print(const.SAVING_TYPE_MENU_PAGE_LINE)

                    user_account_bank_obj.display_transact_hist()

                    print(const.SAVING_TYPE_MENU_PAGE_LINE)
                    print("\n")

                    user_saving_type_obj.display_account_info()

                    print(const.SAVING_TYPE_MENU_PAGE_LINE)
                    print("\n")

                    temp_user_account_deposit_amt = input(f"1. TYPE YOUR DEPOSIT AMOUNT HERE\n"
                                                          f"{const.USER_INPUT_ONLY_NUMBER} $")

                    print(const.SAVING_TYPE_MENU_PAGE_LINE)

                    if not temp_user_account_deposit_amt.isnumeric():
                        check_data_input_is_valid = False

                        print(const.WARNING_TEXT_1 + const.INVALID_USER_NUMBER_INPUT_WARN + const.WARNING_TEXT_2)

                    elif int(temp_user_account_deposit_amt) < const.MIN_DEPOSIT_AMT:
                        check_data_input_is_valid = False

                        print(f"{const.WARNING_TEXT_1}MINIMUM AMOUNT TO DEPOSIT IS {const.MIN_DEPOSIT_AMT}!"
                              f"{const.WARNING_TEXT_2}")

                current_datetime = dt.now().strftime(const.DATETIME_FORMAT)

                user_account_deposit_amt = int(temp_user_account_deposit_amt)

                res_excel_offline_new_export_transact_hist = True

                user_saving_type_obj.deposit(
                    export_file_no_error_flag=res_excel_offline_new_export_transact_hist,
                    amount=user_account_deposit_amt
                )

                self.accounts[const.ACC_BALANCE_KEY] = user_saving_type_obj.balance

                acc_transact_hist_for_offline = {
                    const.ACC_DATE_KEY: current_datetime,
                    const.ACC_TRANSACT_HIST_KEY: user_saving_type_obj.transaction_history
                }

                print(const.PAGING_MENU_JUMP)

                res_excel_offline_new_export_transact_hist = (
                    user_account_bank_obj.excel_offline_new_export_transact_hist(
                        acc_transact_hist=acc_transact_hist_for_offline
                    )
                )

                if res_excel_offline_new_export_transact_hist is True:
                    acc_transact_hist_for_online = {
                        const.ACC_DATE_KEY: current_datetime,
                        const.ACC_BALANCE_KEY: self.accounts[const.ACC_BALANCE_KEY]
                    }

                    # gspreed_transact_hist = {
                    #     const.ACC_DATE_KEY: acc_transact_hist_for_online[const.ACC_DATE_KEY],
                    #     const.ACC_NUMBER_KEY: self.accounts[const.ACC_NUMBER_KEY],
                    #     const.ACC_NAME_KEY: self.accounts[const.ACC_NAME_KEY],
                    #     const.ACC_BALANCE_KEY: acc_transact_hist_for_online[const.ACC_BALANCE_KEY],
                    #     const.ACC_STUDENT_KEY: const.CREATOR_NAME
                    # }
                    #
                    # spreed_transact_hist = []
                    # spreed_transact_hist[len(spreed_transact_hist):] = [i for i in gspreed_transact_hist.values()]
                    #
                    # print(f"spread transact hist: {spreed_transact_hist}")

                    user_account_bank_obj.gdoc_online_export_transact_hist(
                        acc_transact_hist=acc_transact_hist_for_online
                    )

                else:
                    user_saving_type_obj.deposit(
                        export_file_no_error_flag=res_excel_offline_new_export_transact_hist,
                        amount=user_account_deposit_amt
                    )

                    self.accounts[const.ACC_BALANCE_KEY] = user_saving_type_obj.balance

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

                self.display_menu()

            case 2:
                temp_user_account_withdraw_amt = 0
                check_data_input_is_valid = False

                while check_data_input_is_valid is False:
                    check_data_input_is_valid = True

                    print(const.LOGO_MENU_PAGE)
                    print(const.SAVING_TYPE_MENU_PAGE_LINE)

                    user_account_bank_obj.display_transact_hist()

                    print(const.SAVING_TYPE_MENU_PAGE_LINE)
                    print("\n")

                    user_saving_type_obj.display_account_info()

                    print(const.SAVING_TYPE_MENU_PAGE_LINE)
                    print("\n")

                    temp_user_account_withdraw_amt = input(f"1. TYPE YOUR WITHDRAWAL AMOUNT HERE\n"
                                                           f"{const.USER_INPUT_ONLY_NUMBER} $")

                    print(const.SAVING_TYPE_MENU_PAGE_LINE)

                    if not temp_user_account_withdraw_amt.isnumeric():
                        check_data_input_is_valid = False

                        print(const.WARNING_TEXT_1 + const.INVALID_USER_NUMBER_INPUT_WARN + const.WARNING_TEXT_2)

                    elif int(temp_user_account_withdraw_amt) < const.MIN_WITHDRAW_AMT:
                        check_data_input_is_valid = False

                        print(f"{const.WARNING_TEXT_1}MINIMUM AMOUNT TO WITHDRAW IS {const.MIN_WITHDRAW_AMT}!"
                              f"{const.WARNING_TEXT_2}")

                current_datetime = dt.now().strftime(const.DATETIME_FORMAT)

                user_account_withdraw_amt = int(temp_user_account_withdraw_amt)

                res_excel_offline_new_export_transact_hist = True

                res_user_withdraw_transact = user_saving_type_obj.withdraw(
                    export_file_no_error_flag=res_excel_offline_new_export_transact_hist,
                    amount=user_account_withdraw_amt
                )

                if res_user_withdraw_transact is False:
                    system_time.sleep(1)

                    print(const.PAGING_MENU_JUMP)

                    self.display_menu()

                self.accounts[const.ACC_BALANCE_KEY] = user_saving_type_obj.balance

                acc_transact_hist_for_offline = {
                    const.ACC_DATE_KEY: current_datetime,
                    const.ACC_TRANSACT_HIST_KEY: user_saving_type_obj.transaction_history
                }

                print(const.PAGING_MENU_JUMP)

                res_excel_offline_new_export_transact_hist = (
                    user_account_bank_obj.excel_offline_new_export_transact_hist(
                        acc_transact_hist=acc_transact_hist_for_offline
                    )
                )

                if res_excel_offline_new_export_transact_hist is True:
                    acc_transact_hist_for_online = {
                        const.ACC_DATE_KEY: current_datetime,
                        const.ACC_BALANCE_KEY: self.accounts[const.ACC_BALANCE_KEY]
                    }

                    # gspreed_transact_hist = {
                    #     const.ACC_DATE_KEY: acc_transact_hist_for_online[const.ACC_DATE_KEY],
                    #     const.ACC_NUMBER_KEY: self.accounts[const.ACC_NUMBER_KEY],
                    #     const.ACC_NAME_KEY: self.accounts[const.ACC_NAME_KEY],
                    #     const.ACC_BALANCE_KEY: acc_transact_hist_for_online[const.ACC_BALANCE_KEY],
                    #     const.ACC_STUDENT_KEY: const.CREATOR_NAME
                    # }
                    #
                    # spreed_transact_hist = []
                    # spreed_transact_hist[len(spreed_transact_hist):] = [i for i in gspreed_transact_hist.values()]
                    #
                    # print(f"spread transact hist: {spreed_transact_hist}")

                    user_account_bank_obj.gdoc_online_export_transact_hist(
                        acc_transact_hist=acc_transact_hist_for_online
                    )

                else:
                    user_saving_type_obj.withdraw(
                        export_file_no_error_flag=res_excel_offline_new_export_transact_hist,
                        amount=user_account_withdraw_amt
                    )

                    self.accounts[const.ACC_BALANCE_KEY] = user_saving_type_obj.balance

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

                self.display_menu()

            case 3:
                print(const.PAGING_MENU_JUMP)
                print(const.LOGO_QUIT_PAGE)
                print(const.QUIT_BANK_MENU_PAGE)

                system_time.sleep(2)

                print(const.PAGING_MENU_JUMP)

                menu_from_bank_obj = MainApplicationMenu()
                menu_from_bank_obj.display_menu()

    """
    Display the extension menu for the user.

    Args:
        user_transact_hist_data (pd.DataFrame): The user's transaction history data.

    Returns:
        list: A list containing the menu type and the user saving type object.

    ===================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a function extended_display_menu that takes two arguments:
    self and user_transact_hist_data.

    The function checks if user_transact_hist_data is an instance of the pd.DataFrame class.
    If it is, it resets the index of user_transact_hist_data,
    and assigns the value of the const.ACC_NUMBER_KEY key from the dictionary representation of
    user_transact_hist_data to the variable check_user_transact_hist_number.
    Otherwise, it assigns an empty list to check_user_transact_hist_number.

    The function then prints a constant value const.SAVING_TYPE_MENU_PAGE_LINE.

    Next, there are a series of conditional statements based on the value of
    self.accounts[const.ACC_SAVING_TYPE_KEY] and the length of check_user_transact_hist_number.
    Depending on the conditions, the function creates an object of the Conventional or Sharia class,
    passing in several arguments including the account_number, account_holder, balance, and transaction_history.

    The function then prints some constant values, calls the display_account_info method of the created object,
    and prints additional constant values based on certain conditions.

    Finally, the function returns a list containing the values of menu_type and user_saving_type_obj.
    """
    def extended_display_menu(self, user_transact_hist_data):
        if isinstance(user_transact_hist_data, pd.DataFrame):
            user_transact_hist_data.reset_index(drop=True, inplace=True)

            check_user_transact_hist_number = user_transact_hist_data.to_dict()[const.ACC_NUMBER_KEY]

        else:
            check_user_transact_hist_number = []

        print(const.SAVING_TYPE_MENU_PAGE_LINE)

        if (self.accounts[const.ACC_SAVING_TYPE_KEY] == const.ACC_CONVENTIONAL_SAVING_TYPE and
                len(check_user_transact_hist_number) == 0):
            menu_type = "MENU_VER_2"

            user_saving_type_obj = Conventional(account_number=self.accounts[const.ACC_NUMBER_KEY],
                                                account_holder=self.accounts[const.ACC_NAME_KEY],
                                                balance=const.DEF_ACC_BALANCE_DATA,
                                                transaction_history=const.DEF_ACC_TRANSACT_HIST_DATA)

            system_time.sleep(1)

            print("\n")
            print(const.BANK_MENU_PAGE)

            user_saving_type_obj.display_account_info()

            print(const.LIST_OF_ACC_SAVING_TYPE_MENU_INPUT_VER_2)
            print(f"LIMIT ACCOUNT BALANCE: {const.LIMIT_MIN_ACC_AMT_BALANCE}")
            print("")

        elif (self.accounts[const.ACC_SAVING_TYPE_KEY] == const.ACC_CONVENTIONAL_SAVING_TYPE and
              len(check_user_transact_hist_number) > 0):
            latest_idx = (len(user_transact_hist_data.to_dict()[const.ACC_BALANCE_KEY]) - 1)
            check_user_latest_balance = user_transact_hist_data.to_dict()[const.ACC_BALANCE_KEY][latest_idx]
            check_user_transact_hist_list = user_transact_hist_data[const.ACC_TRANSACT_HIST_KEY].tolist()

            transaction_history = check_user_transact_hist_list

            user_saving_type_obj = Conventional(account_number=self.accounts[const.ACC_NUMBER_KEY],
                                                account_holder=self.accounts[const.ACC_NAME_KEY],
                                                balance=check_user_latest_balance,
                                                transaction_history=transaction_history)

            system_time.sleep(1)

            print("\n")
            print(const.BANK_MENU_PAGE)

            user_saving_type_obj.display_account_info()
            user_account_saving_penalty_cond = user_saving_type_obj.acc_penalty_cond()

            if user_account_saving_penalty_cond is False:
                menu_type = "MENU_VER_1"

                print(const.LIST_OF_ACC_SAVING_TYPE_MENU_INPUT_VER_1)
                print(f"LIMIT ACCOUNT BALANCE: {const.LIMIT_MIN_ACC_AMT_BALANCE}")
                print("")

            else:
                menu_type = "MENU_VER_2"

                print(const.LIST_OF_ACC_SAVING_TYPE_MENU_INPUT_VER_2)
                print(f"LIMIT ACCOUNT BALANCE: {const.LIMIT_MIN_ACC_AMT_BALANCE}")
                print("")
                print(const.WARNING_TEXT_1 + const.ACC_AMT_BALANCE_PENALTY_WARN + const.WARNING_TEXT_2)
                print(const.WARNING_TEXT_1 + const.ACC_SAVING_WITHDRAW_BANNED_WARN + const.WARNING_TEXT_2)
                print(const.WARNING_TEXT_1 + const.ACC_SAVING_DEPOSIT_SOME_AMT_BALANCE_FIRST_WARN +
                      const.WARNING_TEXT_2)
                print("")

        elif (self.accounts[const.ACC_SAVING_TYPE_KEY] == const.ACC_SHARIA_SAVING_TYPE and
              len(check_user_transact_hist_number) == 0):
            menu_type = "MENU_VER_2"

            user_saving_type_obj = Sharia(account_number=self.accounts[const.ACC_NUMBER_KEY],
                                          account_holder=self.accounts[const.ACC_NAME_KEY],
                                          balance=const.DEF_ACC_BALANCE_DATA,
                                          transaction_history=const.DEF_ACC_TRANSACT_HIST_DATA)

            system_time.sleep(1)

            print("\n")
            print(const.BANK_MENU_PAGE)

            user_saving_type_obj.display_account_info()

            print(const.LIST_OF_ACC_SAVING_TYPE_MENU_INPUT_VER_2)
            print("")

        else:
            latest_idx = (len(user_transact_hist_data.to_dict()[const.ACC_BALANCE_KEY]) - 1)
            check_user_latest_balance = user_transact_hist_data.to_dict()[const.ACC_BALANCE_KEY][latest_idx]
            check_user_transact_hist_list = user_transact_hist_data[const.ACC_TRANSACT_HIST_KEY].tolist()

            transaction_history = check_user_transact_hist_list

            user_saving_type_obj = Sharia(account_number=self.accounts[const.ACC_NUMBER_KEY],
                                          account_holder=self.accounts[const.ACC_NAME_KEY],
                                          balance=check_user_latest_balance,
                                          transaction_history=transaction_history)

            system_time.sleep(1)

            print("\n")
            print(const.BANK_MENU_PAGE)

            user_saving_type_obj.display_account_info()

            if check_user_latest_balance >= const.LIMIT_MIN_ACC_AMT_BALANCE:
                menu_type = "MENU_VER_1"

                print(const.LIST_OF_ACC_SAVING_TYPE_MENU_INPUT_VER_1)

            else:
                menu_type = "MENU_VER_2"

                print(const.LIST_OF_ACC_SAVING_TYPE_MENU_INPUT_VER_2)

            print("")

        return [menu_type, user_saving_type_obj]

    """
    Display the main menu of the application.

    This function prints the logo and the saving type menu page line.

    It then creates an instance of the Bank class with the accounts attribute set to the accounts passed to
    the constructor. It calls the display_transact_hist method of the Bank instance to display
    the transaction history.

    It then calls the get_selected_user_transact_hist_data method of the Bank instance to get
    the selected user's transaction history data.

    It calls the extended_display_menu function with the argument user_transact_hist_data set to
    the value returned by the get_selected_user_transact_hist_data method.

    It assigns the first element of the returned value to the variable res_menu_type and
    the second element to the variable res_user_saving_type_obj.

    It initializes the variable user_main_menu_input to the string '0' and
    the variable check_data_input_is_valid to False.

    It enters a while loop that continues until check_data_input_is_valid is True.
    Inside the loop, it checks the value of res_menu_type and prints a message according to the menu type.

    It prompts the user for input using the const.USER_INPUT_ONLY_NUMBER message and
    assigns the input to the variable user_main_menu_input.

    It checks if the input is not numeric and sets check_data_input_is_valid to False.
    It prints an error message using const.WARNING_TEXT_1, const.INVALID_USER_NUMBER_INPUT_WARN,
    and const.WARNING_TEXT_2.

    It checks if the menu type is the first type and if the input is not between 1 and 3 (inclusive).
    If so, it sets check_data_input_is_valid to False.
    It prints an error message using const.WARNING_TEXT_1, const.INVALID_USER_NUMBER_OUT_OF_RANGE_INPUT_WARN,
    and const.WARNING_TEXT_2.

    It checks if the menu type is the second type and if the input is not between 1 and 2 (inclusive).
    If so, it sets check_data_input_is_valid to False.
    It prints an error message using const.WARNING_TEXT_1, const.INVALID_USER_NUMBER_OUT_OF_RANGE_INPUT_WARN,
    and const.WARNING_TEXT_2.

    It calls the sleep method of the system_time module with an argument of 1 to pause the execution for 1 second.

    It prints the const.PAGING_MENU_JUMP message.

    It calls the display_core_menu function with the following arguments:
        - user_menu_type: the value of res_menu_type
        - user_main_menu_input: the value of user_main_menu_input
        - user_account_bank_obj: the instance of the Bank class created earlier
        - user_saving_type_obj: the value of res_user_saving_type_obj

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a method called display_menu in a class.
    It prints a menu page and some lines, creates a Bank object, displays transaction history,
    and gets user transaction history data.

    It then calls another method called extended_display_menu with the user transaction history data and
    stores the returned values.

    The code then goes into a while loop that checks if the user input is valid based on the menu type.
    If the input is not valid, warning messages are printed.
    Once the input is valid, the code sleeps for 1 second, prints a paging menu,
    and calls another method called display_core_menu with various parameters.

    Overall, this code seems to be part of a larger program that handles menu display and user input validation.
    """
    def display_menu(self):
        print(const.LOGO_MENU_PAGE)
        print(const.SAVING_TYPE_MENU_PAGE_LINE)

        user_account_bank_obj = Bank(accounts=self.accounts)
        user_account_bank_obj.display_transact_hist()
        get_user_transact_hist_data = user_account_bank_obj.get_selected_user_transact_hist_data()

        res_extended_display = self.extended_display_menu(user_transact_hist_data=get_user_transact_hist_data)
        res_menu_type = res_extended_display[0]
        res_user_saving_type_obj = res_extended_display[1]

        user_main_menu_input = '0'
        check_data_input_is_valid = False

        while check_data_input_is_valid is False:
            check_data_input_is_valid = True

            if res_menu_type == const.LIST_OF_MENU_TYPE[0]:
                print("TYPE YOUR CHOICE [from 1 to 3]!")

            elif res_menu_type == const.LIST_OF_MENU_TYPE[1]:
                print("TYPE YOUR CHOICE [from 1 to 2]!")

            user_main_menu_input = input(const.USER_INPUT_ONLY_NUMBER)

            if not user_main_menu_input.isnumeric():
                check_data_input_is_valid = False

                print(const.WARNING_TEXT_1 + const.INVALID_USER_NUMBER_INPUT_WARN + const.WARNING_TEXT_2)
                print("\n\n")

            elif res_menu_type == const.LIST_OF_MENU_TYPE[0] and not (1 <= int(user_main_menu_input) <= 3):
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_NUMBER_OUT_OF_RANGE_INPUT_WARN} 1 to 3"
                      f"{const.WARNING_TEXT_2}")
                print("\n\n")

            elif res_menu_type == const.LIST_OF_MENU_TYPE[1] and not (1 <= int(user_main_menu_input) <= 2):
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_NUMBER_OUT_OF_RANGE_INPUT_WARN} 1 to 2"
                      f"{const.WARNING_TEXT_2}")
                print("\n\n")

        system_time.sleep(1)

        print(const.PAGING_MENU_JUMP)

        self.display_core_menu(user_menu_type=res_menu_type,
                               user_main_menu_input=user_main_menu_input,
                               user_account_bank_obj=user_account_bank_obj,
                               user_saving_type_obj=res_user_saving_type_obj)


class LoginApplicationMenu(BaseMenu):
    def __init__(self):
        self.user_position = const.LOGIN_MAIN_MENU_TITLE

    """
    Prompt the user to go back to the menu.

    This function waits for 1 second, then enters a loop to check if the user input is valid.

    The user is prompted with a message asking if they want to try the user's position again or go back to the menu.
    The user's input is obtained using the input() function.

    If the user input is equal to the constant LOGIN_MAIN_MENU_TITLE,
    the check_data_input_is_valid variable is set to True.
    After waiting for 1 second, the constant PAGING_MENU_JUMP is printed.
    An instance of the LoginApplicationMenu class is created and its display_menu() method is called.

    If the user input is equal to the constant MAIN_MENU_TITLE, the check_data_input_is_valid variable is set to True.
    After waiting for 1 second, the constant PAGING_MENU_JUMP is printed.
    An instance of the MainApplicationMenu class is created and its display_menu() method is called.

    ==================================================================================================================

    The explanation of the code snippet:

    This code defines a function called prompt_user_back_to_menu that prompts the user
    to either try a certain action again or go back to the main menu.

    It uses a while loop to continuously prompt the user until a valid input is received.
    The user's input is checked against certain constants and if a match is found,
    the corresponding menu object is created and its display_menu method is called.
    """
    def prompt_user_back_to_menu(self):
        system_time.sleep(1)

        check_data_input_is_valid = False

        while check_data_input_is_valid is False:
            print(f"You want try to {self.user_position} again OR back to MENU?")

            user_input = input(f"TYPE \"{self.user_position}\" OR \"MENU\": ")

            if user_input.upper() == const.LOGIN_MAIN_MENU_TITLE:
                check_data_input_is_valid = True

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

                login_menu_obj = LoginApplicationMenu()
                login_menu_obj.display_menu()

            elif user_input.upper() == const.MAIN_MENU_TITLE:
                check_data_input_is_valid = True

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

                main_menu_obj = MainApplicationMenu()
                main_menu_obj.display_menu()

    """
    Display the menu for the user to interact with the bank application.

    This function prompts the user to enter their name and password in order to log in to the bank application.
    The user is asked to enter their name, which should be at least 4 characters long and
    contain only alphabetic characters.

    The user is then asked to enter their password, which should be at least 5 characters long.

    If the user's name or password does not meet the requirements,
    a warning message is displayed and the user is asked to enter the information again.

    If the user's name and password are valid, the function checks if the user is registered in the bank's database.

    If the user is not registered, a warning message is displayed.

    If the user is registered, their account number and saving type are retrieved from the database.

    Depending on the saving type of the user's account,
    a message is displayed indicating whether they will be directed to a conventional saving type or
    a sharia saving type.

    After displaying the appropriate message,
    the function calls the `display_menu` method of the `BankApplicationMenu` class to display the
    menu options for the user.

    Finally, the function prompts the user to go back to the main menu.

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a function called display_menu that prompts the user for their name and password.
    It validates the input and checks if the user is registered.

    If the user is registered, it retrieves their account number and savings type.
    Then it displays a menu based on the savings type. Finally, it prompts the user to go back to the menu.
    """
    def display_menu(self):
        account = {}
        check_data_input_is_valid = False

        while check_data_input_is_valid is False:
            check_data_input_is_valid = True

            print(const.LOGO_MENU_PAGE)
            print(const.LOGIN_MENU_PAGE)
            print("What is your NAME?\n"
                  "TYPE YOUR NAME!")

            account[const.ACC_NAME_KEY] = (input("[At least 4 CHARACTERS & ONLY ALPHABET (with/no SPACE) "
                                                 "(Case-insensitive)!]: ")
                                           .title().strip())

            account[const.ACC_NAME_KEY] = ' '.join(account[const.ACC_NAME_KEY].split())
            temp_account_name_key = account[const.ACC_NAME_KEY].replace(" ", "")

            if len(temp_account_name_key) < 4:
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_STRING_OUT_OF_RANGE_INPUT_WARN} "
                      f"3 CHARACTERS{const.WARNING_TEXT_2}")

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

            elif not temp_account_name_key.isalpha():
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_STRING_INPUT_WARN}{const.WARNING_TEXT_2}")

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

        check_data_input_is_valid = False

        while check_data_input_is_valid is False:
            check_data_input_is_valid = True

            system_time.sleep(1)

            print(const.PAGING_MENU_JUMP)
            print(const.LOGO_MENU_PAGE)
            print(const.LOGIN_MENU_PAGE)
            print("What is your PASSWORD?\n"
                  "TYPE YOUR PASSWORD!")

            account[const.ACC_PASS_KEY] = input("[At least 5 CHARACTERS (Case-sensitive)!]: ")

            if len(account[const.ACC_PASS_KEY]) < 5:
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_STRING_OUT_OF_RANGE_INPUT_WARN} 4 CHARACTERS"
                      f"{const.WARNING_TEXT_2}")

        temp_user_account_bank_obj = Bank(account)
        res_user_login = temp_user_account_bank_obj.check_registered_data()

        if not isinstance(res_user_login, pd.DataFrame):
            if res_user_login == const.USER_ACC_NAME_AND_PASS_NOT_FOUND_ERROR:
                print(const.WARNING_TEXT_1 + const.USER_ACC_NAME_AND_PASS_NOT_FOUND_ERROR + const.WARNING_TEXT_2)

        else:
            res_user_login.reset_index(drop=True,
                                       inplace=True)

            account[const.ACC_NUMBER_KEY] = res_user_login.to_dict()[const.ACC_NUMBER_KEY][0]
            account[const.ACC_SAVING_TYPE_KEY] = res_user_login.to_dict()[const.ACC_SAVING_TYPE_KEY][0]

            system_time.sleep(1)

            print(const.PAGING_MENU_JUMP)
            print(const.LOGO_MENU_PAGE)

            if account[const.ACC_SAVING_TYPE_KEY] == const.ACC_CONVENTIONAL_SAVING_TYPE:
                print(f"WILL BE DIRECTED TO {const.ACC_CONVENTIONAL_SAVING_TYPE.upper()} ASAP!")

            else:
                print(f"WILL BE DIRECTED TO {const.ACC_SHARIA_SAVING_TYPE.upper()} ASAP!")

            system_time.sleep(1)

            print(const.PAGING_MENU_JUMP)

            bank_menu_obj = BankApplicationMenu(accounts=account)
            bank_menu_obj.display_menu()

        system_time.sleep(1)

        print(const.PAGING_MENU_JUMP)

        self.prompt_user_back_to_menu()


class RegisterApplicationMenu(BaseMenu):
    def __init__(self):
        self.user_position = const.REGISTER_MAIN_MENU_TITLE

    """
    Prompts the user to go back to the menu.

    This function waits for 1 second using the `sleep` function from the `system_time` module.
    It then prints the constant value `PAGING_MENU_JUMP`.

    It initializes the variable `check_data_input_is_valid` to `False`.

    The function enters a `while` loop and continues looping until `check_data_input_is_valid` is `True`.
    Within the loop, it prints a message asking the user if they want to try the current operation again or
    go back to the menu.

    The user is prompted to input either the value of `self.user_position` or the string "MENU".

    If the user inputs the value of `const.REGISTER_MAIN_MENU_TITLE`,
    the variable `check_data_input_is_valid` is set to `True`.

    The function then waits for 1 second using the `sleep` function from the `system_time` module.
    It prints the constant value `PAGING_MENU_JUMP`.
    It creates an instance of the `RegisterApplicationMenu` class and calls its `display_menu` method.

    If the user inputs the value of `const.MAIN_MENU_TITLE`, the variable `check_data_input_is_valid` is set to `True`.
    The function then waits for 1 second using the `sleep` function from the `system_time` module.
    It prints the constant value `PAGING_MENU_JUMP`.

    It creates an instance of the `MainApplicationMenu` class and calls its `display_menu` method.

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a method called prompt_user_back_to_menu that prompts
    the user to either try something again or go back to the main menu.

    It takes user input and checks if it matches certain values.
    If the input matches const.REGISTER_MAIN_MENU_TITLE,
    it creates an instance of the RegisterApplicationMenu class and calls its display_menu method.

    If the input matches const.MAIN_MENU_TITLE, it creates an instance of the MainApplicationMenu class and
    calls its display_menu method.
    """
    def prompt_user_back_to_menu(self):
        system_time.sleep(1)

        print(const.PAGING_MENU_JUMP)

        check_data_input_is_valid = False

        while check_data_input_is_valid is False:
            print(f"You want try to {self.user_position} again OR back to MENU?")

            user_input = input(f"TYPE \"{self.user_position}\" OR \"MENU\": ")

            if user_input.upper() == const.REGISTER_MAIN_MENU_TITLE:
                check_data_input_is_valid = True

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

                register_menu_obj = RegisterApplicationMenu()
                register_menu_obj.display_menu()

            elif user_input.upper() == const.MAIN_MENU_TITLE:
                check_data_input_is_valid = True

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

                main_menu_obj = MainApplicationMenu()
                main_menu_obj.display_menu()

    """
    Display the menu for user registration.

    This function prompts the user to enter their name, password, and account saving type.
    It validates the input and stores the user's information in the `account` dictionary.

    If the user's information is valid, it creates a `Bank` object with the account information and
    calls the `processed_registered_data` method to process the registered data.

    If the registration is successful, it calls the `display_menu` method of the `LoginApplicationMenu` class.
    Otherwise, it calls the `prompt_user_back_to_menu` method of the current class.

    Parameters:
        self: The instance of the class.

    Returns:
        None

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a function called display_menu that prompts
    the user for input related to creating an account.

    It checks the validity of the user's input, such as the name, password, and account saving type.
    If the input is valid, it proceeds to create an account and display a success message.
    If the input is invalid, it displays a warning message and prompts the user to input again.
    """
    def display_menu(self):
        account = {}
        check_data_input_is_valid = False

        while check_data_input_is_valid is False:
            check_data_input_is_valid = True

            print(const.LOGO_MENU_PAGE)
            print(const.REGISTER_MENU_PAGE)
            print("What is your NAME?\n"
                  "TYPE YOUR NAME!")

            account[const.ACC_NAME_KEY] = (input("[At least 4 CHARACTERS & ONLY ALPHABET (with/no SPACE) "
                                                 "(Case-insensitive)!]: ")
                                           .title().strip())

            account[const.ACC_NAME_KEY] = ' '.join(account[const.ACC_NAME_KEY].split())
            temp_account_name_key = account[const.ACC_NAME_KEY].replace(" ", "")

            if len(temp_account_name_key) < 4:
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_STRING_OUT_OF_RANGE_INPUT_WARN} "
                      f"3 CHARACTERS{const.WARNING_TEXT_2}")

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

            elif not temp_account_name_key.isalpha():
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_STRING_INPUT_WARN}{const.WARNING_TEXT_2}")

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

        print(f"\n{const.SUCCESS_TEXT_1}HELLO {account[const.ACC_NAME_KEY]}, NICE TO KNOW YOU!{const.SUCCESS_TEXT_2}")

        check_data_input_is_valid = False

        while check_data_input_is_valid is False:
            check_data_input_is_valid = True

            system_time.sleep(1)

            print(const.PAGING_MENU_JUMP)
            print(const.LOGO_MENU_PAGE)
            print(const.REGISTER_MENU_PAGE)
            print("What is your PASSWORD?\n"
                  "TYPE YOUR PASSWORD!")

            account[const.ACC_PASS_KEY] = input("[At least 5 CHARACTERS (Case-sensitive)!]: ")

            if len(account[const.ACC_PASS_KEY]) < 5:
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_STRING_OUT_OF_RANGE_INPUT_WARN} 4 CHARACTERS"
                      f"{const.WARNING_TEXT_2}")

        print(f"\n{const.SUCCESS_TEXT_1}OKAY!\n"
              f"YOUR PASSWORD HAS BEEN SET UP!{const.SUCCESS_TEXT_2}")

        check_data_input_is_valid = False

        while check_data_input_is_valid is False:
            check_data_input_is_valid = True

            system_time.sleep(1)

            print(const.PAGING_MENU_JUMP)
            print(const.LOGO_MENU_PAGE)
            print(const.REGISTER_MENU_PAGE)
            print("What do you want for your ACCOUNT SAVING TYPE?")
            print(const.LIST_OF_ACC_SAVING_TYPE_MENU_LIST)
            print("")
            print("TYPE YOUR CHOICE [1 to 2]!")

            account[const.ACC_SAVING_TYPE_KEY] = input(const.USER_INPUT_ONLY_NUMBER)

            if not account[const.ACC_SAVING_TYPE_KEY].isnumeric():
                check_data_input_is_valid = False

                print(const.WARNING_TEXT_1 + const.INVALID_USER_NUMBER_INPUT_WARN + const.WARNING_TEXT_2)

            elif not (1 <= int(account[const.ACC_SAVING_TYPE_KEY]) <= len(const.LIST_OF_ACC_SAVING_TYPE)):
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_NUMBER_OUT_OF_RANGE_INPUT_WARN} 1 to "
                      f"{len(const.LIST_OF_ACC_SAVING_TYPE)}"
                      f"{const.WARNING_TEXT_2}")

        acc_save_index = int(account[const.ACC_SAVING_TYPE_KEY]) - 1

        print(f"\n{const.SUCCESS_TEXT_1}SO YOU CHOOSE {const.LIST_OF_ACC_SAVING_TYPE[acc_save_index]}!\n"
              f"OKAY!{const.SUCCESS_TEXT_2}")

        account[const.ACC_SAVING_TYPE_KEY] = const.LIST_OF_ACC_SAVING_TYPE[acc_save_index]

        user_account_bank_obj = Bank(account)
        res_registered_user_account = user_account_bank_obj.processed_registered_data()

        if res_registered_user_account is True:
            system_time.sleep(1)

            print(const.PAGING_MENU_JUMP)

            login_menu_obj = LoginApplicationMenu()
            login_menu_obj.display_menu()

        else:
            system_time.sleep(1)

            self.prompt_user_back_to_menu()


class MainApplicationMenu(BaseMenu):
    """
    Displays the main menu to the user and handles the user's input.

    Args:
        self: The object instance.

    Returns:
        None.

    ==================================================================================================================

    The explanation of the code snippet:

    This code snippet defines a function called display_menu that prompts the user to input a choice from a menu.
    It checks if a specific file exists and displays different menu options accordingly.

    The user's input is validated to ensure it is a number within a certain range.
    Depending on the user's input and the existence of the file, different actions are taken,
    such as displaying additional menus or quitting the program.
    """
    def display_menu(self):
        local_export_file_path = const.LOCAL_FOLDER_EXPORT_FILE_PATH + const.EXCEL_USER_ACC_LIST

        user_main_menu_input = ''
        check_data_input_is_valid = False

        while check_data_input_is_valid is False:
            check_data_input_is_valid = True

            print(const.LOGO_MENU_PAGE)
            print(const.WELCOMING_MENU_PAGE)

            if os.path.exists(local_export_file_path):
                print(const.LIST_OF_MAIN_MENU_INPUT_VER_2)
                print("TYPE YOUR CHOICE [from 1 to 3]!")

            else:
                print(const.LIST_OF_MAIN_MENU_INPUT_VER_1)
                print("TYPE YOUR CHOICE [from 1 to 2]!")

            user_main_menu_input = input(const.USER_INPUT_ONLY_NUMBER)

            if not user_main_menu_input.isnumeric():
                check_data_input_is_valid = False

                print(const.WARNING_TEXT_1 + const.INVALID_USER_NUMBER_INPUT_WARN + const.WARNING_TEXT_2)

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

            elif os.path.exists(local_export_file_path) and not (1 <= int(user_main_menu_input) <= 3):
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_NUMBER_OUT_OF_RANGE_INPUT_WARN} 1 to 3"
                      f"{const.WARNING_TEXT_2}")

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

            elif not os.path.exists(local_export_file_path) and not (1 <= int(user_main_menu_input) <= 2):
                check_data_input_is_valid = False

                print(f"{const.WARNING_TEXT_1}{const.INVALID_USER_NUMBER_OUT_OF_RANGE_INPUT_WARN} 1 to 2"
                      f"{const.WARNING_TEXT_2}")

                system_time.sleep(1)

                print(const.PAGING_MENU_JUMP)

        if os.path.exists(local_export_file_path):
            print(f"\nWILL BE DIRECTED TO {const.LIST_OF_MAIN_MENU_VER_2[int(user_main_menu_input) - 1]} ASAP!")

        else:
            print(f"\nWILL BE DIRECTED TO {const.LIST_OF_MAIN_MENU_VER_1[int(user_main_menu_input) - 1]} ASAP!")

        if os.path.exists(local_export_file_path):
            match int(user_main_menu_input):
                case 1:
                    system_time.sleep(1)

                    print(const.PAGING_MENU_JUMP)

                    register_menu_obj = RegisterApplicationMenu()
                    register_menu_obj.display_menu()

                case 2:
                    system_time.sleep(1)

                    print(const.PAGING_MENU_JUMP)

                    login_menu_obj = LoginApplicationMenu()
                    login_menu_obj.display_menu()

                case 3:
                    system_time.sleep(1)

                    print(const.PAGING_MENU_JUMP)
                    print(const.LOGO_QUIT_PAGE)
                    print(const.QUIT_MENU_PAGE)

                    system_time.sleep(2)

                    quit(code=None)

        else:
            match int(user_main_menu_input):
                case 1:
                    system_time.sleep(1)

                    print(const.PAGING_MENU_JUMP)

                    register_menu_obj = RegisterApplicationMenu()
                    register_menu_obj.display_menu()

                case 2:
                    system_time.sleep(1)

                    print(const.PAGING_MENU_JUMP)
                    print(const.LOGO_QUIT_PAGE)
                    print(const.QUIT_MENU_PAGE)

                    system_time.sleep(2)

                    quit(code=None)


if __name__ == '__main__':
    menu_obj = MainApplicationMenu()
    menu_obj.display_menu()
