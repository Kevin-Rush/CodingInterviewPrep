'''
4. Copy linked list with arbitrary pointer
You are given a linked list where the node has two pointers. The first is the regular next pointer. 
The second pointer is called arbitrary_pointer and it can point to any node in the linked list. Your 
job is to write code to make a deep copy of the given linked list. Here, deep copy means that any operations 
on the original list should not affect the copied list.
'''

def deep_copy_arbitrary_pointer(head):
   if head == None:
      return None
   
   originalCurrent = head 
   new_head = None
   new_prev = None
   hashTable = dict()
    #making a copy
   while originalCurrent != None:
      new_node = LinkedListNode(originalCurrent.data) #make new_node an actual LinkedListNode object NOT a node equal to originalCurrent
      new_node.arbitrary = originalCurrent.arbitrary #give the new node the same pointer as originalCurrent

      if new_prev != None:
         new_prev.next = new_node 
      else:
         new_head = new_node
      
      hashTable[originalCurrent] = new_node #save originalCurrent in the hashMap as equal to new_node
      new_prev = new_node
      originalCurrent = originalCurrent.next #move to the next node in the original list
   
   new_originalCurrent = new_head

   while new_originalCurrent != None:
      if new_originalCurrent.arbitrary != None:
         node = hashTable[new_originalCurrent.arbitrary]
         new_originalCurrent.arbitrary = node
      new_originalCurrent = new_originalCurrent.next
   
   return new_head