# --- Linear Search Implementation ---
def linear_search(arr, target):
    # Iterate through the array using the index
    for i in range(len(arr)):
        # Check if the current element matches the target value
        if arr[i] == target:
            return i  # Return the index if a match is found
    # Return -1 if the entire array is searched and target is not found
    return -1

# --- Binary Search Implementation ---
# Note: Binary search requires a sorted array
def binary_search(arr, target):
    # Initialize the lower and upper bounds of the search interval
    low, high = 0, len(arr) - 1
    
    # Continue searching while the search space is valid
    while low <= high:
        # Calculate the middle index (using integer division)
        mid = (low + high) // 2
        
        # Check if the target is exactly at the middle
        if arr[mid] == target:
            return mid
        # If the middle element is less than the target, discard the left half
        elif arr[mid] < target:
            low = mid + 1
        # If the middle element is greater than the target, discard the right half
        else:
            high = mid - 1
            
    # Return -1 if the target is not in the array
    return -1

if __name__ == "__main__":
    # Test data (must be sorted for binary search to work correctly)
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    
    # Display the results
    print(f"Array: {arr}")
    print(f"Linear Search index for {target}: {linear_search(arr, target)}")
    print(f"Binary Search index for {target}: {binary_search(arr, target)}")
