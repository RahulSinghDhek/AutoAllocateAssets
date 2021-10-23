from enum import Enum


class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


# COMMANDS
ALLOCATE = "ALLOCATE"
SIP = "SIP"
CHANGE = "CHANGE"
BALANCE = "BALANCE"
REBALANCE = "REBALANCE"

# OUTPUT MESSAGES
CANNOT_REBALANCE = "CANNOT_REBALANCE"

# ERROR MESSAGES
PATH_ERROR = "Please provide path to input file"
FILE_ERROR = "Could not open the file"
ALLOCATION_FAILED = "Allocation of fund failed for {} command for the values {}"
SIP_FAILED = "Please check and verify the amounts for {} command for the values {}"
CHANGE_FAILED = "Failed to input interest rate change for {} inputs with value {}"
INPUT_PARSE_FAILED = "Failed to parse the {} inputs"
NO_SIP_AMOUNT = "No SIP amount find, Please check the input"

# WARNING
INVALID_COMMAND = "Invalid Command"
TWICE_ALLOCATION = "Trying to allocate more than once. Check the {} command"
