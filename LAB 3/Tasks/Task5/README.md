## Task 5

The instructions are followed by the given steps:

1. Create a text file with some text in it.
2. Use the `SHA-256` (Secure Hash Algorithm) hashing algorithm by the following command:

```bash
openssl dgst -sha256 sample.txt
```
3. Use the `Message digest 5` hashing algorithm by the following command:

```bash
openssl dgst -md5 sample.txt
```
4. Use the `SHA-1` hashing algorithm by the following command:

```bash
openssl dgst -sha1 sample.txt
```

- Among the trio, SHA-256 offers the lengthiest hash output and is widely regarded as the most robust in terms of security.
- Despite its speed, MD5 is deemed insecure and is advised against for security reasons.
- SHA-1, although stronger than MD5, is susceptible to collision attacks, rendering it less secure than SHA-256. Consequently, it's gradually being replaced by more resilient hashing algorithms.