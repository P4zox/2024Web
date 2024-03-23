class Car: #建立雙向串列，自訂一個class
    def __init__(self, color):
        self.color = color
        self.previous=None
        self.next=None

# Right traverse the linked list
def rTraverse(head):
    print("start right trverse!")
    ptr=head
    while ptr!=None:
        print('The color of the car is {}'.format(ptr.color))
        ptr=ptr.next
    print('Finish right traverse!')

# Left traverse the linked list
def lTraverse(head):
    print("start left trverse!")
    ptr=head
    while ptr.next!=None:
        ptr=ptr.next
    while ptr!=None:
        print('The color of the car is {}'.format(ptr.color))
        ptr=ptr.previous
    print('Finish left traverse!')

# Initiate the first element of this double linked list
head = Car("red")
ptr = head
ptr.previous = None
ptr.next= None

# Add next element into linked list
new=Car('blue')
ptr.next=new
new.previous = ptr
ptr=new

rTraverse(head)
lTraverse(head)