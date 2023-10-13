CREATOR_NAME = "Daniel Albesta"

PAGING_MENU_JUMP = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

LOGO_MENU_PAGE = \
    '''                                              
,-----.    ,---.  ,--.  ,--.,--. ,--.      ,---.  ,-----.   ,-----. 
|  |) /_  /  O  \\ |  ,'.|  ||  .'   /     /  O  \\ |  |) /_ '  .--./ 
|  .-.  \\|  .-.  ||  |' '  ||  .   '     |  .-.  ||  .-.  \\|  |     
|  '--' /|  | |  ||  | `   ||  |\\   \\    |  | |  ||  '--' /'  '--'\\ 
`------' `--' `--'`--'  `--'`--' '--'    `--' `--'`------'  `-----' 
'''

LOGO_QUIT_PAGE = \
    '''
                                                                    ,---. 
 ,----.    ,-----.  ,-----. ,------.      ,-----.,--.   ,--.,------.|   | 
'  .-./   '  .-.  ''  .-.  '|  .-.  \\     |  |) /_\\  `.'  / |  .---'|  .' 
|  | .---.|  | |  ||  | |  ||  |  \\  :    |  .-.  \'.    /  |  `--, |  |  
'  '--'  |'  '-'  ''  '-'  '|  '--'  /    |  '--' /  |  |   |  `---.`--'  
 `------'  `-----'  `-----' `-------'     `------'   `--'   `------'.--.  
                                                                    '--'  
'''

SUCCESS_TEXT_1 = "\033[1;37;32m"
SUCCESS_TEXT_2 = "\033[0;0m"

WARNING_TEXT_1 = "\033[1;37;31m"
WARNING_TEXT_2 = "\033[0;0m"

WELCOMING_MENU_PAGE = ("======================================================================\n"
                       "HELLO, WELCOME TO DANIEL ALBESTA's SIMPLE BANK MANAGEMENT SYSTEM MENU!\n"
                       "======================================================================\n")

QUIT_MENU_PAGE = ("======================================================================\n"
                  "THANKS FOR SPENDING A TIME WITH MY SIMPLE PROGRAM!\n"
                  "HAVE A NICE DAY!\n"
                  "======================================================================")

REGISTER_MENU_PAGE = ("========================================================================\n"
                      "HELLO USER! THIS IS REGISTER MENU PAGE!\n"
                      "========================================================================\n")

LOGIN_MENU_PAGE = ("========================================================================\n"
                   "HELLO USER! THIS IS LOGIN MENU PAGE!\n"
                   "========================================================================\n")

BANK_MENU_PAGE = ("========================================================================\n"
                  "HELLO USER! THIS IS BANK MENU PAGE!\n"
                  "========================================================================\n")

QUIT_BANK_MENU_PAGE = ("======================================================================\n"
                       "THANKS FOR THE TRANSACTION YOU HAVE MAKE!\n"
                       "HAVE A NICE DAY!\n"
                       "======================================================================")

LIST_OF_MAIN_MENU_INPUT_VER_1 = ("\nCHOOSE:\n\n"
                                 "1. REGISTER NEW ACCOUNT\n"
                                 "2. QUIT THE PROGRAM\n\n")

LIST_OF_MAIN_MENU_INPUT_VER_2 = ("\nCHOOSE:\n\n"
                                 "1. REGISTER NEW ACCOUNT\n"
                                 "2. LOGIN EXISTING ACCOUNT\n"
                                 "3. QUIT THE PROGRAM\n\n")

LIST_OF_MAIN_MENU_VER_1 = ["REGISTER", "QUIT"]
LIST_OF_MAIN_MENU_VER_2 = ["REGISTER", "LOGIN", "QUIT"]

LIST_OF_ACC_SAVING_TYPE_MENU_LIST = ("\nCHOOSE:\n\n"
                                     "1. CONVENTIONAL SAVING\n"
                                     "2. SHARIA SAVING\n\n")

