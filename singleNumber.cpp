#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

int singleNumber(int a[], int n);

int main(int argc, const char *argv[])
{
    int count = 100;
    int a[count];
    for (int i = 0; i < count; i++) {
        a[i] = count % 3;
    }
    /*
    for (int i = 0; i < 16; i++) {
        a[i] *= 3;
    }
    */
    cout << singleNumber(a, count) << endl;
   return 0;
}

int singleNumber(int a[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        if( sum > 0 ) sum -= a[i];
        else sum += a[i];
        i++;
    }

    return sum;
}
