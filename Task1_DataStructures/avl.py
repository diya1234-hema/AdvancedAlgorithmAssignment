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

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        x.height = 1 + max(
            self.get_height(x.left),
            self.get_height(x.right)
        )

        return x

    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(
            self.get_height(x.left),
            self.get_height(x.right)
        )

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        return y

    def insert(self, root, city_name, population):

        if not root:
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

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and city_name < root.left.city_name:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and city_name > root.right.city_name:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and city_name > root.left.city_name:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and city_name < root.right.city_name:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)

            print(
                f"City: {root.city_name}, "
                f"Population: {root.population}"
            )

            self.inorder(root.right)


