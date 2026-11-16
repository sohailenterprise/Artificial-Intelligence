import numpy as np

units = np.array([[30, 20, 10],   # rows: 4 days
                  [25, 30, 15],   # cols: Tea, Coffee, Cake
                  [40, 25, 20],
                  [35, 15, 25]])
price = np.array([100, 150, 200])

# Broadcasting: (4,3) * (3,) -> revenue of every item on every day
revenue = units * price

print("Revenue per day:", revenue.sum(axis=1))
print("Units sold per item:", units.sum(axis=0))
print("Best day index:", revenue.sum(axis=1).argmax())
print("Coffee, last two days:", units[-2:, 1])