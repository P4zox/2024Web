#Step 1，需自訂一個類別(Class)
class Car: 
    def __init__(self, color):
        self.color = color
        self.next = None

# Traverse the linked list
def traverse(head):
    ptr = head
    while True:
        print('The color of the car is {}.'.format(ptr.color))
        if ptr.next==head:
            break
        ptr= ptr.next
    print('Finish traverse')

# Step 2，Initiate the first element of the linkede list
head = Car("red")
ptr = head
ptr.next = None
# Add next element into linked list
new_data=Car("blue")
ptr.next= new_data
new_data.next=head
ptr=new_data

traverse(head)