# problem -5: stock span problem: similar to , nearest greater to left, problem 2

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


# leetcode 739: Given an array of integers temperatures represents the daily temperatures, return an 
#array answer such that answer[i] is the number of days you have to wait after the ith day to get a 
#warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

##similar to problem 1, nearest greater to right. and it's only minor alternative to stock span problem.


from collections import deque
class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
       
        ans=[-1]*len(arr)
        res=[0]* len(arr)

        s= deque()
        for i in reversed(range(len(arr))): # here only 
            while s:
                if s[-1][0] > arr[i]:
                    ans[i] = s[-1][1]
                    break                
                else: 
                    s.pop()               
            s.append((arr[i],i))

        #print( ans)

        for i in range(len(ans)):
            if ans[i] !=-1:
                res[i]=  ans[i]-i
            else:
                res[i]=0

        return res

#Input: temperatures = [73,74,75,71,69,72,76,73]
#Output: [1,1,4,2,1,1,0,0]
