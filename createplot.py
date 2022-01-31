import pandas as pd

plot_points = input("Enter in your points (Format: {Column Name: [1, 1], [1,2]}\n>")

pd.plot(plot_points, kind='line')
