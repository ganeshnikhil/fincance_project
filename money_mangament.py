import datetime
import pandas as pd
import os 

# Name of the CSV file. The file must already exist.
filename = 'expenses.csv'
#header = {'date': None, 'time': None, 'expenses': None, 'alert': None}
header = 'date,time,expenses,alert\n'
if os.path.exists(filename):
   pass
else:
    with open(filename,'w') as file:
        file.write(header)
       
        
# Input total amount spent today
try:
    expenses = int(input('Enter your expenses today:'))
except ValueError:
    print("Invalid input. Please enter a valid integer for expenses.")
    quit()

# Day
today = datetime.date.today()
date = today.strftime('%d/%m/%Y')

# Time
now = datetime.datetime.now()
time = now.strftime("%I:%M:%S")

# Check alert
alert = 1 if expenses > 200 else 0

# Create a data dictionary
data = {'date': [date], 'time': [time], 'expenses': [expenses], 'alert': [alert]}

try:
    # Read the CSV file into a DataFrame
   df = pd.read_csv(filename)

    # Check if the given date already exists in the DataFrame
   if date in df['date'].values:
        # Update the existing data for the given date
      df.loc[df['date'] == date, ['time', 'expenses', 'alert']] = time, expenses, alert
      print("[+] Data updated")
   else:
       # Append the new data to the DataFrame
       df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
       print("[-] Data updated")

    # Write the updated DataFrame back to the CSV file
   df.to_csv(filename, index=False)
except FileNotFoundError:
    print("File not found. Please ensure the file exists before running the script.")
except Exception as e:
    print(f"An error occurred: {e}")
