# Task:salary calculation:-

base_salary=50000
bonus=5000
tax_rate=10 # percentage
other_charges=2000
one_day_salary=base_salary/30
gross_salary=base_salary+bonus
gross_salary_tax= (tax_rate/100) * gross_salary
net_salary=gross_salary-gross_salary_tax-other_charges
print(f"Gross salary : {gross_salary}")
print(f"Gross salary tax : {gross_salary_tax}")
print(f"Net salary : {net_salary}")
print(f"One day salary : {one_day_salary}")
    



