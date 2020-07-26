class BST_Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return
        elif self.data < data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST_Node(data)
        else:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST_Node(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            val = self.left.find_min()
        else:
            val = self.data
        return val

    def find_max(self):
        if self.right:
            val = self.right.find_max()
        else:
            val = self.data
        return val

    def find_sum(self):
        sum = 0
        if self.left:
            sum += self.left.find_sum()
        if self.right:
            sum += self.right.find_sum()
        sum += self.data
        return sum
    
    def delete(self,val):
        if val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        elif val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)
            return self

        def delete_alternate(self, value):
            if value < self.data:
                if self.left:
                    self.left = self.left.delete(value)
            elif value > self.data:
                if self.right:
                    self.right = self.right.delete(value)
            else:
                if self.left is None and self.right is None:
                    return None
                elif self.left is None:
                    return self.right
                elif self.right is None:
                    return self.left
                max_val = self.left.find_max()
                self.data = max_val
                self.left = self.left.delete(max_val)
            return self


def tree_builder(elements):
    root = BST_Node(elements[0])
    for element in elements:
        root.add_child(element)
    return root

countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
country_tree = tree_builder(countries)
print(country_tree.in_order_traversal())
print("UK is in the list? ", country_tree.search("UK"))
print("Sweden is in the list? ", country_tree.search("Sweden"))

numbers_tree = tree_builder([17, 4, 1, 20, 9, 23, 18, 34])
print("In order traversal gives this list:",numbers_tree.in_order_traversal())
print("Pre order traversal gives this list:",numbers_tree.pre_order_traversal())
print("Post order traversal gives this list:",numbers_tree.post_order_traversal())
print("Minimum :",numbers_tree.find_min())
print("Maximum :",numbers_tree.find_max())
print("Sum :",numbers_tree.find_sum())
numbers_tree.delete(20)
print("After deleting 20 ",numbers_tree.in_order_traversal())