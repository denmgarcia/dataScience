import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("nba.csv")

# Examining the dataframe
print(df)
df.shape

df.Salary.describe().apply(lambda x: format(x, 'f'))

# Line graph of 20 basketball player and their salary

data = df.tail(20)
name = data["Name"].tolist()
salary = data["Salary"].tolist()
plt.ticklabel_format(style="plain")
plt.xticks(rotation=80, fontsize = 'small')
plt.xlabel("Basketball Player")
plt.ylabel("Salary")
plt.plot(name, salary)
plt.show()


## If there's an error on visual code kindly try this command
## Linux: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
##  plt.show()
## sudo apt-get install python3-tk
## Windows with pip  | pip install pyqt5
 


