# Program to calculate gross salary of employee


basic_salary = float(input("Enter the basic salary: "))


hra = 0.15 * basic_salary
da = 0.1 * basic_salary
gross_salary = basic_salary + hra + da

print(f"Gross Salary: {gross_salary}")
