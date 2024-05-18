# problem - 6: maximum area on histogram. we use, nsr and nsl to find the width and then use area formula 

from collections import deque
def nsr(arr):
    temp=[len(arr)]*len(arr) # value in right side on the array
    s=deque()
    for i in reversed(range(len(arr))):
        while s:
            if s[-1][0] < arr[i]:
                temp[i]= s[-1][1]
                break
            else: 
                s.pop()

        s.append((arr[i],i))

    return temp
def nsl(arr):
    temp=[-1]*len(arr)
    s=deque()
    for i in range(len(arr)):
        while s:
            if s[-1][0] < arr[i]:
                temp[i]= s[-1][1]
                break
            else:
                s.pop()

        s.append((arr[i],i))

    return temp
def sol(arr):
    width, ans=[],[]
    right= nsr(arr)
    left= nsl(arr)
    #print(right,left)

    for i in range(len(arr)):
        width.append( (right[i] - left[i] -1))

    
    for i in range(len(arr)):
        ans.append(( arr[i] * width[i]))

    #print(ans)

    return max(ans)

print(sol([6, 2, 5, 4, 5, 1, 6]))

# output: 12
