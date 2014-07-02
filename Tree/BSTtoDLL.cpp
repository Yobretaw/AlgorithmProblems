#include <iostream>
#include <BSTStructure.h>
using namespace std;

node* help(node*, node*&, node*&);

node* BSTtoDLL(node* root) {
  node* head = NULL;
  node* pre = NULL;
  return help(root, pre, head );
}

node* help(node* curr, node*& pre, node*& head) {
  if(root == NULL) return NULL;

  help(current->left, pre, head);
  curr->left = pre;
  if(pre == NULL)
    head = current;
  else
    pre->right = current;
  
  node* right = current->right;
  head->left = current;
  current->right = head;

  pre = current;
  help(right, pre, head);
}

int main()
{
  node* root = new node(7, 
      new node(3, 
        new node(1, 
          new node(0, NULL, NULL),
          new node(2, NULL, NULL)),
        new node(5,
          new node(4, NULL, NULL),
          new node(6, NULL, NULL))),
      new node(11,
        new node(9,
          new node(8, NULL, NULL),
          new node(10, NULL, NULL)),
        new node(13,
          new node(12, NULL, NULL),
          new node(14, NULL, NULL))));

  node* dll = BSTtoDLL(root);
  node* head = dll;
  while(dll && dll->next != head) {
    cout << dll->val << end;
  }

  return 0;
}


