import matplotlib.pyplot as plt
import numpy as np
from bubble_sort import bubble_sort
import matplotlib.animation as animation

colors = {
    "base": "#dddddd",
    "edge": "#cccccc",
    "focus": "#E6E6FA",   # lavender
    "compare": "#FFD8A8", # pastel orange
    "sorted": "#C8F7D4",  # green
}

arr = np.random.randint(0, 1000, 25)
swap_frames = 3

fig, ax = plt.subplots(figsize = (12,4))
bars = ax.bar(np.arange(len(arr)), arr, width=0.9, align="edge",
              facecolor=colors["base"], edgecolor=colors["edge"])

ax.axis('off')
ax.set_title('Bubble Sort Animation')
ax.set_xlim(0, len(arr))
ax.margins(0,0)

def update(frame):
    positions, bar_order, focus, compare, sorted_start = frame

    for bar, x in zip(bars, positions):
        bar.set_x(x)
        bar.set_facecolor(colors['base'])
        bar.set_edgecolor("#cccccc")

    if sorted_start < len(bars):
        for k in range(sorted_start, len(bars)):
            original_bar_idx = bar_order[k]
            bars[original_bar_idx].set_facecolor(colors['sorted'])

    if focus is not None and compare is not None:
        bars[focus].set_facecolor(colors['focus'])
        bars[compare].set_facecolor(colors['compare'])

    return bars

ani = animation.FuncAnimation(
    fig, update, frames=bubble_sort(arr, swap_frames),
    interval=50, repeat=False, blit=False, cache_frame_data=False
)

plt.show()