'''
Given two sorted linked lists, merge them so that the resulting linked list is also sorted. 
Consider two sorted linked lists and the merged list below them as an example.

head1 ->  4 -> 8 -> 15 -> 19 -> Null
head2 -> 7 -> 9 -> 10 -> 16 -> Null
head1 -> 4 -> 7 -> 8 -> 9 -> 10 -> 16 -> 19 -> Null
'''

def merge_sorted(head1, head2):
  if head1 == None:
    return head2
  elif head2 == None:
    return head1
  
  mergedHead = None
  if head1.data <= head2.data:
    mergedHead = head1
    head1 = head1.next
  else:
    mergedHead = head2
    head2 = head2.next

  mergedTail = mergedHead

  while head1 != None and head2 != None:
    temp = None
    if head1.data <= head2.data:
      temp = head1
      head1 = head1.next
    else:
      temp = head2
      head2 = head2.next

    mergedTail.next = temp
    mergedTail = temp

  if head1 != None:
    mergedTail.next = head1
  elif head2 != None:
    mergedTail.next = head2
  return mergedHead

#tested in browser