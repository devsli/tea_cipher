The Tiny Encryption Algorithm
=============================
*Simple and fast symmetric-key algorithm cipher*

Reference:
----------
.. code:: python

    >>> tea_encrypt(b'barbecue', b'good for nothing')
    b'\xa38\x82\xb7\xc6\xa6\xa8c'
    >>> tea_decrypt(b'\xa38\x82\xb7\xc6\xa6\xa8c', b'good for nothing')
    b'barbecue'

    >>> xtea_encrypt(b'american', b'vegetable garden')
    b'\x8c\x14\xa5\xab\x1b\n\xc4\xf0'
    >>> xtea_decrypt(b'\x8c\x14\xa5\xab\x1b\n\xc4\xf0', b'vegetable garden')
    b'american'

Installation:
-------------
.. code:: sh

    # from GitHub:
    git clone git://github.com/amezoure/tea_cipher.git
    cd tea_cipher && python setup.py install

    # or just from PyPI:
    pip install --upgrade tea_cipher

Properties:
-----------
TEA has a few weaknesses. Most notably, it suffers from equivalent keys-each
key is equivalent to three others, which means that the effective key size is
only 126 bits. As a result, TEA is **especially bad as a cryptographic hash
function**. TEA is also susceptible to a related-key attack which requires
8388608 chosen plaintexts under a related-key pair, with 4294967296 time
complexity. Because of these weaknesses, the XTEA cipher was designed.
