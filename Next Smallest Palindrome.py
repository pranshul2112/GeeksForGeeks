#  https://practice.geeksforgeeks.org/problems/next-smallest-palindrome/0

def generateNextPalindrome(arr, n):
    global carry
    mid = n // 2
    left = False
    i = mid - 1
    j = mid + 1 if n % 2 == 1 else mid

    while i >= 0 and arr[i] == arr[j]:
        i -= 1
        j += 1
    if i < 0 or arr[i] < arr[j]:
        left = True

    while i >= 0:
        arr[j] = arr[i]
        j += 1
        i -= 1

    if left:
        carry = 1
        i = mid - 1
        if n % 2 == 1:
            arr[mid] += carry
            carry = arr[mid] // 10
            arr[mid] %= 10
            j = mid + 1

        else:
            j = mid

    while i >= 0:
        arr[i] += carry
        carry = arr[i] // 10
        arr[i] %= 10
        arr[j] = arr[i]
        j += 1
        i -= 1
    return 

def allAreNine(arr, n):
    for i in range(n):
        if arr[i] != 9:
            return False
    return True


def nextSmallestPalindrome(arr, n):
    if allAreNine(arr, n):
        res = [1]
        for i in range(1, n):
            res.append(0)
        res.append(1)
        return " ".join(str(x) for x in res)

    generateNextPalindrome(arr, n)
    return " ".join(str(x) for x in arr)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(nextSmallestPalindrome(arr, n))
