#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define MAX_SIZE 100

void printParenthesis(int n, int open = 0 , int close = 0, string s = "") {
	if(open == close && close == n) {
		cout << s << endl;
		return;
	}
	
	if(open < n)
		printParenthesis(n, open + 1, close, s + "(");
	if(open > close)
		printParenthesis(n, open, close + 1, s +")");
}

int main() {
	int n = 5;
	printParenthesis(n);
	return 0;
}
