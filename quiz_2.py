# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
# Written by *** and Eric Martin for COMP9021


import sys

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def display_encoded_set(encoded_set):
    encoded_set = bin(encoded_set)[2:][:: -1]
    print('{', end='')
    found_bit = False
    for i in range(len(encoded_set) // 2 * 2 - 1, -1, -2):
        if encoded_set[i] == '1':
            if found_bit:
                print(', ', end='')
            print(-(i + 1) // 2, end='')
            found_bit = True
    for i in range(0, len(encoded_set), 2):
        if encoded_set[i] == '1':
            if found_bit:
                print(', ', end='')
            print(i // 2, end='')
            found_bit = True
    print('}')


def code_derived_set(encoded_set):
    encoded_running_sum = 0
    # For "encoded_set" coding {e_1, e_2, ..., e_n},
    # listed in increasing order,
    # running_sums will eventually be the list
    # [e_1, e_1 + e_2, e_1 + e_2 + e_3, ... e_1 + ... + e_n]
    running_sums = []
    # Will successively take the values
    # e_1, e_1 + e_2, e_1 + e_2 + e_3, ... e_1 + ... + e_n,
    # appended to running_sums
    running_sum = 0
    # As done in display_encoded_set()...
    encoded_set = bin(encoded_set)[2:][:: -1]
    # REPLACE THIS COMMENT WITH YOUR CODE
    for i in range(len(encoded_set) // 2 * 2 - 1, -1, -2):
        if encoded_set[i] == '1':
            running_sum += -(i + 1) // 2
            running_sums.append(running_sum)
    for i in range(0, len(encoded_set), 2):
        if encoded_set[i] == '1':
            running_sum += i // 2
            running_sums.append(running_sum)
    for num in set(running_sums):
        if num < 0:
            encoded_running_sum += 2**(-num*2-1)
        else:
            encoded_running_sum += 2**(num*2)
    return encoded_running_sum


print('The encoded set is: ', end='')
display_encoded_set(encoded_set)

print('The derived encoded set is: ', end='')
display_encoded_set(code_derived_set(encoded_set))
