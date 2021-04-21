import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("C:\\Users\\PC\\Desktop\\demo2.csv")
sns.set_style()
pd.set_option('display.max_rows', data.shape[0]+1)
plt.hist(data)
sns.relplot(data= data, kind= 'line')
plt.show()


