import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Facecream": [2500, 2630, 2140, 3400, 3600, 2760],
    "Facewash": [1500, 1200, 1340, 1130, 1740, 1555],
    "Toothpaste": [5200, 5100, 4550, 5870, 6100, 6000],
    "Bathingsoap": [9200, 6100, 9550, 8870, 9960, 8100],
    "Shampoo": [1200, 2100, 3550, 1870, 1560, 1890]
}
df = pd.DataFrame(data)
df['Total'] = df.iloc[:, 1:].sum(axis=1)
plt.plot(df['Month'], df['Total'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()
plt.plot(df['Month'], df['Facecream'], label='Facecream')
plt.plot(df['Month'], df['Facewash'], label='Facewash')
plt.plot(df['Month'], df['Toothpaste'], label='Toothpaste')
plt.plot(df['Month'], df['Bathingsoap'], label='Soap')
plt.plot(df['Month'], df['Shampoo'], label='Shampoo')
plt.legend()
plt.title("Product Sales Data")
plt.show()
x = range(len(df['Month']))
plt.bar(x, df['Facecream'], width=0.4, label='Facecream')
plt.bar([i+0.4 for i in x], df['Facewash'], width=0.4, label='Facewash')
plt.xticks([i+0.2 for i in x], df['Month'])
plt.legend()
plt.title("Facecream vs Facewash Sales")
plt.show()
total_sales = df.iloc[:, 1:-1].sum()
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()