from numpy import matrix, array

GENERATOR_MATRIX = matrix([
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
])

REGENERATOR_MATRIX = matrix([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
])

PARITY_CHECK_MATRIX = matrix([
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
])

HAMMINGCODE_MARKER_POSITIONS = [
    [1, 2], [1, 3], [1, 4],
    [2, 1], [2, 2], [2, 3], [2, 4], [2, 5],
    [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
    [4, 1], [4, 2], [4, 3], [4, 4], [4, 5],
    [5, 2], [5, 3], [5, 4],
]

def encode(bits):
    encoded_code = ''
    if len(bits) % 4 != 0:
        raise ValueError('Only a multiple of 4 as bits are allowed.')
    while len(bits) >= 4:
        four_bits = bits[:4]
        bit_array = generate_bit_array(four_bits)
        hamming_code = matrix_array_multiply_and_format(GENERATOR_MATRIX, bit_array)
        encoded_code += ''.join(hamming_code)
        bits = bits[4:]
    return encoded_code


def decode(bits):
    decoded_code = ''
    if len(bits) % 7 != 0:
        raise ValueError('Only a multiple of 7 as bits are allowed.')
    for bit in bits:
        if int(bit) not in [0, 1]:
            raise ValueError('The provided bits contain other values that 0 or 1: %s' % bits)
    while len(bits) >= 7:
        seven_bits = bits[:7]
        uncorrected_bit_array = generate_bit_array(seven_bits)
        corrected_bit_array = parity_correct(uncorrected_bit_array)
        decoded_bits = matrix_array_multiply_and_format(REGENERATOR_MATRIX, corrected_bit_array)
        decoded_code += ''.join(decoded_bits)
        bits = bits[7:]
    return decoded_code


def parity_correct(bit_array):
    # Check the parity using the PARITY_CHECK_MATRIX
    checked_parity = matrix_array_multiply_and_format(PARITY_CHECK_MATRIX, bit_array)
    parity_bits_correct = True
    # every value as to be 0, so no error accoured:
    for bit in checked_parity:
        if int(bit) != 0:
            parity_bits_correct = False
    if not parity_bits_correct:
        error_bit = int(''.join(checked_parity), 2)
        for index, bit in enumerate(bit_array):
            if error_bit == index + 1:
                if bit == 0:
                    bit_array[index] = 1
                else:
                    bit_array[index] = 0
    return bit_array


def matrix_array_multiply_and_format(matrix, array):
    unformated = matrix.dot(array).tolist()[0]
    return [str(bit % 2) for bit in unformated]


def generate_bit_array(bits):
    return array([int(bit) for bit in bits])


def extract_hamming_code(mat):
    hamming_code = ''
    for pos in HAMMINGCODE_MARKER_POSITIONS:
        hamming_code += str(int(mat[pos[0], pos[1]]))
    return hamming_code
