class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Split the path by '/' to get all components
        components = path.split("/")

        # Stack to store valid directory names
        stack = []

        # Process each component
        for dir in components:
            # Ignore empty strings and '.' (current directory)
            if dir == "" or dir == ".":
                continue
            # '..' means go up one directory
            elif dir == "..":
                if stack:
                    stack.pop()  # Remove last directory
            # Valid directory name, add to stack
            else:
                stack.append(dir)

        # Build the simplified path
        result = "/" + "/".join(stack)

        # Return the simplified canonical path
        return result
