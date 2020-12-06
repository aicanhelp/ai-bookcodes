import random


class QuickSort():
    def __init__(self, nums):
        self.__nums = nums

    def sort(self):
        self.__shuffle()
        self.__sort(0, len(self.__nums) - 1)
        return self.__nums

    def __shuffle(self):
        random.shuffle(self.__nums)

    def __sort(self, l, h):
        if h <= l: return
        j = self.__partition(l, h)
        self.__sort(l, j)
        self.__sort(j + 1, h)
        return self.__nums

    def __partition(self, l, h):
        i = l + 1
        j = h
        v = self.__nums[h]
        while True:
            while self.__nums[i] < v and i != h: i = i + 1
            while self.__nums[j] > v and j != l: j = j - 1
            if i >= j: break
            self.__swap(i, j)

        self.__swap(l, i)
        return j

    def __swap(self, i, j):
        v = self.__nums[i]
        self.__nums[i] = self.__nums[j]
        self.__nums[j] = v


class HeapSort():
    # 数组第0个位置不能有元素, 因为0 * 2 = 0
    def __init__(self, nums):
        self.__nums = nums

    def sort(self):
        n = len(self.__nums) - 1
        for i in range(int(n / 2), 1):
            self.__sink(i, n)
            
        while n > 1:
            self.__swap(1, n)
            n = n - 1
            self.__sink(1, n)

        return self.__nums

    def __sink(self, i, n):
        while 2 * i <= n:
            j = 2 * i
            if j < n and self.__less(j, j + 1):
                j = j + 1
            if not self.__less(i, j):
                self.__swap(i, j)
            i = j

    def __swap(self, i, j):
        v = self.__nums[i]
        self.__nums[i] = self.__nums[j]
        self.__nums[j] = v

    def __less(self, i, j):
        return self.__nums[i] < self.__nums[j]
