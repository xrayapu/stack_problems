 problem -5: stock span problem: similar to , nearest greater to left, problem 2

from collections import deque
def sol(arr):
    ans=[-1]*len(arr)
    res=[0]* len(arr)

    s= deque()
    for i in range(len(arr)):
        while s:
            if s[-1][0] > arr[i]: # change some minor things 
                ans[i] = s[-1][1]
                break                
            else: 
                s.pop()               
        s.append((arr[i],i))

    for i in range(len(ans)): # just small change
        res[i]= i - ans[i]

    return res

print(sol([100,80,60,70,60,75,85])) 

#output:[1, 1, 1, 2, 1, 4, 6]

#print(sol([10, 4, 5, 90 ,120, 80]))
#output:[1, 1, 2, 4, 5, 1]
