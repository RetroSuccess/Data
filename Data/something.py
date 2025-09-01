from matplotlib import pyplot as plt
import pandas as pd

data = {
    "Cataegory":["Electronics", "Clothing", "Books", "Home", "Food"],
    "Scores":[4.2, 3.8, 4.5, 3.9, 4.1]
}

df = pd.DataFrame(data)

df = df.sort_values(by="Scores", ascending=False)

colors = ["blue", "green", "orange", "yellow"]

plt.bar(df["Cataegory"], df["Scores"], color=colors)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Bar Chart")

plt.show()