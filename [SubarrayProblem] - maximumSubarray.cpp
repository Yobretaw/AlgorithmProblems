// ==========================================
// find the contiguous subarray within a one-
// dimensional array of numbers which has lar-
// est sum 
//
// Complexity: O(n)
// LANG		 : C++
// ==========================================

#include <iostream>
using namespace std;

// a is the input array with length n
int maxSubarray( int* numbers, int n ) {
	int max_so_far		= numbers[0];
	int max_ending_here = numbers[0];

	for( int i = 1; i < n; i++ ) {
		if( max_ending_here < 0 ) {
			max_ending_here = numbers[i];
		}
		else {
			max_ending_here += numbers[i];
		}

		if( max_ending_here >= max_so_far ) {
			max_so_far = max_ending_here;
		}
	}

	return (max_so_far > 0)?max_so_far:0;
}

int main() {
	int a[5] = {100, 100, -2, 100, 100};
	cout << maxSubarray( a, 5 ) << endl;
	return 0;
}
