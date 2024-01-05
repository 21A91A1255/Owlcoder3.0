#include <iostream>
#include <string>
using namespace std;
 
string toBinary(int n, int len)
{
    string binary;
    for (unsigned i = (1 << len - 1); i > 0; i = i / 2) {
        binary += (n & i) ? "1" : "0";
    }
 
    return binary;
}
 
int main()
{
    int n;
    cin>>n;
    int len = 32;
 
    cout << "The binary representation of " << n << " is " << toBinary(n, len);
 
    return 0;
}