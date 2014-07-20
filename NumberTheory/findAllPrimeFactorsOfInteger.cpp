#include "iostream"
#include "vector"
using namespace std;

vector<int> find_largest_prime(long long n) {
  vector<int> primes;

  long long d = 2;
  while( n > 1 ) {
    while( n % d == 0 ) {
      if(primes.size() == 0) primes.push_back(d);
      if(primes.size() > 0 && d != primes[primes.size()-1]) {
        primes.push_back(d);
      }
      n /= d;
    }

    d++;
    if(d * d  > n) {
      if (n > 1) {
        primes.push_back(n);
        return primes;
      }
    }
  }

  return primes;
}

int main()
{
  long long n = 600851475143;
  //long long n = 625;
  vector<int> primes = find_largest_prime(n);
  for(int i = 0; i < (int)primes.size(); i++) {
    cout << primes[i] << endl;
  }

  return 0;
}
