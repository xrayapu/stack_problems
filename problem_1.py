# problem -1: nearest right element in the array
from collections import deque
def sol(arr):
    ans=[-1]*len(arr)
    s=deque()
    for num in reversed(range(len(arr))):
        while s:
            if s[-1] > arr[num]:
                ans[num] = s[-1]
                break

            else:
                s.pop()

        s.append(arr[num])

    return ans

print( sol([1,3,0,0,1,2,4]))

