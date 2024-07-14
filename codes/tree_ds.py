class TreeNode:
    
    def __init__(self, data: str, children: list = []):
        self.data = data
        self.children = children
        
    def __str__(self, level = 0) -> str:
        ret = " " * level + str(self.data) + '\n'
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChildren(self, TreeNode):
        self.children.append(TreeNode)
    
    
tree = TreeNode('Drinks',[])

cold = TreeNode('Cold', [])

hot = TreeNode('Hot', [])

tree.addChildren(cold)  

tree.addChildren(hot)

tea = TreeNode('tea', [])

coffee = TreeNode('coffee',[])

cola = TreeNode('cola',[])

fanta = TreeNode('fanta',[])

cold.addChildren(fanta)
cold.addChildren(cola)

hot.addChildren(tea)

hot.addChildren(coffee)

print(tree)
