import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

list1 = [1,2,3,4,5]

sorted_results = sorted(list1)
print("Sorted list:", sorted_results)

print(np.mean(list1))
print(np.median(list1))

data = {'Name':["Alice", "Bob", "Charlie"], 
        'Age':[25, 30, 35], 
        'City':["New York", "Los Angeles", "Chicago"]}

df = pd.DataFrame(data) 
print(df[['Name', 'Age']])
print(df[df['Age'] > 28])
df["Salary"] = [50000, 60000, 70000]
df["Rating"] = [4.5, 3.8, 4.2]
#print(df.shape)
#print(df.info())
#print(df.describe())
#print(df.head())
#print(df.tail())

print(df)
# df = pd.read_csv("data.csv")  # Removed or commented out

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.bar(df['Name'], df['Age'], color=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Age Distribution')
plt.xlabel('Name')
plt.ylabel('Age')
plt.xticks(rotation=45)

# Bar plot - Salary by Name
plt.subplot(2, 2, 2)
plt.bar(df['Name'], df['Salary'], color=['orange', 'purple', 'brown'])
plt.title('Salary Distribution')
plt.xlabel('Name')
plt.ylabel('Salary ($)')
plt.xticks(rotation=45)

# Scatter plot - Age vs Salary
plt.subplot(2, 2, 3)
plt.scatter(df['Age'], df['Salary'], s=100, color='red', alpha=0.7)
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary ($)')

# Line plot - Rating by Name
plt.subplot(2, 2, 4)
plt.plot(df['Name'], df['Rating'], marker='o', linestyle='-', color='green', linewidth=2)
plt.title('Rating by Name')
plt.xlabel('Name')
plt.ylabel('Rating')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Additional individual plots
# Pie chart for Age distribution
plt.figure(figsize=(8, 6))
plt.pie(df['Age'], labels=df['Name'], autopct='%1.1f%%', colors=['gold', 'lightblue', 'lightgreen'])
plt.title('Age Distribution Pie Chart')
plt.show()

# Horizontal bar plot for Salary
plt.figure(figsize=(8, 4))
plt.barh(df['Name'], df['Salary'], color=['cyan', 'magenta', 'yellow'])
plt.title('Salary Comparison')
plt.xlabel('Salary ($)')
plt.tight_layout()
plt.show()