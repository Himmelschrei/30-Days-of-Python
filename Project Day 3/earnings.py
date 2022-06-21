name = ((input("Please enter employee's name: ")).strip()).title()
h_wage = float(input("Please enter their hour wage: "))
h_week = float(input("Please enter their worked hourse this week: "))

w_wage = h_week * h_wage

print(f"{name} earned ${w_wage} this week.")