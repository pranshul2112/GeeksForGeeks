#  https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

def subArraySum(arr, k):
    header = wsum = 0

    for i in range(len(arr)):

        wsum += arr[i]

        while wsum > k:
            wsum -= arr[header]
            header += 1

        if wsum == k:
            return " ".join(str(x) for x in [header + 1, i + 1])

    return -1


test = int(input())

for _ in range(test):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(subArraySum(arr, k))
