
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:

# 1c0111001f010100061a024b53535009181c
# after hex decoding, and when XOR'd against:

# 686974207468652062756c6c277320657965
# should produce:

# 746865206b696420646f6e277420706c6179


def xor_combination(hex_string1, hex_string2):

    # decode hex strings to bytes
    bytes1 = bytes.fromhex(hex_string1)
    bytes2 = bytes.fromhex(hex_string2)

    result = bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
    # b"the kid don't play"

    return result.hex()



hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"


if __name__ == '__main__':
    result = xor_combination(hex_string1, hex_string2)
    assert result, "746865206b696420646f6e277420706c6179"
