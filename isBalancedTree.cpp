//=========================================
// Check if the given BST is balanced
//=========================================
#include <iostream>
#include <stdlib.h>
#include "BSTStructure.h"
using namespace std;

bool isBalanced_help(node *root, int& num) {
	if(root == NULL) {
		num = 0;
		return true;
	}

	int left = 0; 
	int right = 0;
	bool isLeftBalanced = isBalanced_help(root->left, left);
	bool isRightBalanced = isBalanced_help(root->right, right);

	if(isLeftBalanced && isRightBalanced && abs(left - right) <= 1)
		return true;

	num = max(left, right);
	return false;
}

bool isBalanced(node *root) {
	int num;
	return isBalanced_help(root, num);
}

int main() {
	node *n1 = makeBST(1, NULL, NULL);
	node *n7 = makeBST(7, NULL, NULL);
	node *n5 = makeBST(5, NULL, NULL);
	node *n15 = makeBST(15, NULL, NULL);
	node *n22 = makeBST(22, NULL, NULL);
	node *n9 = makeBST(9, NULL, NULL);
	node *n6 = makeBST(6, n5, n7);
	node *n8 = makeBST(8, NULL, n9);
	node *n20 = makeBST(20, n15, n22);
	node *n2 = makeBST(2, n1, n8);
	node *n10 = makeBST(10, n2, n20);
	cout << isBalanced(n10) << endl;
}
