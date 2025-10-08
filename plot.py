import matplotlib.pyplot as plt

labels = [
    'Below 18 years',
    '18–45 years',
    '45–60 years',
    '60 years & above'
]
sizes = [6, 66.5, 16.9, 10.6]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

plt.figure(figsize=(7,7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Road Accident Fatalities in India by Age Group (2022)')
plt.axis('equal')
plt.show()
