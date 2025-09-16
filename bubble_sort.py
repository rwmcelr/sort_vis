import numpy as np

def bubble_sort(arr, subframes):
    arr = list(arr)
    n = len(arr)

    positions = np.arange(n, dtype=float)

    # This list tracks the logical order of the bars.
    # e.g., bar_order[j] gives the original index of the bar currently at logical position j.
    bar_order = list(range(n))

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            # The original indices of the bars we are about to compare.
            compare_idx1 = bar_order[j]
            compare_idx2 = bar_order[j + 1]

            # Yield the state for the comparison frame.
            yield positions.copy(), bar_order.copy(), compare_idx1, compare_idx2, n - i

            if arr[j] > arr[j + 1]:
                # 1. Swap the values in the underlying array.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # 2. Get the start and end x-coordinates for the animation.
                start_pos1 = positions[compare_idx1]
                start_pos2 = positions[compare_idx2]

                # 3. Animate the swap over a number of subframes.
                for t in range(1, subframes + 1):
                    # Linear interpolation factor.
                    factor = t / subframes

                    # Calculate the new interpolated x-coordinate for each of the two swapping bars.
                    positions[compare_idx1] = start_pos1 + (start_pos2 - start_pos1) * factor
                    positions[compare_idx2] = start_pos2 + (start_pos1 - start_pos2) * factor

                    # Yield the updated positions array for this intermediate frame.
                    yield positions.copy(), bar_order.copy(), compare_idx1, compare_idx2, n - i

                # 4. Update the logical order tracker after the swap is complete.
                bar_order[j], bar_order[j + 1] = bar_order[j + 1], bar_order[j]

        # Yield a frame to show the newly sorted element at the end of the pass.
        yield positions.copy(), bar_order.copy(), None, None, n - i - 1

        if not swapped:
            # If no swaps occurred in a full pass, the array is sorted.
            break

    # Final yield to color the entire array as sorted.
    yield positions.copy(), bar_order.copy(), None, None, 0