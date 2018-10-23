public class Solution {
	public ListNode reverse(ListNode head) {
		//base case
		if (head == null || head.next == null){
			return head;
		}
		ListNode nextNode = head.next;
		ListNode newHead = this.reverse(nextNode);
		nextNode.next = head;
		head.next = null;
		return newHead;
	}
}