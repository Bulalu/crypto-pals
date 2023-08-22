# the string
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

# should produce
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

# Cryptopals Rule ⭐️
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

# Hex is like a special way of counting that uses 16 symbols instead of 10.
# It's often used to represent computer data in a way that's easy for people to read.
    
# Base64 is a way to turn computer data (like pictures or files) into text so that it can be sent or stored more easily.

import base64

def hex_to_base64(hex_string):
    # Convert the hex string to bytes
    bytes_from_hex = bytes.fromhex(hex_string)
    print(bytes_from_hex)

    # Encode the bytes to base64
    base64_representation = base64.b64encode(bytes_from_hex)

    # Return the base64 representation as a string
    return base64_representation.decode()

if __name__ == '__main__':
    add_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    _base64 = hex_to_base64(add_hex)
    assert(_base64 == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
    
    