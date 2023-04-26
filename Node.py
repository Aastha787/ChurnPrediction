#helper class to store our splits in a node 
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        #constructor for decision node
        
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        
        #constructor for leaf nodes
    def is_leaf(self):
        return self.value is not None