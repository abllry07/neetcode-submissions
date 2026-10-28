/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        if (head == nullptr) {
            return head;
        }
        // recommended time and space = O(n) time & O(1) space
        // to achieve this, we would have to iterate over each node once and manipulate the pointers

        ListNode *prev = nullptr;
        while (head->next != nullptr) { 
            ListNode *temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }
        head->next = prev;
        return head;
    }
};
