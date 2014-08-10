#include "iostream"
#include "BSTStructure.h"
using namespace std;

void widthHelp(node* root, int curr, int& min, int& max) {
  if(root == NULL)
    return;

  if(curr < min)
    min = curr;

  if(curr > max)
    max = curr;

  widthHelp(root->left, curr - 1, min, max);
  widthHelp(root->right, curr + 1, min, max);
}

int width(node* root) {
  int min = 0;
  int max = 0;

  widthHelp(root, 0, min, max);
  return max - min;
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
  printBST(root);
  cout << width(root) << endl;
  return 0;
}
