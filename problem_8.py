# problem 8: rain water trapping # not ngl problem
def maxl(arr):
    temp= []
    top=arr[0]
    temp.append(top)
    
    for i in range(1,len(arr)):
        if arr[i] < top:
            top=top
        else: top= arr[i]
        temp.append(top)

    return temp

def maxr(arr):
    temp= []
    top=arr[len(arr)-1]
    temp.append(top)
    for i in reversed(range(len(arr)-1)):
        if arr[i] < top:
            top=top
            
        else: 
            
            top=arr[i]
        temp.append(top)
    
    temp.reverse()
    
    return temp

def sol(arr):
    ans=0
    water=[]
    right=maxr(arr)
    
    left= maxl(arr)
    

    for i in range(len(arr)):
        water.append(( min(right[i], left[i]) - arr[i]))
        ans+=water[i]
   
        
    return ans

print(sol([0,1,0,2,1,0,1,3,2,1,2,1]))
