# problem 8: rain water trapping # not ngl problem
# def maxl(arr):
#     temp= []
#     top=arr[0]
#     temp.append(top)
    
#     for i in range(1,len(arr)):
#         if arr[i] < top:
#             top=top
#         else: top= arr[i]
#         temp.append(top)

#     return temp

# def maxr(arr):
#     temp= []
#     top=arr[len(arr)-1]
#     temp.append(top)
#     for i in reversed(range(len(arr)-1)):
#         if arr[i] < top:
#             top=top
            
#         else: 
            
#             top=arr[i]
#         temp.append(top)
    
#     temp.reverse()
    
#     return temp

# def sol(arr):
#     ans=0
#     water=[]
#     right=maxr(arr)
    
#     left= maxl(arr)
    

#     for i in range(len(arr)):
#         water.append(( min(right[i], left[i]) - arr[i]))
#         ans+=water[i]
   
        
#     return ans

# print(sol([0,1,0,2,1,0,1,3,2,1,2,1]))

#another easy solution 
#   !
# 3,0,0,2,0,4 
#-> for 0's prespective  left side total max -> 3. right side max ->4
# min(3,4) - 0 ,ans->3 

def sol(arr):
    it=[0]*len(arr)
    mxl=[0]*len(arr)
    mxr=[0]*len(arr)
    ans=0
    mxl[0]=arr[0]
    mxr[len(arr)-1]=arr[len(arr)-1]
    #left side max for any number
    for i in range(1,len(arr)):
        mxl[i]=max(mxl[i-1],arr[i]) # 3 and 0
    # right side max
    for i in reversed(range(len(arr)-1)):
        mxr[i]= max(mxr[i+1],arr[i]) # from last point, 0 and 4
    #how much water can hold , any point to the point skip overflow 
    for i in range(len(arr)):
        it[i]=min(mxl[i],mxr[i])- arr[i]
        ans+=it[i]

    return ans

print(sol([1,8,6,2,5,4,8,3,7]))





