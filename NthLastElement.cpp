#include <iostream>
#include "linkedListStructure.h"
using namespace std;

node *lastElement(node *head, int n) {
	node *last = head;
	while(n > 1) {
		head = head->next;
		n--;
	}

	while(head != NULL) {
		head = head->next;
		last = last->next;
	}
	return last;
}

int main() {
	node *head = makenode(1, makenode(2, makenode(3, makenode(4, NULL))));
	node *n = lastElement(head, 2);
	cout << n->val << endl;
}
