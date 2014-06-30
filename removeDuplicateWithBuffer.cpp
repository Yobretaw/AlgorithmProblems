//=================================================================
// Remove any duplicate in the given linkedlist and keey the one that
// occures first, a buffer can be used
//
// idea: using a hashtable to store previously node and check if it
// has appeared
//
// Runtime: O(n)
//=================================================================
#include <iostream>
#include <string>
#include <tr1/unordered_map>
#include "linkedListStructure.h"
using namespace std;
using namespace tr1;

void remove(node *head) {
	if(head == NULL)
		return;

	unordered_map<int, bool> table;
	table[head->val] = true;

	while(head != NULL && head->next != NULL) {
		int val = head->next->val;
		if(table[val] == false) {
			table[val] = true;
			head = head->next;
		}
		else {
			node *copy = head->next;
			head->next = head->next->next;
			delete copy;
		}
	}
}

int main() {
	node *head = makenode(2, NULL);
	int i;
	while(cin >> i) {
		head = makenode(i, head);
	}
	printNode(head);
	cout << endl;
	remove(head);
	printNode(head);
	deleteNode(head);
}


