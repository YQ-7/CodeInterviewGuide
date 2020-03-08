import unittest


def heap_sort(arr):
    """
        堆排序
        时间复杂度O(NlogN)
    """
    if arr is None:
        return arr
    build_max_heap(arr)
    for i in range(len(arr) - 1, -1, -1):
        swap(arr, 0, i)
        heapify(arr, 0, i)


def build_max_heap(arr):
    """
        初始化最大堆
        时间复杂度O(NlogN)
    """
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))


def heapify(arr, i, size):
    """
        维护最大堆
        时间复杂度O(logN)
    """
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i
    while left < size:
        if arr[left] > arr[i]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            swap(arr, largest, i)
        else:
            break
        i = largest
        left = i * 2 + 1
        right = i * 2 + 2


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
