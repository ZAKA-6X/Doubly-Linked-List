
# Doubly Linked List:

### Node Class

The Node class represents each element in the doubly linked list. It has three attributes: data, which stores the value of the node, prev, which points to the previous node in the list, and next, which points to the next node in the list. The init method initializes a node with optional data and sets the prev and next nodes to None by default.

## DoublyLinkedList Class

    The DoublyLinkedList class manages the doubly linked list.
    It has two attributes: head, which points to the first node in the list, and tail, which points to the last node in the list.
    The init method initializes an empty doubly linked list with dummy head and tail nodes.
    The append method adds a new node at the end of the list by traversing the list until it finds the last node.
    The prepend method adds a new node at the beginning of the list.
    The add_element method adds a new node at a specified index in the list.
    The display method prints the elements of the linked list.
    The length method calculates the length of the linked list.
    The delete_by_data method deletes a node with a given data value.
    The delete_by_index method deletes a node at a specified index.
    The get_index method returns the index of a node with a given data value.

### Usage

An instance of DoublyLinkedList is created. Nodes are added to the linked list using the append or prepend method. Various operations such as adding, deleting, and retrieving elements are performed on the linked list.
