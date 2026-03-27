import pandas as pd
df = pd.read_csv("books.csv")
print("\nComplete Book Report:\n")
print(df)
author_name = input("\nEnter author name: ")
print("\nBooks by author:")
print(df[df['author'] == author_name])
publisher_name = input("\nEnter publisher name: ")
print("\nBooks by publisher:")
print(df[df['publisher'] == publisher_name])
cheapest = df[df['price'] == df['price'].min()]
costliest = df[df['price'] == df['price'].max()]
print("\nCheapest Book:")
print(cheapest[['title', 'price']])
print("\nCostliest Book:")
print(costliest[['title', 'price']])
sorted_df = df.sort_values(by='year')
print("\nBooks sorted by Year:")
print(sorted_df)