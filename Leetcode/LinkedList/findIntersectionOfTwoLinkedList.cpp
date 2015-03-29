#include <iostream>
#include <linkedListStructure.h>
using namespace std;

node* findIntersection(node* a, node* b) {
  int len_a = 0;
  int len_b = 0;
  
  node* aa = a;
  node* bb = b;

  while(aa) {
    aa = aa->next;
    len_a++;
  }
  while(bb) {
    bb = bb->next;
    len_b++;
  }

  node* longer = (len_a > len_b)? a : b;
  node* shorter = (len_a < len_b)? a : b;
  int diff = abs(len_a - len_b);

  while(diff > 0) {
    longer = longer->next;
    diff--;
  }
  
  while(longer != NULL) {
    if(longer == shorter) return longer;
    longer = longer->next;
    shorter = shorter->next;
  }

  return NULL;
}

int main() {
  node* share = makenode(15, makenode(30, NULL));
  node* a = makenode(3, makenode(6, makenode(9, share)));
  node* b = makenode(10, share);
  cout << findIntersection(a, b)->val << endl;      // should output 15
}

