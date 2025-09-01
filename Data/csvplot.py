import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file
df = pd.read_csv("movies_info.csv")

# Step 2: Plot bar graph
plt.bar(df["original_title"], df["overview"], df["genres"])

# Step 3: Add labels and title
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Graph from CSV")

# Step 4: Show plot
plt.show()