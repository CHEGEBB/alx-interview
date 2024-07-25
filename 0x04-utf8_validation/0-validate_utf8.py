#!/usr/bin/python3
"""
Module for Validating UTF-8 Encoding
"""

def validate_utf8(data):
    """
    Check if the given list of integers represents valid UTF-8 encoded data.
    :param data: List of integers
    :return: True if valid UTF-8 encoding, otherwise False
    """
    # Counter for the number of bytes remaining in the current UTF-8 character
    bytes_remaining = 0

    # Bit masks to identify the leading bits of each byte
    first_bit_mask = 1 << 7  # Binary: 10000000
    second_bit_mask = 1 << 6  # Binary: 01000000

    # Iterate over each integer in the data list
    for byte in data:
        bitmask = 1 << 7
        if bytes_remaining == 0:
            # Count the number of leading 1's in the first byte
            while bitmask & byte:
                bytes_remaining += 1
                bitmask >>= 1

            # If it's a single-byte character (0xxxxxxx) or continuation byte (10xxxxxx)
            if bytes_remaining == 0:
                continue

            # UTF-8 encoded characters should be between 1 and 4 bytes long
            if bytes_remaining == 1 or bytes_remaining > 4:
                return False
        else:
            # Subsequent bytes must start with 10xxxxxx
            if not (byte & first_bit_mask and not (byte & second_bit_mask)):
                return False

        # Decrease the counter for the bytes remaining in the current character
        bytes_remaining -= 1

    # Ensure all characters have been completely validated
    return bytes_remaining == 0

# Test cases
if __name__ == "__main__":
    sample_data1 = [65]
    print(validate_utf8(sample_data1))  # Expected output: True

    sample_data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validate_utf8(sample_data2))  # Expected output: True

    sample_data3 = [229, 65, 127, 256]
    print(validate_utf8(sample_data3))  # Expected output: False
