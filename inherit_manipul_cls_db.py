class GrandParent:
    def __init__(self):
        self.lst = [1]
        self.child_class = Parent

    def move_to_dest_cls_lst(self, destination_class, index=0):
        destination_class.lst.append(self.lst[index])
        self.lst.remove(self.lst[index])

    def print_lst(self):
        print(self.lst)


class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        self.lst = [2]
        self.parent_class = GrandParent
        self.child_class = Child()


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.lst = [3]
        self.parent_class = Parent
        self.grand_parent_class = GrandParent


