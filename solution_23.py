import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        q = []
        if root is not None:
            q.append(root)
        i = 0
        while i < len(q):
            node_i = q[i]
            if node_i.left is not None:
                q.append(node_i.left)
            if node_i.right is not None:
                q.append(node_i.right)
            i +=1
        print(" ".join(str(node.data) for node in q))          


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
