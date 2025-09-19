def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            yield arr, j, n - i
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                yield arr, j, n - i
        yield arr, None, n - i
        if not swapped:
            break
    for x in range(n):
        yield arr, x, 0
    yield arr, None, 0