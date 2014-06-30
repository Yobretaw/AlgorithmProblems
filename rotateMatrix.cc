#include <iostream>
#include <vector>
using namespace std;

void rotate(vector<vector<int> > &m) {
	int size = m.size();
	int tmp = 0;

	for(int i = 0; i < size/2; i++) {
		for(int j = i; j < size - i - 1; j++) {
			tmp = m[i][j];
			m[i][j] = m[size-j-1][i];
			m[size-j-1][i] = m[size-i-1][size-j-1];
			m[size-i-1][size-j-1] = m[j][size-i-1];
			m[j][size-i-1] = tmp;
		}
	}
}

int main() {
	int size = 10;
	vector<vector<int> >m;
	for(int i = 0; i < size; i++) {
		vector<int> n;
		for(int j = size*i+1; j <= size * i+size; j++) {
			n.push_back(j);
		}
		m.push_back(n);
	}

	for(int i = 0; i < size; i++) {
		for(int j = 0; j < size; j++) {
			cout << m[i][j] << " ";
		}
		cout << endl;
	}

	cout << endl;

	rotate(m);


	for(int i = 0; i < size; i++) {
		for(int j = 0; j < size; j++) {
			cout << m[i][j] << " ";
		}
		cout << endl;
	}
}
