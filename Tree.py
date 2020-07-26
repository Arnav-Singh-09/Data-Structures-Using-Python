class Tree_Node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        lvl = 0
        p = self.parent
        while p:
            lvl += 1
            p = p.parent
        return lvl

    def print_Tree(self):
        prefix = '  ' * self.get_level()
        if self.parent:
            prefix += '|_..'
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_Tree()

def build_product():
    root = Tree_Node("Electronics")

    laptop = Tree_Node("Laptop")
    laptop.add_child(Tree_Node("Mac"))
    laptop.add_child(Tree_Node("Surface"))
    laptop.add_child(Tree_Node("Thinkpad"))

    cellphone = Tree_Node("Cell Phone")
    cellphone.add_child(Tree_Node("iPhone"))
    cellphone.add_child(Tree_Node("Google Pixel"))
    cellphone.add_child(Tree_Node("Vivo"))

    tv = Tree_Node("TV")
    tv.add_child(Tree_Node("Samsung"))
    tv.add_child(Tree_Node("LG"))

    fridge = Tree_Node("Refridgerator")
    fridge.add_child(Tree_Node("LG"))
    fridge.add_child(Tree_Node("Whirlpool"))
    fridge.add_child(Tree_Node("Samsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    root.add_child(fridge)

    root.print_Tree()

build_product()