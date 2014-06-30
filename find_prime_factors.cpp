// =====================================
// Given a positive integer n, find all 
// prime factors smaller than n
//
// Runtime: O(sqrt(n))
// LANG	  : C++
// =====================================

#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

vector<int> find_largest_prime_factor( long long n ) {
	vector<int> primes;
	long long d = 2;
	while( n > 1 ) {
		if( n % d == 0 ) {
			primes.push_back(d);
			while(n % d == 0)
				n /= d;
		}

		d++;
		if( d * d > n ) {
			if( n > 1 ) {
				primes.push_back(n);
				return primes;
			}
			return primes;
		}
	}
	return primes;
}

int main() {
	long long n = 3379849318032121231;
	//long long n = 1233;
	vector<int> primes = find_largest_prime_factor(n);
	for( vector<int>::iterator i = primes.begin(); i != primes.end(); i++ )
		cout << *i << endl;
//	cout << primes.back() << endl;

}
