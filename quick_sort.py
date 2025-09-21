colors = {
    "base": "#dddddd",
    "edge": "#cccccc",
    "highlight": "#E6E6FA",
    "highlight_edge": "#734F96",
    "sorted": "#FFC5D3",
    "sorted_edge": "#C68F9D",
    "pivot": "#FFD580",
    "pivot_edge": "#946300"
}

def quick_sort(arr):
    arr = list(arr)

    def _quicksort(low, high):
        if low < high:
            pivot_idx = low
            pivot = arr[pivot_idx]
            yield arr.copy(), {"state": "pivot", "idx": pivot_idx, "low": low, "high": high}

            i = low + 1
            for j in range(low + 1, high + 1):
                yield arr.copy(), {"state": "partition", "idx": j, "low": low, "high": high}
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[low], arr[i - 1] = arr[i - 1], arr[low]
            yield arr.copy(), {"state": "partition-done", "idx": i - 1, "low": low, "high": high}

            yield from _quicksort(low, i - 2)
            yield from _quicksort(i, high)

    yield from _quicksort(0, len(arr) - 1)
    yield arr.copy(), {"state": "done"}


class QuickSortVisualizer:
    def __init__(self, arr):
        self.arr = arr.copy()

    def get_frame_colors(self, arr, meta):
        colors_list = [colors["base"]] * len(arr)
        edges_list = [colors["edge"]] * len(arr)
        state = meta["state"]
        idx = meta.get("idx")
        low = meta.get("low", 0)
        high = meta.get("high", len(arr) - 1)

        if state == "pivot":
            colors_list[idx] = colors["pivot"]
            edges_list[idx] = colors["pivot_edge"]
        elif state == "partition":
            for i in range(low, high + 1):
                colors_list[i] = colors["highlight"]
                edges_list[i] = colors["highlight_edge"]
            if idx is not None:
                colors_list[idx] = colors["pivot"]
                edges_list[idx] = colors["pivot_edge"]
        elif state == "partition-done":
            for i in range(low, high + 1):
                colors_list[i] = colors["base"]
                edges_list[i] = colors["edge"]
        elif state == "done":
            colors_list = [colors["sorted"]] * len(arr)
            edges_list = [colors["sorted_edge"]] * len(arr)
        return colors_list, edges_list