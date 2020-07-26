class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = Node(data, None)

    def print_list(self):
        if self.head is None:
            print("Linked list is empty. :(")
        else:
            itr = self.head
            print("Head", end="->")
            while itr is not None:
                print(itr.data, end = "->")
                itr = itr.next
            print("Tail")

    def length(self):
        count = 0
        itr = self.head
        while itr is not None:
            count += 1
            itr = itr.next
        return count

    def remove_at_beg(self):
        if self.head is None:
            print("Empty List")
        else:
            self.head = self.head.next

    def remove_at_end(self):
        if self.head is None:
            print("Empty List")
        else:
            curr = self.head
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None

    def remove_by_index(self, index):
        if (index < 0) or (index > self.length()):
            print("Invalid Index Value!!!")
        elif index == 0:
            self.remove_at_beg()
        elif index == (self.length() - 1):
            self.remove_at_end()
        elif self.head is None:
            print("Empty List")
        else:
            curr = self.head
            count = 0
            while count != index:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = curr.next

    def remove_all_occurence(self, value):
        flag = 0
        if self.head is None:
            print("Empty List")
        elif self.head.data == value:
            self.remove_at_beg()
            flag = 1
            self.remove_all_occurence(value)
        else:
            curr = self.head
            while curr is not None:
                prev = curr
                if curr.data == value:
                    prev.next = curr.next
                    flag = 1
                curr = curr.next
        if flag == 0:
            print("List is now {} free.".format(value))

    def remove_first_occurence(self, value):
        flag = 0
        if self.head is None:
            print("Empty List")
        elif self.head.data == value:
            self.remove_at_beg()
            flag = 1
        else:
            curr = self.head
            while curr is not None:
                prev = curr
                if curr.data == value:
                    prev.next = curr.next
                    flag = 1
                    break
                curr = curr.next
        if flag == 0:
            print(value, "not present in List !!!")

    def remove_last_occurence(self, value):
        if self.head is None:
            print("Empty List")
        else:
            index = []
            count = 0
            curr = self.head
            while curr is not None:
                if curr.data == value:
                    index.append(count)
                count += 1
                curr = curr.next
            if len(index) == 0 :
                print(value,"not in list")
            elif len(index) == 1:
                self.remove_by_index(index[0])
            else:
                self.remove_by_index(index[-1])

    def insert_at_index(self, data, index):
        if (index < 0) or (index > self.length()):
            print("Invalid Index Value!!!")
        elif index == 0:
            self.insert_at_beg(data)
        elif index == (self.length()):
            self.insert_at_end(data)
        elif (index > 0) and (self.head is None):
            print("Empty List")
        else:
            curr = self.head
            count = 0
            while count != index:
                prev = curr
                curr = curr.next
                count += 1
            node = Node(data, curr)
            prev.next = node

    def insert_after(self, value, data):
        flag = 0
        if self.head is None:
            print("Empty List")
        else:
            curr = self.head
            nxt = curr.next
            while curr is not None:
                if curr.data == value:
                    curr.next = Node(data, nxt)
                    flag = 1
                    break
                curr = curr.next
                nxt = curr.next
        if flag == 0:
            print(value, "not in List")

    def insert_before(self, value, data):
        flag = 0
        if self.head is None:
            print("Empty List")
        elif self.head.data == value:
            self.insert_at_beg(data)
        else:
            prev = self.head
            curr = prev.next
            while curr is not None:
                if curr.data == value:
                    prev.next = Node(data, curr)
                    flag = 1
                    break
                prev = curr
                curr = curr.next
        if flag == 0:
            print(value, "not in List")

l_1 = ['Banana','Apple','Grapes','Orange']
link_list_1 = Linked_List()
link_list_2 = Linked_List()
for data in l_1:
    link_list_1.insert_at_beg(data)
    link_list_2.insert_at_end(data)
link_list_1.print_list()
link_list_2.print_list()
print(link_list_2.length())
link_list_2.insert_at_index("Banana", 3)
link_list_2.print_list()
link_list_2.insert_after("Orange", "Peach")
link_list_2.print_list()