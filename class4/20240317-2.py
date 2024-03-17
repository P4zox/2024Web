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

# 新節點插入第一節點之前，成為單向串列的首節點
new=Car("black")
new.next=head
ptr=head
while ptr.next != head:
    ptr=ptr.next
ptr.next=new
head=new

# 將新節點X插在串列中任意節點I之後
x=Car("pink")
ptr=head
while ptr.color != "red":
    ptr=ptr.next
x.next= ptr.next
ptr.next=x

# 刪除環狀列的第一個節點
ptr=head
while ptr.next!=head:
    ptr=ptr.next
head=head.next
ptr.next=head

# 刪除環狀列的中間節點
ptr=head
while ptr.next.color != "pink":
    ptr=ptr.next
ptr.next=ptr.next.next

traverse(head)