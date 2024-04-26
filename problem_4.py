# problem 4: nearest smaller to the right

from collections import deque

def sol(arr):
    ans=[-1] * len(arr)
    s= deque()
    for i in reversed(range(len(arr))):
        while s:
            if s[-1] < arr[i]:
                ans[i] = s[-1]
                break
            else: s.pop()

        s.append(arr[i])

    return ans

print(sol([4,5,2,10,8]))

# similar as : problem 1, only smaller element is needed here 
