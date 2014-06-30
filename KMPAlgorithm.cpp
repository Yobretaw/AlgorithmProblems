#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

int kmp(string t, string p);
int* failureArray(string p);

int main(int argc, const char *argv[])
{
	//string t = "abaxyabacabbaababacaba";
	//string s = "she sells seashells";
	//string s = "ababac";
	string s = "abracadabracapabra";

	//cout << kmp(t, s) << endl;
	int* f = failureArray(s);
	for (int i = 0; i < s.length(); i++) {
		cout << f[i] << endl;
	}
	return 0;
}


int kmp(string t, string p) {
	int* f = failureArray(p);
	int i = 0, j = 0;

	while (i < t.length()) {
		if (t[i] == p[j]) {
			if (j == p.length()-1) {
				delete [] f;
				return i - j;		// match
			} else {
				i++;
				j++;
			}
		} else {
			if (j > 0) {
				j = f[j-1];
			} else {
				i++;
			}
		}
	}

	/*
	cout << "failureArray" << endl;
	for (int i = 0; i < p.length(); i++) {
		cout << f[i] << endl;
	}
	cout << "end" << endl;
	*/

	delete [] f;
	return -1;		// no match
}

int* failureArray(string p) {
	int* f = new int[p.length()];
	f[0] = 0;

	int i = 1, j = 0;
	while (i < p.length()) {
		if (p[i] == p[j]) {
			f[i] = j + 1;
			i++;
			j++;
		} else if (j > 0) {
			j = f[j-1];
		} else {
			f[i] = 0;
			i++;
		}
	}

	return f;
}


