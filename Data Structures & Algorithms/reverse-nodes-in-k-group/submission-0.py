class Solution:

    def reverse(self, head, tail):
        connecter = tail.next
        prev = None
        curr = head

        while curr != connecter:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head.next = connecter
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head
        curr = head
        cnt = 0

        while curr:
            cnt += 1
            curr = curr.next

        numOfRevs = cnt // k

        if numOfRevs == 0:
            return head
        else:
            dummy = ListNode()
            dummy.next = head
            prevTail = dummy

            currHead = head
            currTail = head
            cnt = 1

            while numOfRevs > 0:
                if cnt % k == 0:
                    
                    newHead = currTail.next
                    oldHead = currHead

                    if not currHead:
                        break

                    res = self.reverse(currHead, currTail)

                    prevTail.next = res
                    prevTail = oldHead

                    currHead = newHead
                    currTail = newHead
                
                    numOfRevs -= 1
                    cnt = 1  
                else:
                    if currTail is None:
                        break
                    currTail = currTail.next
                    cnt += 1
                    
            return dummy.next