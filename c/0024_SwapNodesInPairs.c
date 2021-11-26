// Problem: Swap Nodes in Pairs (https://leetcode.com/problems/swap-nodes-in-pairs/)
// Difficulty: Medium
// Date: 2021-11-23

/*
Given a linked list, swap every two adjacent nodes and return its head. You must
solve the problem without modifying the values in the list's nodes (i.e., only
nodes themselves may be changed.)
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void swap(struct ListNode* first, struct ListNode* second){
    int temp = first -> val;
    first -> val = second -> val;
    second -> val = temp;
}

struct ListNode* swapPairs(struct ListNode* head){
    if (head == NULL) { // reached end
        return NULL;
    }
    if (head -> next == NULL) { // odd number
        return head;
    }
    swap(head, head -> next);
    swapPairs((head -> next) -> next); // skip over the front two
    return head;
}