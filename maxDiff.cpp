// ============================================
// There is an integer array consisting positive
// and negative integers. Find maximum positive
// difference S defined as:
//
// 		S = a[i] - a[j] where i > j
// and
// 		S > 0
//
// LANG: C++
// Running Time: O(n)
// ============================================
//
#include <iostream>
using namespace std;

void MaxDiff( int a[], int sz, int& start, int& end ) {
	int min = 0;
	int maxDiff = 0;
	start = end = 0;
	for( int i = 0; i < sz; i++ ) {
		if( a[i] < a[min] )
			min = i;
		int diff = a[i] - a[min];
		if( diff > maxDiff ) {
			start = min;
			end = i;
			maxDiff = diff;
		}
	}
}
