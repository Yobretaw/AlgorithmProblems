#include "iostream"
#include "vector"
using namespace std;

vector<int> findAll_one(long long n) {
  vector<int> primes;

  long long d = 2;
  long long pre = -1;
  while( n > 1 ) {
    while( n % d == 0 ) {
      if(d != pre) {
        pre = d;
        primes.push_back(d);
      }
      n /= d;
    }

    d++;
    if(d * d  > n) {
      if (n > 1) {
        primes.push_back(n);
      }
      
      break;
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
        n /= d;
        if( d != pre ) {
          pre = d;
          primes.push_back(d);
        }
      } else {
        d++;
      }
    }
    
    if(n != 1)
      primes.push_back(n);

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
