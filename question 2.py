import matplotlib.pyplot as plt
import numpy as py

# Data from the table
data = {
    "Female Height": [175, 158, 166, 175, 160, 165, 166, 170, 170, 172],
    "Female Breath Held": [22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 34.66],
    "Male Height": [184, 182, 180, 191, 189, 181, 180, 170, 176, 185],
    "Male Breath Held": [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27, 59.09, 51.15, 58.32]
}

# Combine breath-holding times for histogram (ignoring sex)
breath_holding_times = female_breath + male_breath

# Plotting the histogram
plt.figure(figsize=(12, 5))

# Subplot 1: Histogram of breath holding times
plt.subplot(1, 2, 1)
plt.hist(breath_holding_times, bins=8, color="skyblue", edgecolor="black")
plt.title("Histogram of Breath Holding Times")
plt.xlabel("Breath Holding Time (s)")
plt.ylabel("Frequency")

# Subplot 2: Side-by-side dot plot for males and females
plt.subplot(1, 2, 2)
plt.scatter(female_breath, ["Female"] * len(female_breath), color="pink", label="Female", alpha=0.7)
plt.scatter(male_breath, ["Male"] * len(male_breath), color="blue", label="Male", alpha=0.7)
plt.title("Side-by-Side Dot Plot of Breath Holding Times")
plt.xlabel("Breath Holding Time (s)")
plt.legend()
plt.grid(axis='x', linestyle="--", alpha=0.5)

# Adjust layout and show plot
plt.tight_layout()
plt.show()
