from src.util import constants, log, utility
from src.managers.portfolio import Portfolio, Amount, Interest
logger = log.Logger()


class AssetAllocator():
    def __init__(self, portfolio, input_array):
        self.portfolio = portfolio
        self.input_array = input_array
        self.sip_amount = None
        self.initial_amount = None
        self.month_count = 1
        self.allocation_done = False
        self.sip_amount_noted = False

    def startSelfAllocation(self):
        for statement in self.input_array:
            split_value = statement.split()
            if not split_value:
                continue
            command = split_value[0]
            if command == constants.ALLOCATE:
                if not self.calculateAllocation(split_value):
                    return

            elif command == constants.SIP:
                if not self.calculateSip(split_value):
                    return

            elif command == constants.CHANGE:
                if not self.calculateChange(split_value):
                    return

            elif command == constants.BALANCE:
                self.balance(split_value)

            elif command == constants.REBALANCE:
                self.reBalance()
            else:
                logger.warning(constants.INVALID_COMMAND)

    def calculateSip(self, split_value, command=constants.SIP):
        if len(split_value) < 4:
            logger.error(
                constants.SIP_FAILED.format(command, str(split_value)))
            return False

        sip_values_list = utility.convertToInt(split_value[1:])
        if sip_values_list:
            self.sip_amount = Amount(sip_values_list[0], sip_values_list[1], sip_values_list[2])
        else:
            logger.error(constants.INPUT_PARSE_FAILED.format(command))
            return False
        self.sip_amount_noted = True
        return True

    def calculateAllocation(self, split_value, command=constants.ALLOCATE):
        if self.allocation_done:
            logger.warning(constants.TWICE_ALLOCATION.format(command))
            return True
        if len(split_value) < 4:
            logger.error(constants.ALLOCATION_FAILED.format(command, str(split_value)))
            return False
        initial_values_list = utility.convertToInt(split_value[1:])
        if initial_values_list:
            self.initial_amount = Amount(initial_values_list[0], initial_values_list[1], initial_values_list[2])
        else:
            logger.error(constants.INPUT_PARSE_FAILED.format(command))
            return False
        self.initial_amount.convertToInt()
        self.portfolio = Portfolio(self.initial_amount)
        self.allocation_done = True
        return True

    def calculateChange(self, split_value, command=constants.CHANGE):
        if not self.sip_amount_noted:
            logger.error(constants.NO_SIP_AMOUNT)
            return False
        if len(split_value) < 5:
            logger.error(constants.CHANGE_FAILED.format(command, str(split_value)))
            return False
        month = split_value[4]
        if month.upper() not in constants.Month.__members__:
            logger.error(constants.CHANGE_FAILED.format(command, str(split_value)))
            return False
        interest_rate_values = utility.convertInterestRatesToFloat(split_value[1:4])
        if interest_rate_values:
            interest = Interest(interest_rate_values[0], interest_rate_values[1], interest_rate_values[2])
            if self.month_count == 1:
                self.portfolio.update_with_interest(interest, constants.Month(self.month_count).name)
            else:
                self.portfolio.add_sip_amount(self.sip_amount, constants.Month(self.month_count).name)
                self.portfolio.update_with_interest(interest, month)
        else:
            logger.error(constants.INPUT_PARSE_FAILED.format(command))
            return False

        if self.month_count % 6 == 0:
            self.portfolio.rebalance()
        self.month_count += 1
        return True

    def balance(self, split_value):
        balance_amount = self.portfolio.get_balance(split_value[1])
        balance_amount.convertToInt()
        print(balance_amount.equity, balance_amount.debt, balance_amount.gold)

    def reBalance(self):
        rebalanced_amount = self.portfolio.get_rebalance()
        if rebalanced_amount:
            rebalanced_amount.convertToInt()
            rebalanced_amount.display()
