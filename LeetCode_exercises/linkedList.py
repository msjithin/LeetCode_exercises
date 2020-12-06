""" 
    Contains classes for single linked lists node,
    double linked list node and single linked node 
"""
"""
    add index()
    add insert()
    check problem solving with algorithms and data strc using python

"""

class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a representation for the node"""
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """Replace existing value of self.data attribute with new_data"""
        self.data = new_data

    def get_next(self):
        """Return self.next attribute """
        return self.next

    def set_next(self, new_next):
        """Replace existing value of self.next attribute with new_next"""
        self.next = new_next





class DLLNode:
    """ Doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a representation for the node"""
        return "DLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """Replace existing value of self.data attribute with new_data"""
        self.data = new_data

    def get_next(self):
        """Return self.next attribute """
        return self.next
    
    def get_previous(self):
        """Return self.previous attribute """
        return self.previous

    def set_next(self, new_next):
        """Replace existing value of self.next attribute with new_next"""
        self.next = new_next

    def set_previous(self, new_previous):
        """Replace existing value of self.previous attribute with new_previous"""
        self.previous = new_previous


class SLL:
    def __init__(self):
        self.head = None
    def __repr__(self):
        return "SLL object : head={} ".format(self.head)

    def is_empty(self):
        """Retruns True if linked list is empty, otherwise False """
        return self.head is None
         
    def add_front(self, new_data):
        """ Add a node whose data is teh new_data
        to the front of the linked list"""
        tmp = SLLNode(new_data)
        tmp.set_next(self.head)
        self.head = tmp

    def size(self):
        """Traverses the linked list 
        and returns an integer value representing
        the number of nodes in the Linked List
        Time complexity = O(n)
        because every node in the linked list must be visited
        
        """
        size=0
        if self.head is None :
            return 0
        current = self.head
        while current is not None:
            # while there are still nodes left to count
            size += 1
            current = current.get_next()
        return size

    def search(self, data):
        """ Traverses the linked list and returns True if data searched
        for is present in one of the Nodes, else False
        Time complexity = O(n)
        """
        if self.head is None:
            return "Linked List is empty, no node to search"
        current = self.head
        while current is not None:
            #1. the nodes data matches what we look for
            if current.get_data() == data :
                return True
            #2. the nodes data doesnt match
            else :
                current = current.get_next()
        return False


    def remove(self, data):
        """ 
        Removes first occurence of node that contains the data argument
        as its self.data variable. Returns nothin.
        Time complexity = O(n)
        """
        # if node is empty
        if self.head is None :
            return "Linked list is empty, no node to remove "
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data :
                found=True
            else :
                if current.get_next() == None:
                    return "Node with data value is not present"
                else :
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
          

class DLL:
    def __init__(self):
        self.head = None
    def __repr__(self):
        return "<DLL object : head=>{} ".format(self.head)

    def is_empty(self):
        """Retruns True if linked list is empty, otherwise False """
        return self.head is None
         
    def add_front(self, new_data):
        """ Add a node whose data is teh new_data
        to the front of the linked list"""
        tmp = DLLNode(new_data)
        tmp.set_next(self.head)
        ## now, DLLNode has next and previous
        # we need to separate the cases if the previous is None or not
        if self.head is not None:
            self.head.set_previous(tmp)
        self.head = tmp

    def size(self):
        """Traverses the linked list 
        and returns an integer value representing
        the number of nodes in the Linked List
        Time complexity = O(n)
        because every node in the linked list must be visited
        
        """
        size=0
        if self.head is None :
            return 0
        current = self.head
        while current is not None:
            # while there are still nodes left to count
            size += 1
            current = current.get_next()
        return size

    def search(self, data):
        """ Traverses the linked list and returns True if data searched
        for is present in one of the Nodes, else False
        Time complexity = O(n)
        """
        if self.head is None:
            return "Linked List is empty, no node to search"
        current = self.head
        while current is not None:
            #1. the nodes data matches what we look for
            if current.get_data() == data :
                return True
            #2. the nodes data doesnt match
            else :
                current = current.get_next()
        return False


    def remove(self, data):
        """
        Removes the first occurence of a Node that contains the data 
        argument as its self.data attribute. Returns nothing.
        Time complexity O(n) -- we have to visit all nodes if data is not in the list
        Edge cases :
        1. empty linked list : head -> None
        2. target data not found  : say remove berry
        3. If remove first node
        4. remove inbetween node
        """
        if self.head is None:
            return "Linked list is empty, no node to remove"
        current = self.head  # keep track of current node we are looking at, first time this is the first node, what head points to
        found = False
        while not found:
            if current.get_data()==data :
                found = True
            else:
                #if we reached last node
                if current.get_next() is None:
                    return "A node with that data value is not present"
                else:
                    current = current.get_next()
        # check if the node if first node
        if current.previous is None:
            self.head = current.get_next()
        # if its some inbetween node
        else: 
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())






    