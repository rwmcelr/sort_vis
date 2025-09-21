colors = {
    "base": "#dddddd",
    "edge": "#cccccc",
    "highlight": "#E6E6FA",
    "highlight_edge": "#734F96",
    "sorted": "#FFC5D3",
    "sorted_edge": "#C68F9D",
    "min": "#FFD580",
    "min_edge": "#946300"
}

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        yield arr.copy(), {"state": "min", "min_idx": i}

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            yield arr.copy(), {"state": "search", "min_idx": min_idx, "search_idx": j, "i": i}

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr.copy(), {"state": "swapped", "min_idx": min_idx, "search_idx": i, "i": i}

    yield arr.copy(), {"state": "done"}

class SelectionSortVisualizer:
    def __init__(self, arr):
        self.arr = arr.copy()
        self.colors_list = [colors["base"]] * len(arr)
        self.edges_list = [colors["edge"]] * len(arr)

    def get_frame_colors(self, arr, meta):
        colors_list = [(c if c == colors["sorted"] else colors["base"])
                       for c in self.colors_list]
        edges_list = [(c if c == colors["sorted_edge"] else colors["edge"])
                      for c in self.edges_list]
        state = meta["state"]

        def color_bar(idx, color):
            colors_list[idx] =  colors[color]
            edges_list[idx] = colors[(color+"_edge")]

        def set_sorted(idx, offset = 0):
            colors_list[:idx] = [colors["sorted"]] * len(arr[:idx + offset])
            edges_list[:idx] = [colors["sorted_edge"]] * len(arr[:idx + offset])
            self.colors_list = colors_list
            self.edges_list = edges_list

        if state == "min":
            color_bar(meta["min_idx"],"min")
        elif state == "search":
            if meta["min_idx"] > 0:
                set_sorted(meta["i"])
            color_bar(meta["min_idx"], "min")
            color_bar(meta["search_idx"],"highlight")
            color_bar(meta["i"], "highlight")
        elif state == "swapped":
            set_sorted(meta["i"], 1)
            color_bar(meta["search_idx"], "min")
            color_bar(meta["min_idx"],"highlight")
        elif state == "done":
            colors_list = [colors["sorted"]] * len(arr)
            edges_list = [colors["sorted_edge"]] * len(arr)

        return colors_list, edges_list