import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from sorts import bubble_sort, insertion_sort, quick_sort, selection_sort

rand_arr = np.random.randint(0, 1000, 50)

sort_map = {
    "bubble": (bubble_sort.bubble_sort, bubble_sort.BubbleSortVisualizer),
    "insertion": (insertion_sort.insertion_sort, insertion_sort.InsertionSortVisualizer),
    "quick": (quick_sort.quick_sort, quick_sort.QuickSortVisualizer),
    "selection": (selection_sort.selection_sort, selection_sort.SelectionSortVisualizer)
}

class SortAnimation:
    def __init__(self, ax, arr, sort_gen, visualizer_cls):
        self.ax = ax
        self.arr = arr.copy()
        self.visualizer = visualizer_cls(arr)
        self.bars = ax.bar(np.arange(len(arr)), arr, width=0.9, align="edge",
                           facecolor="#dddddd", edgecolor="#cccccc")
        self.animation = animation.FuncAnimation(
            fig, self.update, frames=sort_gen(arr),
            interval=15, repeat=False, cache_frame_data=False
        )

    def update(self, frame):
        arr, meta = frame
        colors_list, edges_list = self.visualizer.get_frame_colors(arr, meta)
        for bar, h, c, e in zip(self.bars, arr, colors_list, edges_list):
            bar.set_height(h)
            bar.set_facecolor(c)
            bar.set_edgecolor(e)
        return self.bars


# --- Initialize canvas ---
fig, ax_dict = plt.subplot_mosaic(
     [['header', 'header', 'header', 'header'],
      ['bubble', 'bubble_button', 'insertion_button', 'insertion'],
      ['quick', 'quick_button', 'selection_button', 'selection'],
      ['merge', 'merge_button', 'radix_button', 'radix'],
      ['block', 'block_button', 'bogo_button', 'bogo']],
     figsize = (9,9)
 )
fig.suptitle('Sorting Algorithm Comparisons')
for ax_key in ax_dict.values():
    ax_key.set_xlim(0, len(rand_arr))
    ax_key.set_ylim(0, max(rand_arr) * 1.1)
    ax_key.set_xticks([])
    ax_key.set_yticks([])

# --- Create animations ---
bubble = SortAnimation(ax_dict['bubble'], rand_arr, *sort_map["bubble"])
bubble.ax.set_title("Bubble Sort")
insertion = SortAnimation(ax_dict['insertion'], rand_arr, *sort_map["insertion"])
insertion.ax.set_title("Insertion Sort")
quick = SortAnimation(ax_dict['quick'], rand_arr, *sort_map["quick"])
quick.ax.set_title("Quick Sort")
selection = SortAnimation(ax_dict['selection'], rand_arr, *sort_map["selection"])
selection.ax.set_title("Selection Sort")

plt.show()
