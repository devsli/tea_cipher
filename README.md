# The Tiny Encryption Algorithm.
_Simple and fast symmetric-key algorithm cipher_

## Reference:
```python
>>> tea_encrypt(b'barbecue', b'good for nothing')
b'\xa38\x82\xb7\xc6\xa6\xa8c'
>>> tea_decrypt(b'\xa38\x82\xb7\xc6\xa6\xa8c', b'good for nothing')
b'barbecue'

>>> xtea_encrypt(b'american', b'vegetable garden')
b'\x8c\x14\xa5\xab\x1b\n\xc4\xf0'
>>> xtea_decrypt(b'\x8c\x14\xa5\xab\x1b\n\xc4\xf0', b'vegetable garden')
b'american'
```

## Installation:
```sh
git clone git://github.com/amezoure/tea.git
cd tea && python setup.py install
```

## License:
* [MIT License](LICENSE.md)
