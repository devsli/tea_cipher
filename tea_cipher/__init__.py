#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The Tiny Encryption Algorithm.
Simple and fast symmetric-key algorithm cipher.

Functions:
    tea_encrypt(), tea_decrypt() -- standard TEA encrypting.
    xtea_encrypt(), xtea_decrypt() -- extended TEA encrypting.
'''

__all__ = ('tea_encrypt', 'tea_decrypt', 'xtea_encrypt', 'xtea_decrypt')
__version__ = '0.3.3'

from ctypes import c_uint32 as uint32
from struct import pack, unpack


def tea_encrypt(plaintext, key, delta=0x9E3779B9):
    '''
    Encrypt a plaintext using TEA algorithm.

    plaintext: 64 bits length bytes-like object.
    key: 128 bits length bytes-like object.

    Return a 64 bits length bytes object.
    '''

    v0, v1 = map(uint32, unpack('>2I', plaintext))
    k0, k1, k2, k3 = map(uint32, unpack('>4I', key))
    sm, delta = uint32(0), uint32(delta)

    for i in range(32):
        sm.value += delta.value
        v0.value += ((v1.value << 4) + k0.value) ^ (v1.value + sm.value) ^ ((v1.value >> 5) + k1.value)
        v1.value += ((v0.value << 4) + k2.value) ^ (v0.value + sm.value) ^ ((v0.value >> 5) + k3.value)

    return pack('>2I', v0.value, v1.value)


def tea_decrypt(ciphertext, key, delta=0x9E3779B9):
    '''
    Decrypt a ciphertext using TEA algorithm.

    ciphertext: 64 bits length bytes-like object.
    key: 128 bits length bytes-like object.

    Return a 64 bits length bytes object.
    '''

    v0, v1 = map(uint32, unpack('>2I', ciphertext))
    k0, k1, k2, k3 = map(uint32, unpack('>4I', key))
    sm, delta = uint32(0xC6EF3720), uint32(delta)

    for i in range(32):
        v1.value -= ((v0.value << 4) + k2.value) ^ (v0.value + sm.value) ^ ((v0.value >> 5) + k3.value)
        v0.value -= ((v1.value << 4) + k0.value) ^ (v1.value + sm.value) ^ ((v1.value >> 5) + k1.value)
        sm.value -= delta.value

    return pack('>2I', v0.value, v1.value)


def xtea_encrypt(plaintext, key):
    '''
    Encrypt a plaintext using XTEA algorithm.

    plaintext: 64 bits length bytes-like object.
    key: 128 bits length bytes-like object.

    Return a 64 bits length bytes object.
    '''

    v0, v1 = map(uint32, unpack('>2I', plaintext))
    k = tuple(map(uint32, unpack('>4I', key)))
    sm, delta = uint32(0), uint32(0x9E3779B9)

    for i in range(32):
        v0.value += (((v1.value << 4) ^ (v1.value >> 5)) + v1.value) ^ (sm.value + k[sm.value & 3].value)
        sm.value += delta.value
        v1.value += (((v0.value << 4) ^ (v0.value >> 5)) + v0.value) ^ (sm.value + k[(sm.value >> 11) & 3].value)

    return pack('>2I', v0.value, v1.value)


def xtea_decrypt(ciphertext, key):
    '''
    Decrypt a ciphertext using XTEA algorithm.

    ciphertext: 64 bits length bytes-like object.
    key: 128 bits length bytes-like object.

    Return a 64 bits length bytes object.
    '''

    v0, v1 = map(uint32, unpack('>2I', ciphertext))
    k = tuple(map(uint32, unpack('>4I', key)))
    sm, delta = uint32(0xC6EF3720), uint32(0x9E3779B9)

    for i in range(32):
        v1.value -= (((v0.value << 4) ^ (v0.value >> 5)) + v0.value) ^ (sm.value + k[(sm.value >> 11) & 3].value)
        sm.value -= delta.value
        v0.value -= (((v1.value << 4) ^ (v1.value >> 5)) + v1.value) ^ (sm.value + k[sm.value & 3].value)

    return pack('>2I', v0.value, v1.value)
