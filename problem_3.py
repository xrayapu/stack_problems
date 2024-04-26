# problem 3 : nearest smaller to left

from collections import deque

def sol(arr):
    ans =[-1] * len(arr)

    s=deque()

    for i in range(len(arr)):
        while s:
            if s[-1] < arr[i]:
                ans[i] =s[-1]
                break
            else:
                s.pop()

        s.append(arr[i])

    return ans

print(sol([4,5,2,10,8])) 

#output: [-1, 4, -1, 2, 2]
# similar as problem 2, only here left element is less mainly focus ! 

