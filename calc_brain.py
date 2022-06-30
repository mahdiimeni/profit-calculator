class Calc:
    def __init__(self, profit_percentage, days, first_trade_amount):
        self.percentage = profit_percentage
        self.days = days
        self.fund = first_trade_amount

    def compound_profit_calc(self):
        cp_equation = ((1 + (self.percentage / 100)) ** self.days) * self.fund
        return f" ---> your profit after '{self.days}' days is '{round(cp_equation)}'$"

    def fixed_profit_calc(self):
        percentage_equation = (self.fund * self.percentage) / 100
        fixed_equation = percentage_equation * self.days
        return f" ---> your profit after '{self.days}' days is '{round(fixed_equation)}'$"