LIST_OF_MENU_TYPE = ["MENU_VER_1", "MENU_VER_2"]

LIST_OF_ACC_SAVING_TYPE_MENU_INPUT_VER_1 = ("\nCHOOSE:\n\n"
                                            "1. CASH DEPOSIT\n"
                                            "   [Add the given amount to the account balance]\n"
                                            "2. CASH WITHDRAWAL\n"
                                            "   [Deduct the given amount from the account balance]\n"
                                            "3. LOGOUT\n"
                                            "   (back to main menu)\n")

LIST_OF_ACC_SAVING_TYPE_MENU_INPUT_VER_2 = ("\nCHOOSE:\n\n"
                                            "1. CASH DEPOSIT\n"
                                            "   [Add the given amount to the account balance]\n"
                                            "2. LOGOUT\n"
                                            "   (back to main menu)\n")

LIST_OF_ACC_SAVING_TYPE_MENU = ["DEPOSIT", "WITHDRAWAL", "LOGOUT"]

NO_DATA_AVAILABLE = WARNING_TEXT_1 + "NO DATA ARE AVAILABLE YET!" + WARNING_TEXT_2

USER_INPUT_ONLY_NUMBER = "[ONLY NUMERIC!]: "

SAVING_TYPE_MENU_PAGE_LINE = "************************************************************************"

MAIN_MENU_TITLE = "MENU"
REGISTER_MAIN_MENU_TITLE = "REGISTER"
LOGIN_MAIN_MENU_TITLE = "LOGIN"

ACC_CONVENTIONAL_SAVING_ID = 'C'
ACC_SHARIA_SAVING_ID = 'S'

LIST_OF_ACC_SAVING_TYPE = ["Conventional", "Sharia"]

ACC_CONVENTIONAL_SAVING_TYPE = "Conventional"
ACC_SHARIA_SAVING_TYPE = "Sharia"

DEF_ACC_BALANCE_DATA = 0
DEF_ACC_TRANSACT_HIST_DATA = []

DATE_FORMAT = "%y-%m-%d"
DATETIME_FORMAT = "%y-%m-%d %H:%M:%S"

DEF_ACC_NUMBER_LEADING_ZEROS = 1
LIMIT_MIN_ACC_AMT_BALANCE = 10000.0
CONVENTIONAL_SAVING_TYPE_INTEREST_RATE = 4.0
SHARIA_SAVING_TYPE_INTEREST_RATE = 0.0
MIN_DEPOSIT_AMT = 10000
MIN_WITHDRAW_AMT = 10000

ACC_SAVING_TYPE_KEY = "account_saving_type"
ACC_DATE_KEY = "date"
ACC_NUMBER_KEY = "account_number"
ACC_NAME_KEY = "account_name"
ACC_PASS_KEY = "account_password"
ACC_INTEREST_RATE_KEY = "interest_rate"
ACC_TRANSACT_HIST_KEY = "transact_hist"
ACC_MIN_BALANCE_KEY = "min_balance"
ACC_DETAIL_KEY = "detail_information"
ACC_STATUS_KEY = "transaction_status"
ACC_BALANCE_BEFORE_KEY = "balance_before"
ACC_BALANCE_KEY = "balance"
ACC_TIME_KEY = "transaction_time"
ACC_STUDENT_KEY = "student"
ACC_SPREADSHEET_KEY = "spreadsheet_name"

ACC_AMT_BALANCE_INCREMENT = "balance_amount_increasing_by"
ACC_AMT_BALANCE_DECREMENT = "balance_amount_decreasing_by"

EXCEL_FILE_CREATED_SUCCESSFULLY = "EXCEL FILE CREATED SUCCESSFULLY!"
EXCEL_FILE_UPDATED_SUCCESSFULLY = "EXCEL FILE UPDATED SUCCESSFULLY!"
GDOC_FILE_UPDATED_SUCCESSFULLY = "GDOC FILE UPDATED SUCCESSFULLY!"

