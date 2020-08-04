
public class Test21_cwk {

	public static void main(String[] args) {
		ListNode21 node1 = new ListNode21(1);
		node1.next = new ListNode21(2);
		node1.next.next = new ListNode21(4);
		
		ListNode21 node2 = new ListNode21(1);
		node2.next = new ListNode21(3);
		node2.next.next = new ListNode21(4);
		
		System.out.println(node1);
		System.out.println(node2);
		
		Solution21 solution = new Solution21();
		ListNode21 mergeNode21 = solution.mergeTwoLists(node1, node2);
		System.out.println(mergeNode21);
		
	}

}

class Solution21 {
	public ListNode21 mergeTwoLists(ListNode21 l1, ListNode21 l2) {
		// 최종 return 할 ListNode
		ListNode21 mergeNode = new ListNode21();
		ListNode21 tempNode = mergeNode;
		
		int val = 0;
		
		ListNode21 node1 = l1;
		ListNode21 node2 = l2;
		
		while(node1 != null && node2 != null)
		{
			if(node1.val <= node2.val) 
			{
				val = node1.val;
				node1 = node1.next;
			} 
			else {
				val = node2.val;
				node2 = node2.next;
			}
			ListNode21 node = new ListNode21(val, null);
			tempNode.next = node;
			tempNode = tempNode.next;
			
		}
		if(node1 == null) {
			tempNode.next = node2;
		} 
		else if(node2 == null) {
			tempNode.next = node1;
		}
		
		return mergeNode.next;
	}
}

class ListNode21 {
	int val;
	ListNode21 next;
	public ListNode21() {}
	public ListNode21(int val) {
		this.val = val;
	}
	public ListNode21(int val, ListNode21 next) {
		this.val = val;
		this.next = next;
	}
	
	@Override
	public String toString() {
		String str = "";
		ListNode21 node = this;
		
		str += this.val;
		node = this.next;
		
		while (node != null) 
		{
			str += " -> " + node.val;
			node = node.next;
		}
		
		return str;
	}
	
	
	
}