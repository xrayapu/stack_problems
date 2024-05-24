
# problem 7: maximum area in binary matrix

#solve but not leetcode's , when it was string there

from collections import deque
def nsl(arr):
    ans=[-1]*len(arr)
   
    s=deque()

    for i in range(len(arr)):
        while s:
            if s[-1][0] < arr[i]:
                ans[i]= s[-1][1]
                break
            else: s.pop()

        s.append((arr[i],i))
    return ans
    


    
def nsr(arr):
    ans=[-1]*len(arr)
   
    s=deque()

    for i in reversed(range(len(arr))):
        while s:
            if s[-1][0] < arr[i]:
                ans[i]= s[-1][1]
                break
            else: s.pop()

        s.append((arr[i],i))
    return ans

def mah(arr):
    left= nsl(arr)
    right= nsr(arr)
    wid, res= [],[]
    for i in range(len(arr)):
        wid.append((right[i]-left[i]-1))

    for i in range(len(arr)):
        res.append((arr[i]*wid[i]))

    return max(res)

def sol(arr):
    narr= arr[0]
    it= mah(narr)
    for i in range(1,len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                narr[j] =0
            else:
                narr[j] += arr[i][j]

        it= max(it,mah(narr))

    return it

# print(sol([[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]))
