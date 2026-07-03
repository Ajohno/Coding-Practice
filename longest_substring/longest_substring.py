def lengthOfLongestSubstring(s: str) -> int:
    # Dictionary for if the character has been seen
    seen = {}
    # The start index of the window
    start = 0
    # The maximum length of the substring found so far
    max_length = 0

    # Iterate through the string with index and character
    for i, char in enumerate(s):

        # If the character has been seen and is within the current window, move the start index
        if char in seen and seen[char] >= start:
            # Move the start index to one position after the last occurrence of the character
            start = seen[char] + 1

        # Update the last seen index of the character
        seen[char] = i
        # Update the maximum length of the substring found so far
        max_length = max(max_length, i - start + 1)

    return max_length