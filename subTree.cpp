#include <iostream>
#include <string>
#include "BSTStructure.h"
using namespace std;

bool match(node *t1, node *t2) {
	if(t1 == NULL && t2 == NULL)
		return true;

	if(t1 == NULL && t2 == NULL)
		return false;

	if(t1->val != t2->val)
		return false;

	return match(t1->left, t2->left) && match(t2->left, t2->right);
}

bool isSubTree(node *t1, node *t2) {
	if(t1 == NULL)
		return false;
	
	if(t1->val == t2->val)
		if(match(t1, t2))
			return true;
	
	return isSubTree(t1->left, t2) || isSubTree(t1->right, t2);
}

int main() {
	return 0;
}
