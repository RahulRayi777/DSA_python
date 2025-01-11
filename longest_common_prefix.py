class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:  # Handle empty input
            return ""
        
        # Find the shortest string in the list
        shortest = min(strs, key=len)
        
        # Loop through each character in the shortest string
        for i in range(len(shortest)):
            # Compare the character at index i in all strings
            for s in strs:
                if s[i] != shortest[i]:
                    # Return the prefix up to the mismatch
                    return shortest[:i]
        
        # If no mismatch, the entire shortest string is the common prefix
        return shortest

# Examples
solution = Solution()

# Example 1
strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))
