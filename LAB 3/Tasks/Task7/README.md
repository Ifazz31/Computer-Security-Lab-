## Task 7

The instructions are followed in the given steps:

1. Create a text file and add some text in it.
2. Generate the hash value H1 for this file using `SHA-256` hash algorithm using the following command:

```bash
openssl dgst -sha256 -hmac "abc123" plain.txt
```
3. Now changed one bit of input and again generated hash value H2
We can see that the hash values (H1 and H2) are not same. So we can see that changing only 1 bit has totally changed the hash value.
We can see that the hash values (H1 and H2) are not same. The we can use the following code to see how many bits are same.

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    string h1, h2;
    cin >> h1 >> h2;
    int same = 0;
    for (int i = 0; i < h1.size(); i++)
    {
        if (h1[i] == h2[i])
        {
            same++;
        }
    }
    cout << "Number of same bit: " << same << "\n";
    return 0;
}
```
Output:

```
Number of same bit: 3
```
So we can say changing only one input can change the whole hash value. 