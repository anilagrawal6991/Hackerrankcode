import collections
import sys

T = int(input())

for i in range(T):
    n = int(input())
    sideLengths = collections.deque(map(int, input().split()))

    lastLength = sys.maxsize
    answer = 'Yes'

    while len(sideLengths) > 0:
        if len(sideLengths) == 1:
            item = sideLengths.pop()
        else:
            if sideLengths[0] < sideLengths[-1]:
                item = sideLengths.pop()
            else:
                item = sideLengths.popleft()

        if item > lastLength:
            answer = 'No'
            break
        else:
            lastLength = item

    print (answer)