def string_bits(string):
    res = ""
    for x in string:
        bits = ''.join(format(ord(x), 'b'))
        while len(bits) != 8:
            bits = '0' + bits
        res += str(bits)
    return res


def bits_string(string):
    data = ""
    for i in range(0, len(string), 8):
        j = min(i+8, len(string))
        char = chr(int(string[i:j], 2))
        data += char
    return data