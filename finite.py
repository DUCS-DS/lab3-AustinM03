#Austin Metzler
from llist import LList, Node, append
from genfinite import lst

def length(lst):
    count = 1
    if lst.head:
        node = lst.head
        while node.next:
            node = node.next
            count += 1
    else:
        return "You Messed Up"
    return count

def llprint(lst):
    if lst.head:
        node = lst.head
        while node.next:
            node = node.next
            print(node.val)
    else:
        return "You Messed up"

if __name__ == "__main__":
    llist = LList()
    append(llist, Node(1))
    append(llist, Node(2))
    append(llist, Node(4))
    append(llist, Node(8))
    append(llist, Node(16))
    append(llist, Node(32))
    append(llist, Node(64))
    append(llist, Node(128))
    append(llist, Node(256))
    append(llist, Node(512))
    print(length(llist))
    llprint(llist)
    print(length(llist))
