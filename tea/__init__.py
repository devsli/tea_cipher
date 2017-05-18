#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The Tiny Encryption Algorithm.
Copyright Amezoure, 2017. All rights reserved.
'''

from ctypes import c_uint32
from struct import pack, unpack


__all__ = (
    # Standard TEA encrypting
    'tea_encrypt', 'tea_decrypt'
)


def tea_encrypt(plaintext, key):
    '''
    Encrypt a 64 bits plaintext using a given 128 bits key.
    Return a 64 bits encrypted string as a bytes object.
    '''

    v0, v1 = (c_uint32(i) for i in unpack('<2I', plaintext))
    k0, k1, k2, k3 = (c_uint32(i) for i in unpack('<4I', key))
    sm, delta = c_uint32(0), c_uint32(0x9E3779B9)

    for i in range(32):
        sm.value += delta.value
        v0.value += ((v1.value << 4) + k0.value) ^ (v1.value + sm.value) ^ ((v1.value >> 5) + k1.value)
        v1.value += ((v0.value << 4) + k2.value) ^ (v0.value + sm.value) ^ ((v0.value >> 5) + k3.value)

    return pack('<2I', v0.value, v1.value)


def tea_decrypt(ciphertext, key):
    '''
    Decrypt a 64 bits ciphertext using a given 128 bits key.
    Return a 64 bits decrypted string as a bytes object.
    '''

    v0, v1 = (c_uint32(i) for i in unpack('<2I', ciphertext))
    k0, k1, k2, k3 = (c_uint32(i) for i in unpack('<4I', key))
    sm, delta = c_uint32(0xC6EF3720), c_uint32(0x9E3779B9)

    for i in range(32):
        v1.value -= ((v0.value << 4) + k2.value) ^ (v0.value + sm.value) ^ ((v0.value >> 5) + k3.value)
        v0.value -= ((v1.value << 4) + k0.value) ^ (v1.value + sm.value) ^ ((v1.value >> 5) + k1.value)
        sm.value -= delta.value

    return pack('<2I', v0.value, v1.value)
