class Node:
    def __init__(self, city_name, population):
        self.city_name = city_name
        self.population = population
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, city_name, population):

        if root is None:
            return Node(city_name, population)

        if city_name < root.city_name:
            root.left = self.insert(
                root.left,
                city_name,
                population
            )

        else:
            root.right = self.insert(
                root.right,
                city_name,
                population
            )

        return root
    def search(self, root, city_name):

        if root is None:
            return None

        if root.city_name == city_name:
            return root

        if city_name < root.city_name:
            return self.search(root.left, city_name)

        return self.search(root.right, city_name)
    def inorder(self, root):

        if root:
            self.inorder(root.left)

            print(
                f"City: {root.city_name}, "
                f"Population: {root.population}"
            )

            self.inorder(root.right)
    

    
# Test code starts here
bst = BST()

bst.root = bst.insert(bst.root, "Kathmandu", 1400000)
bst.root = bst.insert(bst.root, "Pokhara", 600000)
bst.root = bst.insert(bst.root, "Butwal", 200000)

print("Cities inserted successfully!")

result = bst.search(bst.root, "Pokhara")

if result:
    print(f"Found: {result.city_name}")
    print(f"Population: {result.population}")
else:
    print("City not found")
    print("\nAll Cities:")

bst.inorder(bst.root)
