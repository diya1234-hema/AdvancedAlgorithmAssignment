class Node:
    def __init__(self, city_name, population):
        self.city_name = city_name
        self.population = population

        self.left = None
        self.right = None

        self.height = 1
        
class AVLTree:
    def __init__(self):
        self.root = None
    def get_height(self, node):

     if not node:
        return 0

     return node.height    
    
    