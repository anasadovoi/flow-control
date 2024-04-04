# [HEAD]-- next -->[VALUE1]-- next -->[VALUE2]-- next --> None

class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
  def __str__(self)  :
    return f"[{self.value}]-- next --> {self.next}"


head = Node(100)
# print(head)
# #Add new nodes (200,300,400,500)
# head.next = Node(200)
# head.next.next = Node(300)
# head.next.next.next = Node(400)
# head.next.next.next.next = Node(500)
#print(head)
print('#########')

# add the values through a loop
h = head
for value in [200,300,400,500]:
  h.next = Node(value)
  h = h.next
h = head
while h:
  print(h)
  h = h.next
  break

