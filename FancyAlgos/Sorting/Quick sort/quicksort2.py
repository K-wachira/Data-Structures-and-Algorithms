import sys
def quickSort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    left = []
    right = []
    for value in nums[1:]:
        if value <= pivot:
            left.append(value)
        else:
            right.append(value)

    return quickSort(left) + [pivot] + quickSort(right)


nums = [10, 16, 8, 12, 2, 15, 6, 3, 9, 5]


def partition(low, high, arr):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    print("%1s %ls %1s %-15s" % (arr[low], pivot, arr[j], arr))
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksort(arr, low, high):
    if low < high:
        j = partition(low, high, arr)
        quicksort(arr, low, j)
        quicksort(arr, j+1, high)

    return arr


arr = [10, 16, 8, 12, 2, 15, 6, 3, 9, 5]

low = 0
high = len(arr)-1
print(quicksort(arr, low, high))
