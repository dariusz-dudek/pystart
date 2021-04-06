work_experience = float(input('Work experience in years: '))
hours = int(input('Hours worked            : '))
goods = int(input('Numbers of goods sold   : '))
salary = 2000.0

seniority = salary * 0.1 if work_experience > 2 else salary * (work_experience * 0.02)
bonus_for_sale = salary * 0.25 if goods >= 30 else 0
for_active = salary * 0.08 if hours > 160 and work_experience > 1 else salary * 0.02

print(f'Your salary is:\n'
      f'Basic salary    : {salary:,.2f}\n'
      f'Seniority       : {seniority:,.2f}\n'
      f'Bonus for sale  : {bonus_for_sale:,.2f}\n'
      f'Bonus for active: {for_active:,.2f}\n'
      f'SUM             : {salary + seniority + bonus_for_sale + for_active:,.2f}\n')


