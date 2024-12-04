import matplotlib.pyplot as plt
import numpy as np

# Sample data for plant growth (in mm)
with_music = [304, 257, 174, 214, 69, 317, 387, 47, 157, 0,
              332, 308, 317, 286, 236, 299, 206, 278, 188, 43, 0, 0, 0, 0, 0]
without_music = [292, 270, 47, 288, 324, 292, 364, 316, 287, 75,
                 282, 149, 274, 319, 213, 3, 324, 2, 128, 219, 94, 164, 0, 0, 0]

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Dot Plot for With Music
axs[0, 0].scatter([1]*len(with_music), with_music, color='blue', alpha=0.5)
axs[0, 0].set_title('Dot Plot: With Music')
axs[0, 0].set_ylabel('Growth (mm)')
axs[0, 0].set_xticks([])

# Dot Plot for Without Music
axs[0, 1].scatter([2]*len(without_music), without_music, color='orange', alpha=0.5)
axs[0, 1].set_title('Dot Plot: Without Music')
axs[0, 1].set_ylabel('Growth (mm)')
axs[0, 1].set_xticks([])

# Histogram for With Music
axs[1, 0].hist(with_music, bins=10, color='blue', alpha=0.7)
axs[1, 0].set_title('Histogram: With Music')
axs[1, 0].set_xlabel('Growth (mm)')
axs[1, 0].set_ylabel('Frequency')

# Histogram for Without Music
axs[1, 1].hist(without_music, bins=10, color='orange', alpha=0.7)
axs[1, 1].set_title('Histogram: Without Music')
axs[1, 1].set_xlabel('Growth (mm)')
axs[1, 1].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()
plt.show()