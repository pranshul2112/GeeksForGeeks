#  https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

def sortarray(arr):
    counter0 = counter1 = counter2 = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            counter0 += 1
        
        elif arr[i] == 1:
            counter1 += 1
            
        else:
            counter2 += 1
    
    arr = [0] * counter0 + [1] * counter1 + [2] * counter2
    
    return " ".join(str(x) for x in arr)
    
    
test = int(input())

for _ in range(test):
    
    n = int(input())
    arr = list(map(int, input().split()))
    print(sortarray(arr))
    
