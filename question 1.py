import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data for the bar chart
data = {
    'Category': ['Spinach', 'Sausage', 'Prawns', 'Pineapple', 'Mushroom'],
    'Proportion': [0.27, 0.20, 0.10, 0.15, 0.18]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a horizontal bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x='Proportion', y='Category', data=df, color='purple')

# Customize the plot
plt.xlabel('Proportion of Total')
plt.ylabel('')
plt.title('Proportion of Ingredients')
plt.tight_layout()
plt.show()