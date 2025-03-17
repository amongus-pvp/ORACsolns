def find_sequence_end(start, length, size, dna, target_char):
    """
    Searches for a sequence of `target_char` of length `length` starting from `start`.
    Returns the index where the sequence ends, or -1 if not found.
    """
    count = 0
    for i in range(start, size):
        if dna[i] == target_char:
            count += 1
            if count == length:
                return i
    return -1
 
def is_valid_venom_level(length, size, dna):
    """
    Checks if the DNA can be transformed into the format S^x N^x A^x K^x E^x
    for the given venom level `length`.
    """
    s_end = find_sequence_end(0, length, size, dna, 'S')
    if s_end < 0:
        return False
 
    n_end = find_sequence_end(s_end + 1, length, size, dna, 'N')
    if n_end < 0:
        return False
 
    a_end = find_sequence_end(n_end + 1, length, size, dna, 'A')
    if a_end < 0:
        return False
 
    k_end = find_sequence_end(a_end + 1, length, size, dna, 'K')
    if k_end < 0:
        return False
 
    e_count = 0
    for i in range(k_end + 1, size):
        if dna[i] == 'E':
            e_count += 1
            if e_count == length:
                return True
    return False
 
def max_venom_level(dna):
    """
    Determines the maximum venom level using binary search.
    """
    s_count = dna.count('S')  # Maximum possible venom level
    low = 1
    high = s_count
    max_level = 0
 
    while low <= high:
        mid = (low + high) // 2
        if is_valid_venom_level(mid, len(dna), dna):
            max_level = mid
            low = mid + 1
        else:
            high = mid - 1
 
    return max_level
 
n = int(input())  # Number of letters in the DNA
dna = input().strip()  # DNA sequence
 
result = max_venom_level(dna)
print(result)
