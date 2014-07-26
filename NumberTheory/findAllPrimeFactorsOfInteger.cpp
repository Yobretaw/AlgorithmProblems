#include "iostream"
#include "vector"
using namespace std;

vector<int> findAll_one(long long n) {
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

vector<int> findAll_two(long long n) {
    int pre = -1;
    vector<int> primes;

    long long d = 2;
    while( d * d < n ) {
      if(n % d == 0) {
        if( d != pre ) {
          pre = d;
          primes.push_back(d);
          n /= d;
        }
      } else {
        d++;
      }
    }
    
    if(n != 1)
      primes.push_back(d);
    return primes;
}

int main()
{
  long long n = 600851475143;
  //long long n = 625;
  vector<int> primes = findAll_one(n);
  vector<int> primess = findAll_two(n);
  for(int i = 0; i < (int)primes.size(); i++) {
    cout << primes[i] << endl;
  }
  cout << endl;
  for(int i = 0; i < (int)primess.size(); i++) {
    cout << primess[i] << endl;
  }

  return 0;
}
