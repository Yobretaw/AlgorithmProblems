#include <iostream>
#include <stdlib.h>
#include "BSTStructure.h"
using namespace std;

void maxPathSumHelper(node *root, int& currentSum, int& maxSum);

int manPathSum(node *root) {
	int currentSum = 0;
	int maxSum = INT_MIN;

	maxPathSumHelper(root, currentSum, maxSum);
	return maxSum;
}

void maxPathSumHelper(node *root, int& currentSum, int& maxSum) {
	if(root == NULL) {
		currentSum = 0;
		return;
	}

	int leftSum = 0, rightSum = 0;
	maxPathSumHelper(root->left, leftSum, maxSum);
	maxPathSumHelper(root->right, rightSum, maxSum);

	currentSum = max(root->val, max(root->val + leftSum, root->val + rightSum));
	maxSum = max(maxSum, currentSum, root->val + leftSum + rightSum);
}

