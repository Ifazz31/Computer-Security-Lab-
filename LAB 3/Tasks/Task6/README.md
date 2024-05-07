## Task 6

1. Create a text file and add some text.
2. Generate a keyed hash using `HMAC-MD5` algorithm

```bash
openssl dgst -md5 -hmac "abcdefg" plain.txt
```
3. Generate a keyed hash using `HMAC-SHA256` algorithm

```bash
openssl dgst -sha256 -hmac "abc123" plain.txt
```
4. Generate a keyed hash using `HMAC-SHA1` algorithm

```bash
openssl dgst -sha1 -hmac "abc123efg" plain.txt
```