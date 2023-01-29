import datetime 
import csv 
import pandas as pd
#parameter headers of data
header=['date','time','expenses','alert']
#name of file . file must be already genrated..
filename='expenses.csv'

#with open(filename,'w') as file:
#open the csv file in append mode 
with open(filename,'a+',newline='') as file:
   #input total amount spend today
   expenses=int(input('Enter your expenses today:'))
   #day
   today = datetime.date.today()
   date=today.strftime('%d/%m/%Y')
   #time
   now = datetime.datetime.now()
   time=now.strftime("%I:%M:%S")
   #check alert 
   if expenses>200:
      alert=1
   else:
      alert=0
   total_expenses=0
   #create a data list
   data=[date,time,expenses,alert]
   #open the file and check if the given data already exist
   df = pd.read_csv(filename)  
   for i in range(len(df)):
  
      if df.loc[i,"date"]==date:
         #if exist update it with new data
         df.loc[i]=data
         #write to the file
         df.to_csv(filename, index=False)
         print("data updated")
         #quit the program excution 
         quit()
   #append dat to the file
   writer_object = csv.writer(file)
   writer_object.writerow(data)
   file.close()
   


    
