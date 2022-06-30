# -*-*- Compound and Fixed Profit Calculator

from calc_brain import Calc


calculator_is_on = True
while calculator_is_on:
    # --- Percentage of desired daily profit.
    percentage = float(input("% > "))

    # --- Number of working days.
    trade_days = int(input("Days > "))

    # --- The first amount of the transaction.
    first_amount = float(input("$ > "))

    usr_choice = input("Compound profit or Fixed profit? (C or F): ").lower()

    calculator = Calc(percentage, trade_days, first_amount)

    if usr_choice == "c":
        print(calculator.compound_profit_calc())
    else:
        print(calculator.fixed_profit_calc())

    calc_off = input("Would you like to continue? (Y or N): ").lower()
    if calc_off == "n":
        calculator_is_on = False
