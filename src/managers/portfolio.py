from src.util import constants


class Portfolio:
    month_map = {}

    def __init__(self, amount):
        self.sip_count = 1
        self.amount = amount
        self.rebalanced_amount = None

    def add_sip_amount(self, amount, month):
        self.sip_count += 1
        if amount:
            self.amount.equity += amount.equity
            self.amount.debt += amount.debt
            self.amount.gold += amount.gold
            self.amount.convertToInt()
            self.month_map[month] = Amount(self.amount.equity, self.amount.debt, self.amount.gold)

    def update_with_interest(self, interest, month):
        self.amount.equity += (interest.equity * self.amount.equity / 100)
        self.amount.debt += (interest.debt * self.amount.debt / 100)
        self.amount.gold += (interest.gold * self.amount.gold / 100)
        self.amount.convertToInt()
        self.month_map[month] = Amount(self.amount.equity, self.amount.debt, self.amount.gold)

    def get_balance(self, month):
        return self.month_map[month]

    def rebalance(self):
        if self.sip_count % 6 == 0:
            amount = self.month_map.get(constants.Month(self.sip_count).name)
            total_amount = amount.equity + amount.debt + amount.gold
            amount.equity = 0.6 * total_amount
            amount.debt = 0.3 * total_amount
            amount.gold = 0.1 * total_amount
            self.month_map[constants.Month(self.sip_count).name] = Amount(self.amount.equity, self.amount.debt,
                                                                          self.amount.gold)
            self.rebalanced_amount = amount

    def get_rebalance(self):
        if self.sip_count < 6:
            print(constants.CANNOT_REBALANCE)
            return None
        return self.rebalanced_amount


class Interest:
    def __init__(self, equity, debt, gold):
        self.equity = equity
        self.debt = debt
        self.gold = gold


class Amount:
    def __init__(self, equity, debt, gold):
        self.equity = equity
        self.debt = debt
        self.gold = gold

    def convertToInt(self):
        self.equity = int(self.equity)
        self.debt = int(self.debt)
        self.gold = int(self.gold)

    def display(self):
        print("{} {} {}".format(self.equity, self.debt, self.gold))
