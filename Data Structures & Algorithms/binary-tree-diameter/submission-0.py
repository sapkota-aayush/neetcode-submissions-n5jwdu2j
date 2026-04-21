class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0  # initialize global answer

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # update diameter
            self.ans = max(self.ans, left + right)

            # return height
            return 1 + max(left, right)

        dfs(root)
        return self.ans