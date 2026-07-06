def longest_unique_prefix(s: str) -> int:
    """Return the length of the longest prefix containing no repeated characters."""
    # Length of longest unique prefix
    prefix_length = 0

    # Set of seen characters
    seen = set()

    # Loop through each character in the string
    for char in s:

        # Check if the character has been seen before
        if char in seen:
            # Break the loop to return the prefix_length
            return prefix_length
        # If the character has not been seen
        else:
            # Increment the prefix length
            prefix_length += 1

            # Save character as seen
            seen.add(char)

    # Return the length of the longest unique prefix
    return prefix_length