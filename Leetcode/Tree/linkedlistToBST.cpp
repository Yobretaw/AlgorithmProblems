#include "iostream"
#include "vector"
#include "stack"
#include "BSTStructure.h"
using namespace std;

node* linkedListToBST(node*& list, int start, int end) {
  if(start > end) {
    return NULL;
  }

  int mid = start + (end - start) / 2;
  node* leftChild = linkedListToBST(list, start, mid - 1);
  node* parent = new node(list->val, leftChild, NULL);

  list = list->next;
  parent->right = linkedListToBST(list, mid + 1, end);

  return parent;
}

node* arrayToBST(vector<int>& a, int start, int end) {
  static int idx = 0;

  if(start > end)
    return NULL;

  int mid = start + (end - start) / 2;
  node* leftChild = arrayToBST(a, start, mid - 1);
  node* parent = new node(a[idx], leftChild, NULL);

  idx++;
  parent->right = arrayToBST(a, mid + 1, end);

  return parent;
}

node* arrayToBSTwithoutRecursion(vector<int>& a) {
  return NULL;
}

int main()
{
  node* l1 = new node(1);
  node* l2 = new node(2);
  node* l3 = new node(3);
  node* l4 = new node(4);
  node* l5 = new node(5);
  node* l6 = new node(6);
  node* l7 = new node(7);
  node* l8 = new node(8);

  l1->next = l2;
  l2->next = l3;
  l3->next = l4;
  l4->next = l5;
  l5->next = l6;
  l6->next = l7;
  l7->next = l8;

  vector<int> a = {1, 2, 3, 4, 5, 6, 7, 8};

  //node* root = linkedListToBST(l1, 0, 7);
  node* root = arrayToBST(a, 0, 7);
  printBST(root);
  return 0;
}
