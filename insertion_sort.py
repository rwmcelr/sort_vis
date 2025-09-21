colors = {
    "base": "#dddddd",
    "edge": "#cccccc",
    "highlight": "#E6E6FA",
    "highlight_edge": "#734F96",
    "sorted": "#FFC5D3",
    "sorted_edge": "#C68F9D",
    "key": "#FFD580",
    "key_edge": "#946300"
}

def insertion_sort(arr):
    arr = list(arr)
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        yield arr.copy(), {"state": "key", "idx": i}

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr.copy(), {"state": "shift", "key_idx": i, "current_idx": j + 1}

        arr[j + 1] = key
        yield arr.copy(), {"state": "insert", "idx": j + 1}

    yield arr.copy(), {"state": "done"}


class InsertionSortVisualizer:
    def __init__(self, arr):
        self.arr = arr.copy()
        self.colors_list = [colors["base"]] * len(arr)
        self.edges_list = [colors["edge"]] * len(arr)

    def get_frame_colors(self, arr, meta):
        colors_list = self.colors_list
        edges_list = self.edges_list
        state = meta["state"]

        def color_bar(idx, color):
            colors_list[idx] =  colors[color]
            edges_list[idx] = colors[(color+"_edge")]

        if state == "key":
            color_bar(meta["idx"],"key")
        elif state == "shift":
            if meta["key_idx"] > 0:
                colors_list[:meta["key_idx"]] = [colors["sorted"]] * len(arr[:meta["key_idx"]])
                edges_list[:meta["key_idx"]] = [colors["sorted_edge"]] * len(arr[:meta["key_idx"]])
            color_bar(meta["key_idx"], "key")
            color_bar(meta["current_idx"],"highlight")
        elif state == "insert":
            if meta["idx"] > 0:
                colors_list[:meta["idx"]] = [colors["sorted"]] * meta["idx"]
                edges_list[:meta["idx"]] = [colors["sorted_edge"]] * meta["idx"]
                color_bar(meta["idx"],"highlight")
        elif state == "done":
            colors_list = [colors["sorted"]] * len(arr)
            edges_list = [colors["sorted_edge"]] * len(arr)

        return colors_list, edges_list