class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Step 1: If the list is empty, return ""
        if not strs:
            return ""

        # Step 2: Start with the first string as prefix
        prefix = strs[0]

        # Step 3: Compare prefix with each word in the list
        for word in strs[1:]:
            # While current word does not start with prefix, shrink prefix
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # Remove last character
                # If prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""

        # Step 4: Return the final common prefix
        return prefix
