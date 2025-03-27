class Listnode:
    # define listnode
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next
    
class solution:
    def addtwonums(self,l1,l2):# define addtwonums
        dummy=Listnode()
        current=dummy
        carry=0

        while l1 or l2 or carry:
            # get the values of l1 and l2
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            # add the values and carry
            total=val1+val2+carry

            carry=total//10
            # create a new node with the value of the total
            current.next=Listnode(total%10)
            # move to the next node
            current= current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
# next lets create a linked list
def create_linked_list(lst):
    # initialize the head of linked list 
    dummy=Listnode()
    curr=dummy
    for num in lst: #iterate through the lists values and add the values to the linked list
        curr.next=Listnode(num) 
        # move to the mext listnode
        curr=curr.next
    return dummy.next
def print_ll(node):
    v=[]#values list
    while node:#if node not empty meaning not 0 or -1
        v.append(str(node.val))#add value that is stored in that node to the list
        node=node.next#move to the next node 
    print("->".join(v)) #join them and print as a string   
listone=create_linked_list([2,4,3])
listtwo=create_linked_list([5,6,4])
k=solution()
r=k.addtwonums(listone,listtwo)
print_ll(r)
