#include "iostream"
#include "cmath"
#include "linkedListStructure.h"
using namespace std;
//                    Sum two linkedlist
// ==============================================================
// Given two numbers represented by a linked list, where each node
// contains a single digit. The digits are stored in order,
// such that the most sigificant digit is at the head of the list. Write a
// function that adds the two numbers and return the sum as a 
// linked list
// 
// Example
// input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
// output: 9 -> 0 -> 7
// ==============================================================

node* sumList_help(node* l, node* s, int diff, int& carry, node* head) {
  if(l == NULL && s == NULL) {
    return NULL;
  }

  node* rest;
  if(diff != 0) {
    rest = sumList_help(l->next, s, diff - 1, carry, head);
  } else {
    rest = sumList_help(l->next, s->next, 0, carry, head);
  }

  int sum = l->val + carry + ((diff == 0) ? s->val : 0);
  carry = sum / 10;
  sum = sum % 10;

  if(carry != 0 && l == head) {
    return new node(carry, new node(sum, rest));
  }

  return new node(sum, rest);
}

node* sumList(node* a, node* b) {
  int alen = len(a);
  int blen = len(b);

  int diff = abs(alen - blen);
  node* l = alen >= blen ? a : b;
  node* s = alen < blen ? a : b;

  int carry = 0;
  return sumList_help(l, s, diff, carry, l);
}

// Given two numbers represented by a linked list, where each node
// contains a single digit. The digits are stored in reverse order,
// such that the right most digit is at the head of the list. Write a
// function that adds the two numbers and return the sum as a 
// linked list
// 
// Example
// input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
// output: 8 -> 0 -> 8
// ==============================================================

node* sumListReverse(node* a, node* b, int carry) {
  if(a == NULL && b == NULL) {
    if(carry != 0) {
      return new node(carry, NULL);
    }
    
    return NULL;
  }

  int sum = carry;
  sum += (a == NULL) ? 0 : a->val;
  sum += (b == NULL) ? 0 : b->val;

  int digit = sum % 10;
  carry = sum / 10;

  return new node(digit, sumListReverse((a == NULL) ? NULL : a->next,
                                        (b == NULL) ? NULL : b->next,
                                        carry));
}

int main()
{
  node* a = new node(3, new node(1, new node(5, NULL)));
  node* b = new node(5, new node(9, new node(2, NULL)));
  node* c = new node(4, new node(9, new node(6, new node(9, NULL))));

  printNode(sumList(a, b));
  printNode(sumList(a, c));
  printNode(sumList(b, c));

  printNode(sumListReverse(a, b, 0));
  printNode(sumListReverse(a, c, 0));
  printNode(sumListReverse(b, c, 0));
  return 0;
}
