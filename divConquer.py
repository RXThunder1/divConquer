def countZeroes(arr):
    left, right = 0, len(arr) - 1
    
    # Binary search to find the first occurrence of 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == 0:
            right = mid - 1
        else:
            left = mid + 1
    
    # All elements are 1s, so right + 1 gives the count of 0s
    return len(arr) - right - 1


    def sortedFrequency(arr, num):
    def findBoundary(arr, num, isFirst):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < num:
                left = mid + 1
            elif arr[mid] > num:
                right = mid - 1
            else:
                if isFirst:
                    if mid == 0 or arr[mid - 1] != num:
                        return mid
                    right = mid - 1
                else:
                    if mid == len(arr) - 1 or arr[mid + 1] != num:
                        return mid
                    left = mid + 1
        return -1
    
    firstIdx = findBoundary(arr, num, True)
    if firstIdx == -1:
        return -1
    
    lastIdx = findBoundary(arr, num, False)
    
    return lastIdx - firstIdx + 1


    def findRotatedIndex(arr, num):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        
        # Check which side is normally sorted
        if arr[left] <= arr[mid]:  # Left half is normally sorted
            if arr[left] <= num < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is normally sorted
            if arr[mid] < num <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1



Sure, let's go through each of these functions step by step in Python, ensuring they meet the specified time complexity constraints.

1. countZeroes
This function counts the number of zeroes in a sorted array of 1s and 0s.

python
Copy code
def countZeroes(arr):
    left, right = 0, len(arr) - 1
    
    # Binary search to find the first occurrence of 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == 0:
            right = mid - 1
        else:
            left = mid + 1
    
    # All elements are 1s, so right + 1 gives the count of 0s
    return len(arr) - right - 1
2. sortedFrequency
This function counts the occurrences of a number in a sorted array.

python
Copy code
def sortedFrequency(arr, num):
    def findBoundary(arr, num, isFirst):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < num:
                left = mid + 1
            elif arr[mid] > num:
                right = mid - 1
            else:
                if isFirst:
                    if mid == 0 or arr[mid - 1] != num:
                        return mid
                    right = mid - 1
                else:
                    if mid == len(arr) - 1 or arr[mid + 1] != num:
                        return mid
                    left = mid + 1
        return -1
    
    firstIdx = findBoundary(arr, num, True)
    if firstIdx == -1:
        return -1
    
    lastIdx = findBoundary(arr, num, False)
    
    return lastIdx - firstIdx + 1
3. findRotatedIndex
This function finds the index of a number in a rotated sorted array.

python
Copy code
def findRotatedIndex(arr, num):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        
        # Check which side is normally sorted
        if arr[left] <= arr[mid]:  # Left half is normally sorted
            if arr[left] <= num < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is normally sorted
            if arr[mid] < num <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


def findRotationCount(arr):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # If the array is already sorted, return 0
        if arr[left] <= arr[right]:
            return left
        
        mid = (left + right) // 2
        next_mid = (mid + 1) % len(arr)
        prev_mid = (mid - 1 + len(arr)) % len(arr)
        
        # Check if mid is the rotation point
        if arr[mid] <= arr[next_mid] and arr[mid] <= arr[prev_mid]:
            return mid
        
        # Decide which half to continue the search
        if arr[left] <= arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0  # This case should never occur for a valid input as per the problem statement


    def findFloor(arr, x):
    left, right = 0, len(arr) - 1
    floor = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            floor = arr[mid]
            left = mid + 1
        else:
            right = mid - 1
    
    return floor