#include <iostream>
#include <string>
using namespace std;

int LCS(string a, string b) {
	int m = a.length();
	int n = b.length();
	int result = 0;

	int table[m+1][n+1];
	
	for(int i = 0; i <= m; i++) {
		for(int j = 0; j <= n; j++) {
			if(i == 0 || j == 0)
				table[i][j] = 0;
			else if(a[i - 1] == b[j - 1]) {
				table[i][j] = table[i-1][j-1] + 1;
				result = max(result, table[i][j]);
			}
			else
				table[i][j] = 0;
		}
	}

	return result;
}

int main() {
	string a = "hello";
	string b = "hell";
	cout << LCS("geekforgeeks", "Iamforgours") << endl;
}
