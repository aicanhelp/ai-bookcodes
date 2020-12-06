class BinarySplitSearch:
    def search(self, data, value):
        if len(data) == 0: return -1
        start = 0
        end = len(data)
        while (start < end):
            mid = (end - start) / 2
            if data[mid] == value:
                return mid
            if data[mid] > value:
                end = mid
            else:
                start = mid
        return -1
