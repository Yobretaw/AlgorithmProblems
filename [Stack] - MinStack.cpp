#include <iostream>
using namespace std;

struct node {
	int val;
	node* next;
};

struct MinStack {
	node* stack;
	node* minStack;
};

node* makenode( int val, node* next );
void push( MinStack* ms, int val );
int pop( MinStack* ms );
int getMin( MinStack* ms );

node* makenode( int val, node* next ) {
	node* newnode = new node;
	newnode->val = val;
	newnode->next = next;
	return newnode;
}

void push( MinStack* ms, int val ) {
	if( ms->stack == NULL ) {
		ms = new MinStack;
		ms->stack = makenode(val, NULL);
		ms->minStack = makenode(val, NULL);
		return;
	}
	else {
		ms->stack = makenode(val, ms->stack);
		if( val < getMin(ms) )
			ms->minStack = makenode(val, ms->minStack);
	}
}

void push( Minstack* ms, int val) {
	if( ms->stack == NULL) {
		ms = new MinStack;
		ms->stack = makenode(val, NULL);
		ms->minStack = makenode(val, NULL);
	}
}

int pop( MinStack* ms ) {
	if( ms->stack->val > ms->minStack->val ) {
		node* popnode = ms->stack;
		ms->stack = ms->stack->next;
		int retval = popnode->val;
		delete popnode;
		return retval;
	}
	else {
		node* popnode = ms->stack;
		node* minpopnode = ms->minStack;
		int retval = popnode->val;
		ms->stack = ms->stack->next;
		ms->minStack = ms->minStack->next;
		return retval;
	}
}

int getMin( MinStack* ms ) {
	return ms->minStack->val;
}

int main() {
	MinStack* ms = new MinStack;

	push(ms, 2);
	push(ms, 6);
	push(ms, 4);
	push(ms, 1);
	push(ms, 5);

	cout << "min: " << getMin(ms) << endl;
	cout << "pop: " << pop(ms) << endl;

	cout << "min: " << getMin(ms) << endl;
	cout << "pop: " << pop(ms) << endl;

	cout << "min: " << getMin(ms) << endl;
	cout << "pop: " << pop(ms) << endl;

	cout << "min: " << getMin(ms) << endl;
	cout << "pop: " << pop(ms) << endl;

	cout << "min: " << getMin(ms) << endl;
	cout << "pop: " << pop(ms) << endl;

	delete ms;
}



