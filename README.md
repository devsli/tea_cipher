# The Tiny Encryption Algorithm.
**Version:** `0.1`

## Usage:
```python
from tea import tea_encrypt, tea_decrypt

plaintext = input('plaintext: ').encode('ascii', 'ignore')
key = input('key: ').encode('ascii', 'ignore')

encrypted = tea_encrypt(plaintext, key)
decrypted = tea_decrypt(encrypted, key)

print('encrypted: %r' % encrypted)
print('decrypted: %r' % decrypted)
```

## License:
* [MIT License](LICENSE.md)
