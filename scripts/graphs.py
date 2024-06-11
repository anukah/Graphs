import pandas as pd
import matplotlib.pyplot as plt
excel_file = '/Users/anukahettiarachchi/PycharmProjects/graphs/Data/types.xlsx'
df = pd.read_excel(excel_file)

stations = df.iloc[1:42, 1].tolist()
data1 = df.iloc[1:42, 2].tolist()
data2 = df.iloc[1:42, 3].tolist()
data3 = df.iloc[1:42, 5].tolist()
data4 = df.iloc[1:42, 6].tolist()

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Plot the first graph (bottom)
ax1.plot(stations, data1, marker='o', label='El Niño')
ax1.plot(stations, data2, marker='o', label='Individual El Niño')
ax1.set_ylabel('Percentage rainfall deviation %', fontweight='bold')
ax1.legend()

# Plot the second graph (top)
ax2.plot(stations, data3, marker='o', label='El Niño')
ax2.plot(stations, data4, marker='o', label='Individual El Niño')
ax2.set_ylabel('Percentage rainfall deviation %', fontweight='bold')
ax2.legend()

fig.text(0.5, 0.04, 'Weather Stations', ha='center', fontweight='bold')

plt.xticks(rotation=90)

plt.tight_layout(rect=[0, 0.04, 1, 1])

plt.show()