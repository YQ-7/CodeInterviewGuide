import unittest


def max_compare(a, b):
    return a > b


def heap_sort(arr, compare=max_compare):
    """
        堆排序
        时间复杂度O(NlogN)
    """
    if arr is None:
        return arr
    build_max_heap(arr, compare)
    for i in range(len(arr) - 1, -1, -1):
        swap(arr, 0, i)
        heapify(arr, 0, i, compare)


def build_max_heap(arr, compare):
    """
        初始化最大堆
        时间复杂度O(NlogN)
    """
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr), compare)


def heapify(arr, i, size, compare):
    """
        维护堆
        时间复杂度O(logN)
    """
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i
    while left < size:
        if compare(arr[left], arr[i]):
            largest = left
        if right < size and compare(arr[right], arr[largest]):
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
    def test_heap_sort(self):
        array = [6, 2, -4, 12, 65, 2]
        heap_sort(array)
        self.assertEqual(-4, array[0])
        self.assertEqual(2, array[1])
        self.assertEqual(65, array[5])


if __name__ == '__main__':
    unittest.main()
