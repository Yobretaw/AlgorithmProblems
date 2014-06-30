//==============================================================
// Given two numbers represented by a linked list, where each node
// contains a single digit. The digits are stored in reverse order,
// such that the 1's digit is at the head of the list. Write a
// function that adds the two numbers and return the sum as a 
// linked list
// 
// Example
// input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
// output: 8 -> 0 -> 8
//==============================================================

#include <iostream>
#include "linkedListStructure.h"
using namespace std;

node* sum1(node *a, node* b, int carryup);

node* sum(node *a, node *b, int upper_digit = 0) {
	if(a == NULL && b == NULL) {
		if(upper_digit == 0)
			return NULL;
		return makenode(upper_digit, NULL);
	}
	int curr_val = upper_digit;
	if(a != NULL) curr_val += a->val;
	if(b != NULL) curr_val += b->val;
	return makenode(curr_val % 10, sum(a==NULL?NULL:a->next, b==NULL?NULL:b->next, curr_val / 10));
}


node* sum1(node* a, node* b, int carryup = 0) {
	if(!a && !b && !carryup) return NULL;
	if(!a && !b) return makenode(1, NULL);

	int v1 = a?a->val:0;
	int v2 = b?b->val:0;

	return makenode((v1+v2+carryup)%10, sum1(a?a->next:NULL, b?b->next:NULL, (v1+v2+carryup)/10));
}

/*
node *sum(node *a, node *b) {
	int val = (a->val + b->val);
	int upper_digit = val / 10;

	node *ret = makenode(val % 10, NULL);
	a = a->next;
	b = b->next;

	while(a != NULL && b != NULL) {
		val = a->val + b->val + upper_digit;
		upper_digit = val / 10;
		ret = makenode(val % 10, ret);
		a = a->next;
		b = b->next;
	}

	if(a == NULL && b == NULL) {
		if(upper_digit == 0) {
			return ret;
		}
		ret = makenode(upper_digit, ret);
		return ret;
	}
	node *notNULL = (a == NULL)? a:b;
	val = notNULL->val + upper_digit;
	upper_digit = val / 10;
	ret = makenode(upper_digit, makenode(val % 10, NULL));
	return ret;
}
*/

int main() {
	node *a = makenode(3, makenode(1, makenode(5, makenode(3, NULL))));
	node *b = makenode(5, makenode(9, makenode(2, makenode(7, NULL))));
	node *c = sum1(a, b);
	printNode(c);
}

