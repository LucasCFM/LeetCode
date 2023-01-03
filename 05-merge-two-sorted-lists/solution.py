from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        print(list1)
        print(list2)

        first_node_1 = list1.val
        first_node_2 = list2.val

        if first_node_1 <= first_node_2:
            result_list = ListNode(val = first_node_1)
            result_list.next = self.doMergeTowList(list1.next, list2, result_list.next)
        else:
            result_list = ListNode(val = first_node_2)
            result_list.next = self.doMergeTowList(list2.next, list1, result_list.next)
        
        return result_list

    def doMergeTowList(self, starter_list: Optional[ListNode], another_list: Optional[ListNode], result_list: Optional[ListNode]) -> List[Union[ListNode, 'doMergeTowList']]:
        if not starter_list:
            result_list = another_list
            return result_list
        
        if not another_list:
            result_list = starter_list
            return result_list

        if starter_list.val <= another_list.val:
            result_list = ListNode(val = starter_list.val)
            result_list.next = self.doMergeTowList(starter_list.next, another_list, result_list.next)
        else:
            result_list = ListNode(val = another_list.val)
            result_list.next = self.doMergeTowList(starter_list, another_list.next, result_list.next)
        
        return result_list
