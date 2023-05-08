import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'miami.csv'


def convert_to_celsius(far):
    return round((far - 32) / 1.8)


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for ind, colum in enumerate(header_row):
    #     print(ind, colum)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = convert_to_celsius(int(row[3]))
            low = convert_to_celsius(int(row[5]))
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # print(highs)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures of Miami - 2023", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
