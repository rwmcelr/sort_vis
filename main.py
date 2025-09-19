import matplotlib.pyplot as plt
import numpy as np
from bubble_sort import bubble_sort
import matplotlib.animation as animation

colors = {
    "base": "#dddddd",
    "edge": "#cccccc",
    "highlight": "#E6E6FA",   # lavender
    "sorted": "#FFC5D3", # pastel pink
}

arr = np.random.randint(0, 1000, 25)

fig, ax = plt.subplots(figsize = (12,4))
bars = ax.bar(np.arange(len(arr)), arr, width=0.9, align="edge",
              facecolor=colors["base"], edgecolor=colors["edge"])

ax.axis('off')
ax.set_title('Bubble Sort Animation')
ax.set_xlim(0, len(arr))
ax.margins(0,0)

def update(frame):
    sorting_array, comparison, sorted_left_edge = frame

    for i, bar in enumerate(bars):
        bar.set_height(sorting_array[i])
        if i < sorted_left_edge:
            bar.set_edgecolor(colors["edge"])
            bar.set_facecolor(colors["base"])
        else:
            bar.set_facecolor(colors["sorted"])

    if comparison:
        bars[comparison].set_facecolor(colors['highlight'])
        if comparison + 1 < sorted_left_edge:
            bars[comparison+1].set_facecolor(colors['highlight'])
        if bars[comparison-1]: bars[comparison-1].set_facecolor(colors['highlight'])

    return bars

ani = animation.FuncAnimation(
    fig, update, frames=bubble_sort(arr),
    interval=15, repeat=False, cache_frame_data=False
)

plt.show()