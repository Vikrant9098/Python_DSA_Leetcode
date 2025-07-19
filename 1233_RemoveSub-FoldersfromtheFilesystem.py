class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        # Step 1: Sort the folders lexicographically
        folder.sort()
        
        res = []  # Result list to hold top-level folders only
        
        for f in folder:
            # If res is empty or current folder f is not a subfolder of the last added folder
            # We check if f starts with the last folder + "/", which indicates it's a subfolder
            if not res or not f.startswith(res[-1] + "/"):
                res.append(f)  # Not a subfolder, so keep it
        
        return res
