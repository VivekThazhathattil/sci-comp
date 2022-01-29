# Given array, find index and minimum value: imin, xmin = min(x)

def find_min(arr):
    arr_min = arr[0]
    arr_idx = 0
    for i in range(len(arr)):
        if arr[i] < arr_min:
            arr_min = arr[i]
            arr_idx = i
    return arr_min, arr_idx

x = [1, 2, 3, 352, 32, -32, 1, 13]
print(find_min(x))
