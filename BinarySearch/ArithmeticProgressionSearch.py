class ArithmeticProgressionSearch:
    def solution(self,a):
        low = 0
        high = len(a) - 1
        middle = -1
        ap = (a[high] - a[low]) / len(a)
        while low <= high:
            middle = (int)((low + high) / 2)
            if a[middle] == a[0] + middle * ap:
                low = middle + 1
            elif a[middle] > a[0] + middle * ap and a[middle - 1] == a[0] + (middle - 1) * ap:
                return a[0] + middle * ap
            else:
                high = middle - 1
        return -1


p = ArithmeticProgressionSearch()
arr = [1, 3, 5, 7, 9, 13]
result = p.solution(arr)
print(result)
