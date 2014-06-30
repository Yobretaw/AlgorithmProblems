#include <iostream>
#include <string>
using namespace std;

void remove(char str[]) {
	bool preIsA = false;

	int i = 0;
	int j = 0;

	while(str[i] != '\0') {
		char c = str[i];
		char nextchar = str[i+1];

		if(c == 'b') {
			i++;
			continue;
		}
		if(nextchar == '\0') {
			str[j++] = str[i];
			break;
		}
		else if(c == 'a' && nextchar == 'c') {
			i += 2;
		}
		else
			str[j++] = str[i++];
	}

	str[j] = '\0';
}

int main() {
	char s[] = "babababababacacacacacacabababac";
	remove(s);
	cout << s << endl;
}
