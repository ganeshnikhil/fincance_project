import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style  

filename = 'expenses.csv'
df = pd.read_csv(filename)
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

monthly_data = {'01': [0, 0], '02': [0, 0], '03': [0, 0], '04': [0, 0], '05': [0, 0], '06': [0, 0],
                '07': [0, 0], '08': [0, 0], '09': [0, 0], '10': [0, 0], '11': [0, 0], '12': [0, 0]}

expenses = []
risk = 0

for i in range(len(df)):
    month_key = df.loc[i, 'date'].strftime('%m')
    # Append daily expenses to expenses list.
    expenses.append(int(df.loc[i, 'expenses']))
    # Add the expenses to monthly_data.
    monthly_data[month_key][0] += int(df.loc[i, 'expenses'])
    # Add the risk factor to monthly_data.
    monthly_data[month_key][1] += int(df.loc[i, 'alert'])

print('Month::Expenses-->Alert')
for key, value in monthly_data.items():
    month_number = int(key)
    total_expenses = value[0]
    risk_factor_count = value[1]
    print(f"{month_number:02d}::{total_expenses}-->{risk_factor_count}")

monthly_expenses = [monthly_data[key][0] for key in monthly_data.keys()]
risk_factor = [monthly_data[key][1] for key in monthly_data.keys()]

# One month is equal to 30 days, so 1 unit = n/30
day = [i / 30 for i in range(1, len(expenses) + 1)]

style.use('ggplot')  
plt.title('Monthly Expenses\n1 day = 0.3 & 1 month = 30 days') 
plt.xlabel('Time (Months)')  # You can customize this label further if needed
plt.ylabel('Amount (in dollars)')  # Customize the y-axis label
plt.plot(day, expenses, 'r', label='Daily Expenses', linewidth=0.5)
plt.plot(monthly_data.keys(), monthly_expenses, '^k:', label='Monthly Expenses', linewidth=1.5)
plt.plot(monthly_data.keys(), risk_factor, 'b--', label='Risk Factor', linewidth=1.5)  # Adding risk factor to plot
plt.legend()
plt.grid(True, color='k')  
plt.show()  
