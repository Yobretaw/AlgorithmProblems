#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include "linkedListStructure.h"
using namespace std;

node* merge(node* head);

int main(int argc, const char *argv[])
{
    /*
    node* head = makenode(3, 
            makenode(1,
                makenode(6,
                    makenode(4, 
                        makenode(9,
                            makenode(5, NULL))))));
    */
    /*
    node* head = makenode( 3,
            makenode( 2, 
                makenode( 4, NULL )));
                */

    node* head = makenode(3, NULL);
    node* cp = head;
    int max = 100000;
    for (int i = 0; i < max; i++) {
        cp->next = makenode(max-i, NULL);
        cp = cp->next;
    }
    head = merge(head);
    printNode(head);
    return 0;
}


node* merge(node* head) {
    
    if( head == NULL ) {
        return NULL;
    }

    if(head->next == NULL) {
        return head;
    }

    node* end = head;
    node* mid = head;
    node* premid = NULL;

    while(end->next != NULL && end->next->next != NULL) {
        end = end->next->next;
        mid = mid->next;
        premid = (premid == NULL)? head : premid->next;
    }

    if(end->next != NULL) {
        mid = mid->next;
        premid = (premid == NULL) ? head : premid->next;
    }

    premid->next = NULL;

    head = merge(head);
    mid = merge(mid);

    node* newhead = ( head->val < mid->val )? head : mid;
    node* newhead_cp = newhead;

    ( head->val < mid->val ) ? ( head = head->next ) : ( mid = mid->next );

    while( head != NULL && mid != NULL ) {
        newhead_cp->next = ( head->val < mid->val ) ? head : mid;
        ( head->val < mid->val ) ? ( head = head->next ) : ( mid = mid->next );
        newhead_cp = newhead_cp->next;
    }

    if( head != NULL ) {
        newhead_cp->next = head;
    } else if( mid != NULL ) {
        newhead_cp->next = mid;
    }

    return newhead;
}

