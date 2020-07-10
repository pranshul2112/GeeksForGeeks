#  https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0

t = int(input())
for _ in range(t):
    n = int(input())
    beg = list(map(int, input().split()))
    end = list(map(int, input().split()))
    
    arr = []
    for i in range(n):
        arr.append((end[i], beg[i]))
    
    arr.sort()
    
    a = arr[0][1]
    b = 0
    c = []
    for i in range(len(arr)):
        if arr[i][1] >= a:
            b += 1
            a = arr[i][0]
            c.append((arr[i][1], arr[i][0]))
            
    for i in range(len(c)):
        for j in range(n):
            if beg[j] == c[i][0] and end[j] == c[i][1]:
                print(j + 1, end=' ')
    print()
            
