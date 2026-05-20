/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;

        for (int i = 0; i < left - 1; i++){
            prev = curr;
            curr = curr.next;
        }

        ListNode last = null;

        for (int j = 0; j < right - left + 1; j++){
            ListNode temp = curr.next;
            curr.next = last;
            last = curr;
            curr = temp;
        } 

        prev.next.next = curr;
        prev.next = last;

        return dummy.next;


    }
}