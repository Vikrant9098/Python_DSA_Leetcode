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
import java.util.PriorityQueue;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // if no list is given, return null
        if (lists == null || lists.length == 0) return null;
        
        // min-heap (priority queue) to store smallest node from each list
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        
        // add first node of each non-empty list into the heap
        for (ListNode node : lists) {
            if (node != null) pq.offer(node);
        }
        
        // dummy node to start the merged list
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy; // tail keeps track of end of merged list
        
        // while heap is not empty
        while (!pq.isEmpty()) {
            // remove the smallest node from heap
            ListNode minNode = pq.poll();
            
            // attach it to the merged list
            tail.next = minNode;
            tail = tail.next; // move tail forward
            
            // if the node has a next node, add it to heap
            if (minNode.next != null) {
                pq.offer(minNode.next);
            }
        }
        
        // return merged list starting from dummy.next
        return dummy.next;
    }
}