USER_ACC_EXISTS_ERROR = "USER ACCOUNT IS ALREADY EXISTS!"
USER_ACC_NAME_AND_PASS_NOT_FOUND_ERROR = "USER ACCOUNT NAME AND PASSWORD NOT FOUND!"

ACC_TRUE_PENALTY = "PENALTY"
ACC_FALSE_PENALTY = "NO PENALTY"

ACC_DEPOSIT_STAT = "Deposit"
ACC_DEPOSIT_ERROR_STAT = "Error_Deposit"

ACC_WITHDRAW_STAT = "Withdraw"
ACC_WITHDRAW_ERROR_STAT = "Error_Withdraw"

INVALID_USER_NUMBER_INPUT_WARN = "INVALID DATA TYPE, MUST BE IN NUMBER!"
INVALID_USER_STRING_INPUT_WARN = "INVALID DATA TYPE, MUST BE IN ALPHABET!"
INVALID_USER_NUMBER_OUT_OF_RANGE_INPUT_WARN = "INVALID NUMERIC RANGE DATA! MUST BE IN RANGE:"
INVALID_USER_STRING_OUT_OF_RANGE_INPUT_WARN = "INVALID STRING DATA TYPE! MUST BE MORE THAN:"
INVALID_USER_ACC_NUMBER_WARN = "INVALID USER ACCOUNT NUMBER"
ACC_AMT_BALANCE_PENALTY_WARN = "USER ACCOUNT AMOUNT BALANCE HAS REACH BELOW MINIMUM BALANCE!"
ACC_SAVING_WITHDRAW_BANNED_WARN = "YOU CANNOT DOING ANY WITHDRAW WITH YOUR CURRENT AMOUNT BALANCE NOW!"
ACC_SAVING_DEPOSIT_SOME_AMT_BALANCE_FIRST_WARN = "YOU MUST DEPOSIT SOME AMOUNT FIRST TO YOUR ACCOUNT!"
LIMIT_MIN_ACC_AMT_BALANCE_WARN = "USER ACCOUNT AMOUNT BALANCE HAS REACH LIMIT MINIMUM BALANCE!"
INSUFFICIENT_AMT_BALANCE_WARN = "INSUFFICIENT AMOUNT BALANCE!"

CREDENTIALS_FILE_NAME_PATH = "resource_files/google_secret.json"
CREDENTIALS_SCOPE_URl = ["https://www.googleapis.com/auth/spreadsheets"]

# noinspection SpellCheckingInspection
CREDENTIALS_SHEET_KEY = "1ojN5IITl16HRFvXFrKuEJQOzpjr5L-vu2dZQ_lKTVJg"

LOCAL_FOLDER_EXPORT_FILE_PATH = "export_files/"

EXCEL_USER_ACC_LIST = "user_account_list.xlsx"
EXCEL_USER_ACC_TRANSACTION_HISTORY = "user_account_transaction_history.xlsx"
EXCEl_FILE_ENGINE = "openpyxl"
EXPORT_EXCEL_VALUE_INPUT_OPTION = "USER_ENTERED"
EXPORT_EXCEL_USER_ACCOUNT_SHEET = "user_account"
EXPORT_EXCEL_FILE_TRANSACTION_SHEET = "Transaction"
EXPORT_EXCEL_FILE_CONVENTIONAL_SHEET = "Conventional"
EXPORT_EXCEL_FILE_SHARIA_SHEET = "Sharia"

FILE_PERMISSION_ERROR_HANDLER_ERROR = (WARNING_TEXT_1 + "REQUESTED FILE FOR ACCESS PERMISSION IS DENIED, REALLY SORRY!"
                                       + WARNING_TEXT_2)
FILE_PERMISSION_NOT_FOUND_HANDLER_ERROR = (WARNING_TEXT_1 + "REQUESTED FILE IS NOT FOUND, REALLY SORRY!"
                                           + WARNING_TEXT_2)
