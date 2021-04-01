class node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self,head = None):
        self.head = head

def print_linked_list(ll1):
    ptr = ll1.head
    while ptr:
        print(ptr.val , '-->' , end = '')
        ptr = ptr.next
        if(ptr.next == None):
            print(ptr.val)
            break
        
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
        
