from heapq import nlargest
from collections import OrderedDict
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
arr2 = list(OrderedDict.fromkeys(arr))
arr3 = nlargest(2, arr2)
print(arr3[1])