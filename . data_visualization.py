import matplotlib.pyplot as plt

data = [5, 10, 15, 20]
labels = ['A', 'B', 'C', 'D']

plt.bar(labels, data)
plt.title("Simple Bar Chart")
plt.savefig("chart.png")
print("Chart saved as chart.png")
