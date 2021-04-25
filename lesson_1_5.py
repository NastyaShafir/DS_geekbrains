income = int(input("Please enter your company income: "))
costs = int(input("Please enter your company's costs: "))
if income > costs:
    profit = income - costs
    print("Your income is more than costs", profit / income)
    n = int(input("Please enter number of employees: "))
    # print("Your profir per one worker is", str(profit / n + '$'))
    print(f"Your profir per one worker is {round(profit / n, 2)}$")
else:
    print("Your income is less than costs", costs - income)
    