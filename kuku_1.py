import pandas as pd
# わからなくてchatgpt使いました

numbers = list(range(1, 10))

df = pd.DataFrame(columns=numbers, index=numbers)

for i in numbers:
    for j in numbers:
        product = i * j
        df.loc[i, j] = product


print(df)
