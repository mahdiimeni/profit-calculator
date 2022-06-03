class Calc:
    def __init__(self, profit_percentage, days, first_trade_volume):
        self.percent = profit_percentage
        self.days = days
        self.fund = first_trade_volume

    def cp_calc(self):
        cp_equation = ((1 + (self.percent / 100)) ** self.days) * self.fund
        return f" ---> your profit after '{self.days}' days is '{round(cp_equation)}'$"

    def fix_profit_calc(self):
        percent_equation = (self.fund * self.percent) / 100
        fix_equation = percent_equation * self.days
        return f" ---> your profit after '{self.days}' days is '{round(fix_equation)}'$"