#node class for creating node object
class node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

#to create linked list object
class linkedlist:
    def __init__(self,head = None):
        self.head = head
#function for printing sll
def print_linked_list(ll1):
    ptr = ll1.head
    while ptr:
        print(ptr.val , '-->' , end = '')
        ptr = ptr.next
        if(ptr.next == None):
            print(ptr.val)
            break
#function for printing reversal of sll
#reversing using two pointers
def printing_reversed_linked_list(ll1):
    if(ll1.head==None):
        print("empty linkedlist")
    elif(ll1.head.next == None):
        print(ll1.head.val)
    else:
        ptr1 = ll1.head
        ptr2 = ptr1.next
        ll1.head = ptr2
        ptr1.next = None
        while ll1.head:
            ll1.head = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ll1.head
    
    ll1.head = ptr1
    print_linked_list(ll1)
        
        
if __name__ == '__main__':
    l1 = linkedlist()
    n = int(input("enter number of nodes:"))
    for i in range(0,n):
        if(l1.head == None):
            l1.head = node(int(input("enter node value:")))
            p1 = l1.head
        else:
           p1.next = node(int(input("enter node value:")))
           p1 = p1.next
    print_linked_list(l1)
    printing_reversed_linked_list(l1)
    
        
