class Solution:
    
    def traverseLeaves(self, node, res):
        if node is None:
            return
        
        if not node.left and not node.right:
            res.append(node.data)
            return
        
        self.traverseLeaves(node.left, res)
        self.traverseLeaves(node.right, res)

    def boundaryTraversal(self, root):
        if not root:
            return []

        res = []

        # Root node
        if root.left or root.right:
            res.append(root.data)

        # Left boundary
        curr = root.left
        while curr:
            if curr.left or curr.right:
                res.append(curr.data)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        # Leaf nodes
        self.traverseLeaves(root, res)

        # Right boundary
        temp = []
        curr = root.right

        while curr:
            if curr.left or curr.right:
                temp.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        res.extend(temp[::-1])

        return res