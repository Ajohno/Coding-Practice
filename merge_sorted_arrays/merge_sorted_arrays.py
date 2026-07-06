def merge_sorted_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    """Return a new sorted array containing all values from nums1 and nums2."""
    # Initialize indexes for nums1 and nums2
    i, j = 0, 0 

    # Result array
    merged_array =[]

    # Iterate through both arrays while the indexes are within their size
    while i < len(nums1) and j < len(nums2):
        # Compare the current elements of both arrays
        if nums1[i] < nums2[j]:
            # If the element in nums1 is smaller than the element in nums2, add to merged_array and move the index of nums1
            merged_array.append(nums1[i])
            # Increment the index for nums1
            i += 1
        else:
            # If the element in nums2 is smaller than the element in nums1, add to merged_array and move the index of nums2
            merged_array.append(nums2[j])
            # Increment the index for nums2
            j += 1

    # Append any remaining elements from either array
    merged_array.extend(nums1[i:])
    merged_array.extend(nums2[j:])

    return merged_array