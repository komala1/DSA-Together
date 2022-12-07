def find(arr,n,x):
    if x not in arr:
        return [-1,-1]
    res = []
    for i in range(len(arr)):
        if arr[i] == x:
            res.append(i)
    return [res[0],res[-1]]
'''Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  2 5
Explanation: First occurrence of 5 is at index 2 and last
             occurrence of 5 is at index 5. '''
