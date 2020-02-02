import matplotlib.pyplot as plt 
import csv
from datetime import datetime

file_ca = open("death_valley_2018_simple.csv","r")
file_ak = open("sitka_weather_2018_simple.csv","r")

csv_file_ca = csv.reader(file_ca, delimiter=",")
csv_file_ak = csv.reader(file_ak, delimiter=",")

header_row_ca = next(csv_file_ca)
header_row_ak = next(csv_file_ak)

highs_ak = []
dates_ak = []
lows_ak = []
for index,column_header in enumerate(header_row_ak):
    if column_header == "NAME":
        name_index = index
    if column_header == "DATE":
        date_index = index
    if column_header == "TMAX":
        max_index = index
    if column_header == "TMIN":
        min_index = index

for row in csv_file_ak:
    title_ak = row[name_index]
    highs_ak.append(int(row[max_index]))                                
    lows_ak.append(int(row[min_index]))                                  
    current_date = datetime.strptime(row[date_index],'%Y-%m-%d')
    dates_ak.append(current_date)


highs_ca = []
dates_ca = []
lows_ca = []
for index,column_header in enumerate(header_row_ca):
    if column_header == "NAME":
        name_index1 = index
    if column_header == "DATE":
        date_index1 = index
    if column_header == "TMAX":
        max_index1 = index
    if column_header == "TMIN":
        min_index1 = index

for row_1 in csv_file_ca:
    title_ca = row[name_index1]
    try:
        high_1 = int(row_1[max_index1])
        low_1 = int(row_1[min_index1])
        current_date_1 = datetime.strptime(row_1[date_index1],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date_1}")
    else:
        highs_ca.append(high_1)                                
        lows_ca.append(low_1)
        dates_ca.append(current_date_1)



fig,(ax,ax1) = plt.subplots(2,1)

ax.plot(dates_ak,highs_ak,color='red')
ax.plot(dates_ak,lows_ak,color='blue')
ax.fill_between(dates_ak,highs_ak,lows_ak,facecolor='blue',alpha=0.3)
ax.set_title(title_ak)


ax1.plot(dates_ca,highs_ca,color='red')
ax1.plot(dates_ca,lows_ca,color='blue')
ax1.fill_between(dates_ca,highs_ca,lows_ca,facecolor='blue',alpha=0.3)
ax1.set_title(title_ca)


plt.suptitle("Temperature comparison between " + title_ak + " and " + title_ca)
fig.autofmt_xdate()

plt.show()