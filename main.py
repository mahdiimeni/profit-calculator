# Compound and Fix Profit Calculator

from calc_brain import Calc

percent = float(input("% > "))
trade_days = int(input("Days > "))
initial_fund = float(input("$ > "))
choice = input("Compound profit or Fix profit? (C or F): ").lower()

calculator = Calc(percent, trade_days, initial_fund)

if choice == "c":
    print(calculator.cp_calc())
else:
    print(calculator.fix_profit_calc())
