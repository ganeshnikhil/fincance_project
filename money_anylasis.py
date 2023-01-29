import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style  
filename='expenses.csv'
df = pd.read_csv(filename)  
month=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
modic={'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0]}

expenses=[]
risk=0
for i in range(len(df)):
   date=df.loc[i,"date"].split('/')
   #append daily espenses to expenses list ..
   expenses.append(int(df.loc[i,'expenses']))
   #add the expeneses
   modic[date[1]][0]+=int(df.loc[i,'expenses'])
   #add risk factor 
   modic[date[1]][1]+=int(df.loc[i,'alert'])



spend=[]
for key in modic.keys():
   #print montly expenses..
   print(f"{month[int(key)-1]}::{modic[key][0]}-->{modic[key][1]}")
   #and append monthly expenses to spend list..
   spend.append(modic[key][0])
# one month is equal 30 days so 1 unit=n/30
day=[i/30 for i in range(1,len(expenses)+1)]

style.use('ggplot')  
plt.title('''Monthly Expenses
         1day=0.3.. & 1month=30days''') 
plt.xlabel('Day and month-->')
plt.ylabel('Expenses-->')
plt.plot(day,expenses,'r',label='daily_exp',linewidth=0.5)
plt.plot(month,spend,'^k:',label='montly_exp',linewidth=1.5)
#^k:
plt.legend()
plt.grid(True, color='k')  
plt.show()   
 