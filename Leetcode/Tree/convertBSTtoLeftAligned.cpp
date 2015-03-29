#include "iostream"
#include "vector"

#include "BSTStructure.h"
using namespace std;

// ==========================================
// Convert the tree below
//
//                A
//              /   \
//             B	   C
//			           /   \
// 			          D      E
//		           /     /   \
//		          F    G      H 
// 
// to 
//
//      A
//		  |
//			B – C
//			|
//			D—E
//			|
//			F—G – H

void traversal(node* root, int level, vector<vector<node*> >& store) {
  if(root == NULL)
    return;

  if((int)store.size() < level + 1)
    store.push_back(vector<node*>());

  store[level].push_back(root);
  traversal(root->left, level+1, store);
  traversal(root->right, level+1, store);
}

void convert(node* root) {
  if(root == NULL)
    return;

  vector<vector<node*> > level;
  traversal(root, 0, level);

  // set down pointer
  int i;
  for(i = 0; i < (int)level.size()-1; i++) {
    level[i][0]->left = level[i+1][0];
  }

  for(int i = 1; i < (int)level.size(); i++) {
    int j;
    for(j = 0; j < (int)level[i].size()-1; j++) {
      if(j >= 1)
        level[i][j]->left = NULL;
      level[i][j]->right = level[i][j+1];
    }

    level[i][j]->left = NULL;
    level[i][j]->right = NULL;
  }

  level[0][0]->right = NULL;
  level[i][0]->left = NULL;
}

int main()
{
  node* root = new node(-15,
      new node(5,
        new node(-8,
          new node(2, NULL, NULL),
          new node(6, NULL, NULL)),
        new node(1, NULL, NULL)),
      new node(6, 
        new node(3, NULL, NULL),
        new node(9, NULL,
          new node(0,
            new node(4, NULL, NULL),
            new node(-1, 
              new node(10, NULL, NULL),
              NULL)))));

  printBST(root);
  convert(root);
  printBST(root);
  return 0;
}
