colors = {
    "base": "#dddddd",
    "edge": "#cccccc",
    "highlight": "#E6E6FA",
    "highlight_edge": "#734F96",
    "sorted": "#FFC5D3",
    "sorted_edge": "#C68F9D"
}

def bubble_sort(arr):
    arr = list(arr)
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            yield arr.copy(), {"state": "compare", "comparison_idx": j, "edge_pos": n - i}

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr.copy(), {"state": "swap", "comparison_idx": j, "edge_pos": n - i}

    yield arr.copy(), {"state": "done"}


class BubbleSortVisualizer:
    def __init__(self, arr):
        self.arr = arr.copy()

    def get_frame_colors(self, arr, meta):
        colors_list = [colors["base"]] * len(arr)
        edges_list = [colors["edge"]] * len(arr)
        state = meta["state"]

        def color_bar(idx, color):
            colors_list[idx] =  colors[color]
            edges_list[idx] = colors[(color+"_edge")]

        if state in ("compare", "swap"):
            if meta["comparison_idx"] is not None:
                color_bar(meta["comparison_idx"], "highlight")
                color_bar(meta["comparison_idx"]+1, "highlight")
            for i in range(meta["edge_pos"], len(arr)):
                color_bar(i, "sorted")
        elif state == "done":
            colors_list = [colors["sorted"]] * len(arr)
            edges_list = [colors["sorted_edge"]] * len(arr)
        return colors_list, edges_list
