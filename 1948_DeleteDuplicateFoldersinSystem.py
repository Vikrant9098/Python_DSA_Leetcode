class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        
        from collections import defaultdict
        
        # Step 1: Build the Trie Tree
        trie = dict()  # Root trie node

        for path in paths:
            node = trie  # Start from the root
            for folder in path:
                if folder not in node:
                    node[folder] = dict()  # Create subfolder if not exists
                node = node[folder]  # Move to the next level

        serial_map = defaultdict(list)  # Maps serialization string to list of nodes

        # Step 2: Serialize each subtree and track duplicates
        def serialize(node):
            if not node:
                return ""  # Empty serialization for leaf

            # Serialize children folders in sorted order to ensure consistency
            serial_parts = []
            for name in sorted(node):
                # Recursively serialize subfolders
                child_serial = serialize(node[name])
                # Append folder name and its serialized subtree
                serial_parts.append(name + "(" + child_serial + ")")
            # Join all parts to create full serialization of the current subtree
            serial = "".join(serial_parts)

            # Track this serialization and associate it with the current node
            serial_map[serial].append(node)

            return serial  # Return the serialization string

        serialize(trie)  # Start serialization from the root

        # Step 3: Mark duplicate folders for deletion
        to_delete = set()
        for serial, nodes in serial_map.items():
            if len(nodes) > 1:
                for node in nodes:
                    to_delete.add(id(node))  # Use id to uniquely identify nodes

        # Step 4: Collect remaining folder paths
        result = []

        def collect_paths(node, path):
            for folder in node:
                child = node[folder]
                # If this node is marked as duplicate, skip it and all its children
                if id(child) in to_delete:
                    continue
                # Include the current folder in path
                new_path = path + [folder]
                result.append(new_path)
                # Recursively collect for children
                collect_paths(child, new_path)

        collect_paths(trie, [])  # Start DFS from the root

        return result
