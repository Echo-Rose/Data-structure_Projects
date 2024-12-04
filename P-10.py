import random
from queue import Queue
from collections import deque

def selection_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            movements += 2
    return arr, comparisons, movements

def insertion_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            movements += 1
            j -= 1
        arr[j + 1] = key
        movements += 1
    return arr, comparisons, movements

def bubble_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movements += 2
    return arr, comparisons, movements

def shell_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        if gap % 2 == 0:
            gap += 1
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                comparisons += 1
                arr[j] = arr[j - gap]
                movements += 1
                j -= gap
            arr[j] = key
            movements += 1
        gap //= 2
    return arr, comparisons, movements

def heapify(arr, n, i, comp_mov):
    comparisons, movements = comp_mov
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
        comparisons += 1
    if r < n and arr[largest] < arr[r]:
        largest = r
        comparisons += 1
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        movements += 2
        arr, comp_mov = heapify(arr, n, largest, (comparisons, movements))
    return arr, (comparisons, movements)

def heap_sort(arr):
    n = len(arr)
    comparisons = 0
    movements = 0
    for i in range(n // 2 - 1, -1, -1):
        arr, (comparisons, movements) = heapify(arr, n, i, (comparisons, movements))
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        movements += 2
        arr, (comparisons, movements) = heapify(arr, i, 0, (comparisons, movements))
    return arr, comparisons, movements

def merge_sort(arr):
    comparisons = [0]
    movements = [0]
    def merge_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_helper(arr, left, mid)
            merge_helper(arr, mid + 1, right)
            merge(arr, left, mid, right, comparisons, movements)
    merge_helper(arr, 0, len(arr) - 1)
    return arr, comparisons[0], movements[0]

def merge(arr, left, mid, right, comparisons, movements):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        comparisons[0] += 1
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
        movements[0] += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
        movements[0] += 1
    while j <= right:
        temp.append(arr[j])
        j += 1
        movements[0] += 1
    for i in range(left, right + 1):
        arr[i] = temp[i - left]


# Quick Sort
def quick_sort(arr):
    comparisons = [0]
    movements = [0]
    def quick_sort_helper(arr, left, right):
        if left < right:
            pivot = partition(arr, left, right, comparisons, movements)
            quick_sort_helper(arr, left, pivot - 1)
            quick_sort_helper(arr, pivot + 1, right)
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr, comparisons[0], movements[0]

def partition(arr, left, right, comparisons, movements):
    pivot = arr[left]
    low = left + 1
    high = right
    while True:
        while low <= high and arr[low] <= pivot:
            low += 1
            comparisons[0] += 1
        while low <= high and arr[high] >= pivot:
            high -= 1
            comparisons[0] += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            movements[0] += 2
        else:
            break
    arr[left], arr[high] = arr[high], arr[left]
    movements[0] += 2
    return high


# Sorting Dispatcher
algorithms = {
    "SEL": selection_sort,
    "INS": insertion_sort,
    "BUB": bubble_sort,
    "SHE": shell_sort,
    "HEA": heap_sort,
    "MER": merge_sort,
    "QUI": quick_sort,
}

if __name__ == "__main__":
    data_input = input("* Please input a data list : ")
    data_list = list(map(int, data_input.split(",")))
    print("Target Sorting Algorithm List:\nSelection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE), Heap(HEA), Merge(MER), Quick(QUI)")
    algorithm_choice = input("* Select sorting algorithm: ").strip().upper()
    if algorithm_choice in algorithms:
        sorted_data, num_comparisons, num_movements = algorithms[algorithm_choice](data_list)
        print(f">> Sorted : {', '.join(map(str, sorted_data))}")
        print(f">> Number of Comparisons : {num_comparisons}")
        print(f">> Number of Data Movements : {num_movements}")
    else:
        print("Invalid sorting algorithm choice.")

# Data List test : 1, 3, 4, 5, 8