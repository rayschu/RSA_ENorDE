#!/usr/bin/env python

import binascii

def RSA_En(plain, e, n):
    cipher = hex(pow(plain, e, n)).rstrip("L")
    return cipher

def RSA_De(cipher, d, n):
    plain = hex(pow(cipher, d, n)).rstrip("L")
    return binascii.unhexlify(plain[2:])
