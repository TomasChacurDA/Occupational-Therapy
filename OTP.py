import pandas as pd

route = "C:/Users/tomas/Desktop/Excel/otp dataset.csv"
data = pd.read_csv(route)
print(data.head(10))
