
# problem 2: nearest greatest to left

from collections import deque
def sol( arr):

    ans=[-1] * len(arr)
    s=deque()
    for i in range(len(arr)):
        while s:
            if s[-1] > arr[i]:
                ans[i]= s[-1]
                break

            else:
                s.pop()

        s.append(arr[i])

    return ans

print(sol([1,3,0,1,1,2,4]))

# output : [-1, -1, 3, 3, 3, 3, -1]

# time: O(n)
# space : O(n)
# no change at all , only reverse array issue nothing else ! same as problem 1
