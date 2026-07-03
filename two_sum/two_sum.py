def twoSum(nums, target):

    # Dictionary of numbers that have been seen so far
    seen = {}

    for i, num in enumerate(nums):
        # Calculate the complement that would sum to the target
        complement = target - num

        # Check if the complement is already in the seen dictionary
        if complement in seen:
            return [seen[complement], i]

        # If not, add the current number and its index to the seen dictionary
        seen[num] = i
