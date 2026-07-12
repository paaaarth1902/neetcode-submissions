class Solution:
    def sortTwoLists(self, list1, list2):
        temp1 = list1
        temp2 = list2
        newHead = ListNode()
        newTemp = newHead

        while temp1 or temp2:
            if temp1 and not temp2:
                newTemp.next = temp1
                newTemp = newTemp.next
                temp1 = temp1.next
            elif temp2 and not temp1:
                newTemp.next = temp2
                newTemp = newTemp.next
                temp2 = temp2.next
            else:
                if temp1.val <= temp2.val:
                    newTemp.next = temp1
                    newTemp = newTemp.next
                    temp1 = temp1.next
                else:
                    newTemp.next = temp2
                    newTemp = newTemp.next
                    temp2 = temp2.next

        return newHead.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            tempList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                res = self.sortTwoLists(l1, l2)
                tempList.append(res)
            
            lists = tempList
        
        return lists[0]
        