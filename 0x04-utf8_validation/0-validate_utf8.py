#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers where each integer represents one byte
    :return: True if data is a valid UTF-8 encoding, otherwise False
    """
    # This variable will keep track of the number of bytes remaining in the current UTF-8 character
    remaining_bytes = 0

    # Masks to check the leading bits in a byte to determine the byte's role in a UTF-8 character
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    # Iterate through each byte in the data list
    for byte in data:
        # Create a mask for checking the leading bits of the current byte
        mask = 1 << 7
        
        if remaining_bytes == 0:
            # If we are not in the middle of validating a multi-byte character
            # Count the number of leading 1's to determine the length of the character
            while mask & byte:
                remaining_bytes += 1
                mask >>= 1

            # For a 1-byte character, we should have zero leading 1's (i.e., 0xxxxxxx)
            if remaining_bytes == 0:
                continue

            # UTF-8 characters can only be between 1 and 4 bytes long
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            # If we are in the middle of validating a multi-byte character
            # Each subsequent byte must start with '10xxxxxx'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the count of remaining bytes to validate for the current character
        remaining_bytes -= 1

    # If we have processed all characters correctly, remaining_bytes should be zero
    return remaining_bytes == 0

# Main block for testing the function with sample data sets
if __name__ == "__main__":
    test_data1 = [65]
    print(validUTF8(test_data1))  # Expected output: True

    test_data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(test_data2))  # Expected output: True

    test_data3 = [229, 65, 127, 256]
    print(validUTF8(test_data3))  # Expected output: False
